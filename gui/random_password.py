#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random, string

class random_password():

    def __init__(self):
        self.char = string.printable[:-11]

    def create_random_password(self, chars=None, seq=8):
        if (chars != None) and (chars != ''):
            self.char = chars
        if seq >= len(self.char):
            self.char *= ((seq//len(self.char)) + 1)
        self.rnd_pass = ''.join(random.sample(self.char,seq))
        return self.rnd_pass

if __name__ == '__main__':
    test = random_password()
    print(test.create_random_password())
