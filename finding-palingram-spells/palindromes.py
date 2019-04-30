"""Find palindromes (letter palingrams) in a dictionary file."""
import load_dictionnary
word_list = load_dictionnary.load('2of4brif.txt')
pali_list = []

for word in word_list:
    if len(xords) > 1 and word == word[::-1]:
        pali_list.append(word)

print('The dictionnary contains {s} palindromes'.format(len(pali_list))
print(pali_list)
