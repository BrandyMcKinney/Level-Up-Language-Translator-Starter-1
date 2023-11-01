import csv


def intro():
    print(
        "\nWelcome to the French and Spanish translator app! \nPlease enter an English word and press the enter key."
    )

    print('\nType "done" at any time to exit.')
  
def exit():
  print('\nThanks for using the translator app. Have a wonderful day!')



translations = {}

with open("translations.csv", "r") as words:
    reader = csv.DictReader(words, delimiter=",")

    for line in reader:
        english = line["English"].lower()
        spanish = line["Spanish"].lower()
        french = line["French"].lower()
        translations[english] = [spanish, french]

done = False

intro()

while not done:
    word = input("\nPlease type an english word to translate: ").lower()

    if word == "done":
        done = True
    elif word in translations:
        print(f'\n\nSPANISH: {translations[word][0]}')
        print(f'\n\nFRENCH: {translations[word][1]}')
    else:
        print("\nThe word is not listed in the dictionary.")

    exit()
