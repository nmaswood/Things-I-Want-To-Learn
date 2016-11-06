import re

class Solution():

    def __init__(self):
        pass


    def strcpy(self, word, delim):

        s = set(delim)

        for (index, letter) in enumerate(word):

            if letter in s:
                return index

        return index

    def strtok(self, word):
        pass

