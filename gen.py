# generator file to make a key database

import random, sys, os

os.chdir(sys.path[0])

limit = 5000 #bruh 10k is a bit much
chars = ['a',
         'b',
         'c',
         'd',
         'e',
         'f',
         'g',
         'h',
         'i',
         'j',
         'k',
         'l',
         'm',
         'n',
         'o',
         'p',
         'q',
         'r',
         's',
         't',
         'u',
         'v',
         'w',
         'x',
         'y',
         'z',
         'A',
         'B',
         'C',
         'D',
         'E',
         'F',
         'G',
         'H',
         'I',
         'J',
         'K',
         'L',
         'M',
         'N',
         'O',
         'P',
         'Q',
         'R',
         'S',
         'T',
         'U',
         'V',
         'W',
         'X',
         'Y',
         'Z',
         '1',
         '2',
         '3',
         '4',
         '5',
         '6',
         '7',
         '8',
         '9',
         '0',
         '`',
         '~',
         '!',
         '@',
         '#',
         '$',
         '%',
         '^',
         '&',
         '*',
         '(',
         ')',
         '-',
         '_',
         '=',
         '+',
         '[',
         '{',
         ']',
         '}',
         '\\',
         '|',
         ';',
         ':',
         '\'',
         '\"',
         ',',
         '<',
         '.',
         '>',
         '/',
         '?',
         ' ',
         ]
# in crypto.py we need to be able to tell how many of each letter there are
database_dict = {}
limitvar = 0
usedcombos = []
for e, char in enumerate(chars):
    while limitvar < limit:
        combo = (f'{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}')
        database_dict[str(char) +str(limitvar)] = combo
        usedcombos.append(combo)
        limitvar += 1
    limitvar = 0
a = open('key.py', 'a')
a.write(f'database_dict = {database_dict}')
a.flush()
a.close()