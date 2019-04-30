"""Find palindromes (letter palingrams) in a dictionary file."""
import load_dictionnary

def main():
    """main programm"""
    word_list = load_dictionnary.load('liste.de.mots.francais.frgut.txt')
    pali_list = []

    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            pali_list.append(word)

    print('The dictionnary contains {} palindromes'.format(len(pali_list)))
    print(*pali_list, sep='\n')

if __name__ == "__main__":
    main()
