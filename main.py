import requests, os, urllib.request
from bs4 import BeautifulSoup
while True:
    word = input("Type the word for its meaning ")
    # Checks if the user typed c and will clear the terminal if true
    if word == "c":
        os.system('clear')
    # This is what happens when the above statement is false
    else:
        # This if statement checks id the word does actually exist
        try:
            # Starting the process
            url = "https://dictionary.com/browse/"
            url_word = url + word
            html = urllib.request.urlopen(url_word)
            htmlParse = BeautifulSoup(html, 'html.parser')
            meaning = []

            # This web-scrapes all the list elements of the webpage

            for para in htmlParse.find_all("li"):
                meaning.append(para.get_text())

            # This picks out the meaning part of the page
            result = []
            index = 28

            while index < 31:
                result.append(meaning[index])
                index = index + 1

            # This finishes it off for the interface
            for i in result:
                print(f"\n{word} means - " + i + "\n")

        # This handles the code if the word doesn't exist to prevent errors
        except urllib.error.HTTPError:
            print('The word does not exist.')
            
