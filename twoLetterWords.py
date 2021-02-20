import string
import random
from termcolor import colored
import msvcrt

# prevents weird character printout from colored() 
# https://stackoverflow.com/questions/59337634/termcolor-colored-outputting-weird-characters
from colorama import init
init(autoreset = True)

words = []
with open("twoLetterWords.txt", 'r') as f:
    for line in f.readlines():
        words.append(line.strip())
wordSet = set(words)

numRounds = int(input("How many rounds do you want to do? "))
correct = 0
missedWords = []

for i in range(numRounds):
    word = random.choice(words)
    if random.random() < 0.45:
        word = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
    
    print('Is this valid: ' + word + '? (y/n) ')
    answer = msvcrt.getch().decode("utf-8")
    exists = word in wordSet
    existanceWord = "IS" if exists else "ISN'T"

    if (answer == 'y' and exists) or (answer != 'y' and not exists):
        correct += 1
        print(colored("Correct! " + word + " " + existanceWord +  " in the scrabble dictionary.", "green"))
    else:
        print(colored("Wrong! " + word + " " + existanceWord +  " in the scrabble dictionary.", "red"))
        if(existanceWord == "IS"):
            missedWords.append(word)
    
    print('')

print("You got " + str(correct) + "/" + str(numRounds) + " correct.")
print("The words you missed that ARE in the dictionary were:")
for word in missedWords:
    print(word)

input("Press enter to exit")