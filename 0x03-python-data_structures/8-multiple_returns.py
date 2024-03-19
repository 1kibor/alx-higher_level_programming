#!/usr/bin/python3

def multiple_returns(sentence):
    sentence_length = len(sentence)

    if sentence_length == 0:
        tuple_x = (sentence_length, None)
    else:
        tuple_x = (sentence_length, sentence[0])

    return tuple_x
