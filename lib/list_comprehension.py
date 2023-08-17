#!/usr/bin/env python3

def return_evens(num_list):
    even_num = [num for num in num_list if num % 2 == 0]
    return even_num

def make_exclamation(sentence_list):
    new_list = [word + '!' for word in sentence_list]
    return new_list