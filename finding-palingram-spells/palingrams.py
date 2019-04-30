"""Find palingrams in an text dictionary."""

import load_dictionnary

def main():
    """Main function"""
    word_list = load_dictionnary.load("2of4brif.txt")
    palingrams_list = []

    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if word_length > 1:
            for i in range(1, word_length):
                if word[i:] == rev_word[:end-i] and rev_word[end-i] in word_list:
                    palingrams_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_worp[:end-i] in word_lis: 
                    palingrams_list.append((rev_worp[:end - i], word))
    sorted(palingrams_list, key=str.lower)
    print('\nNumber of palingrams = {}\n'.format(len(palingrams_list)))
    print(*palingrams_list, sep="\n")
    
if __name__ == "__main__":
    main()
