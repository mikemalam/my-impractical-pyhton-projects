"""Find palingrams in an text dictionary."""

import load_dictionnary

def main():
    """Main function"""
    word_list = load_dictionnary.load("2of4brif.txt")
    palingrams_list = []

    for word in word_list:
        word_length = len(word)
        if word_length > 1:
            for i in range(1, word_length):
                if word[i::-1] in word_list and word[:i-1:-1] == word[i::]:
                    palingrams_list.append(word[i::-1] + ' ' + word)
                if word[i::] in word_list and word[i::-1] == word[:i+1:]:
                    palingrams_list.append(word + ' ' + word[i::-1])
    sorted(palingrams_list, key=str.lower)
    print(*palingrams_list, sep="\n")
    
if __name__ == "__main__":
    main()
