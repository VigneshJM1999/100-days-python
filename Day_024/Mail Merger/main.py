#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from tempfile import template

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt", 'r') as file:
    names = file.readlines()


with open("./Input/Letters/starting_letter.txt", 'r') as file:
    template = file.read()

for name in names:
    stripped_name = name.strip()
    file_name = f"./Output/ReadyToSend/{stripped_name}.txt"
    with open(file_name, 'w') as file:
        new_template = template.replace("[name]", stripped_name)
        file.write(new_template)
