#first duo project with broso (aka bwoso)

import sys, os, re, time
from key import *
os.chdir(sys.path[0])

base_string = input('input to encrypt: ')
print('')
counted_chars = {}
been_counted = {}
base_string_string = base_string
base_string = list(base_string)


def count_chars(list):
    global been_counted
    global counted_chars
    dummynum = 1
    for e, char in enumerate(list):
        try:
            if counted_chars[char] == 0:
                pass
        except:
            counted_chars[char] = 0
        counted_chars[char] += 1
        been_counted[dummynum] = (f'{char}{counted_chars[char]}')
        dummynum += 1
    #for char in counted_chars:
    #    print(char, counted_chars[char])
    #print(counted_chars)
    #print(been_counted)
    return been_counted

def encrypt(dict):
    global database_dict
    encrypted = []
    for e, char in enumerate(dict):
        char = dict[char]
        encrypted.append(database_dict[char])
    a = open('encrypted.txt', 'w')
    a.flush()
    a.close()
    b = open('dummy.py', 'w')
    b.write('compiled_string = \'')
    b.flush()
    b.close()
    for item in encrypted:
        a = open('encrypted.txt', 'a')
        a.write(str(item))
        a.flush()
        a.close()
        
        b = open('dummy.py', 'a')
        #print(item)
        if '\\' in item:
            item = item.replace('\\', '\\\\')
        if '\'' in item:
            item = item.replace('\'', '\\\'')
        if '\"' in item:
            item = item.replace('\"', '\\\"')
        b.write(str(item))
        b.flush()
        b.close()
    b = open('dummy.py', 'a')
    b.write('\'')
    b.flush()
    b.close()
    time.sleep(0.5)
compiled_dict = count_chars(base_string)
encrypt(compiled_dict)
from dummy import *
print(compiled_string)
#print(compiled_dict)
