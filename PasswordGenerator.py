import random
import pyperclip

# List that are used for character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
specialCharacters =  ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
digits = ["1","2","3","4","5","6","7","8","9"]


characterSets = [] # All the choices of character sets are put in here
passwordLength = NotImplemented
GeneratedPassword = NotImplemented

# Code Below

def prompt_characterset_choices():
    for x in range(4):

        if x == 0:
            Choice = input("Do you wish to include lowercase letters?: Y/N ")
            if Choice == "Y":
                characterSets.append("lowercase letters")
            else:
                continue
        elif x == 1:
            Choice = input("Do you wish to include uppercase letters?: Y/N ")
            if Choice == "Y":
                characterSets.append("uppercase letters")
            else:
                continue
        elif x == 2:
            Choice = input("Do you wish to include digits?: Y/N ")
            if Choice == "Y":
                characterSets.append("digits")
            else:
                continue
        elif x == 3:
            Choice = input("Do you wish to include special characters?: Y/N ")
            if Choice == "Y":
                characterSets.append("special characters")


def generate_character():
    randomInt = random.randint(0, len(characterSets) - 1) # A random choice
    
    option = characterSets[randomInt] # gets that choice
    generatedCharacter = None
    
    if option == "lowercase letters":
        RandomIndex =  random.randint(0, len(letters) - 1)
        generatedCharacter = letters[RandomIndex].lower()
    elif option == "uppercase letters":
        RandomIndex =  random.randint(0, len(letters) - 1)
        generatedCharacter = letters[RandomIndex].upper()
    elif option == "digits":
        RandomIndex =  random.randint(0, len(digits) - 1)
        generatedCharacter = digits[RandomIndex]
    elif option == "special characters":
        RandomIndex =  random.randint(0, len(specialCharacters) - 1)
        generatedCharacter = specialCharacters[RandomIndex]

    return generatedCharacter



def generate_randomized_password(): 
    generatedPassword = None
    strings_to_append = []


    for i in range(int(passwordLength)):
        strings_to_append.append(generate_character())

    generatedPassword = "".join(strings_to_append)
    
    return generatedPassword

#Get Length
passwordLength = input("What is the length of the password you wish to be generated?: ")

#Prompt Options
prompt_characterset_choices()

#Generate Password
GeneratedPassword = generate_randomized_password()
print("Randomized Generated Password: " + GeneratedPassword) 

CopyToClipBoard = input("Do you wish to copy the password to your clipboard: Y/N")

if CopyToClipBoard == "Y" :
    #Copy To Clipboard
    print("Copied")
    pyperclip.copy(GeneratedPassword)