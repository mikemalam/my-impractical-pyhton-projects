"""How to find voldemort anagram from 'tmvoordle'."""

import sys
from itertools import permutations
from collections import Counter
import load_dictionnary

def main():
    """Main function."""

    name = 'tmvoordle'
    name = name.lower()

    word_dic_ini = load_dictionnary.load('2of4brif.txt')
    trigrams_filter = load_dictionnary.load('least-likely_trigrams.txt')

    word_list = prep_words(name, word_dic_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(name, filtered_cv_map)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)


