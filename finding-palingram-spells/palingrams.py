"""Find palingrams in an text dictionary."""

import load_dictionnary

def main():
    word_list = load_dictionnary.load("liste.de.mots.francais.frgut.txt")
    palingrams_list = []

    for word in word_list:
        word_length = len(word)
        if word_length > 1:
            for i in range(1, word_length):
                if word[i::-1] in word_list and word[:i-1:-1] == word[i::]:
                    palingrams_list.append(word[i::-1] + ' ' + word)
                if word[i::] in word_list and word[i::-1] == word[:i+1:]:
                    palingrams_list.append(word + ' ' + word[i::-1])
    print(palingrams_list)
    
if __name_ == "__main__":
    main()
