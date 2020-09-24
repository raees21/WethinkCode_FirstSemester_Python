from collections import defaultdict
from functools import reduce

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """Converts words to a list"""

    word_list = split(",.? ",text)
    new_list = list(filter(lambda x: x != "", word_list))
    lower_new_list = [x.lower() for x in new_list]

    return lower_new_list


def words_longer_than(length, text):
    """Shopws only words in a list larger than length"""

    word_list = split(",.? ",text)
    new_list = list(filter(lambda x: x != "" and len(x) > length, word_list))
    lower_new_list = [x.lower() for x in new_list]

    return lower_new_list


def words_lengths_map(text):
    """Counts the word length and groups them"""

    word_list = split(",.? ",text)
    new_list = list(filter(lambda x: x != "", word_list))
    length_list = [len(x) for x in new_list]

    mydictionary = {key: length_list.count(key) for key in sorted(length_list)}

    return mydictionary


def letters_count_map(text):
    """Counts the most common chars and maps them to a dict"""

    words_list = list(text)
    lower_new_list = [x.lower() for x in words_list]
    alphabet_key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    mydictionary = {key: lower_new_list.count(key) for key in sorted(alphabet_key)}

    return mydictionary


def most_used_character(text):
    """Shows the most used char in a string"""

    mydictionary = letters_count_map(text)
    if mydictionary != {} and text != "":
        return max(mydictionary, key=mydictionary.get)
        





#print(convert_to_word_list("These are indeed interesting, an obvious understatement, times. What say you?"))
#print(words_longer_than(4, "hello how Are you Doing"))
#print(words_lengths_map("These are indeed interesting, an obvious understatement, times. What say you?"))
#print(letters_count_map("These are indeed interesting, an obvious understatement, times. What say you?"))
#print(most_used_character("These are indeed interesting, an obvious understatement, times. What say you?"))
