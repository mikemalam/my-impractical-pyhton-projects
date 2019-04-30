"""Find palingrams in an text dictionary."""

import load_dictionnary

def main():
    """Main function"""
    word_list = load_dictionnary.load("2of4brif.txt")
    palingrams_list = []

    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i] in word_list:
                    palingrams_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list: 
                    palingrams_list.append((rev_word[:end - i], word))
    sorted(palingrams_list)

    #Display list of palingrams.
    print('\nNumber of palingrams = {}\n'.format(len(palingrams_list)))
    for first, second in palingrams_list:
        print("{} {}".format(first, second))

if __name__ == "__main__":
    main()
