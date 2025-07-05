#!/usr/bin/env python3
import sys

pattern = sys.argv[1].lower()

if len(pattern) == 5 and all(char.isalpha() or char == "_" for char in pattern):
    pass
else:
    print("Invalid word")
    sys.exit(1)


def valid_words():
    with open("/usr/share/dict/words", "r") as valid_words:
        word_list = []
        for word in valid_words:
            formatted_words = word.strip().lower()
            if len(formatted_words) == 5:
                word_list.append(formatted_words)
        return word_list


word_list = valid_words()


def find_matches():
    matches = []
    for pattern_words in word_list:
        match = True
        for index, letter in enumerate(pattern_words):
            if pattern[index] != "_" and pattern[index] != letter:
                match = False
                break
        if match:
            matches.append(pattern_words)
    if matches == []:
        print("No matches found.")
    return matches


results = find_matches()
for words in results:
    print(words)
