"""Find anagrams from an input od user in a french dictionnary."""

# import sys
from collections import Counter
import load_dictionnary

dic_file = load_dictionnary.load("./finding-palingram-spells/liste.de.mots.francais.frgut.txt")
dic_file.append('a', 'n', 'y', 'l', 'm') #add singleword usualy used
# in french but often mistaken in dictionnary file.
dic_file = sorted(dic_file)

ini_name = input("Enter your full name or a word or a phrase : ")

def find_anagrams(name, list_of_words):
    """Function to get annagram in word list"""
    name_letter_map = Counter(name)
    anagrams_list = []
    for word in list_of_words:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
            if Counter(test) == word_letter_map:
                anagrams_list.append(test)
    print(*anagrams_list, sep='\n')
    print("Remaining letters = {}".format(name))
    print("Number of remaining letters = {}".format(len(name)))
    print("Number of remaining (real word) anagrams ) {}".format(len(anagrams_list)))

def process_choice(name):
    """Function to process choice of user."""
    while True:
        response = input('Enter a word from the list or press Enter to start over or enter # to quit : ')
        if response == '':
            main()
        elif response == '#':
            sys.exit()
        else:
            candidate = ''.join(response.lower().split())
        restin_name_list = list(name)
        for letter in candidate:
            if letter in restin_name_list:
                restin_name_list.remove(letter)
        if len(name) - len(restin_name_list)== len(candidate):
            break
        else print("Please enter an valid choise", file=sys.stderr)
    name = ''join(restin_name_list)
    return response, name

def main():
    """
Main function. Interact with user to choose the best combinations."""

if __name__ == "__main__":
    main()

