#!/usr/bin/python3
def multiple_returns(sentence):
    Len = len(sentence)
    return (Len, sentence[0] if Len > 0 else 'None')
