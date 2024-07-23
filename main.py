import urllib.request
from bs4 import BeautifulSoup


def dictionary():
    try:
        # This prepares the URL webscrape
        url = "https://dictionary.com/browse/"
        word = input("\nType a word to find its meaning ")
        url_word = url + word
        html = urllib.request.urlopen(url_word)

        # Starting the process
        htmlParse = BeautifulSoup(html, 'html.parser')
        synonyms = []

        # This webscrapes all the list elements of the webpage
        for para in htmlParse.find_all("li"):
            synonyms.append(para.get_text())
        result = []

        # This picks out the meaning part of the page
        index = 29
        while index < 31:
            result.append(synonyms[index])
            index = index + 1

        # This finsishes it off for the interface
        for i in result:
            print(f"\n{word} means - " + i)


    except urllib.request.HTTPError:
        print("\nSorry, the word you typed is not in the dictionary")