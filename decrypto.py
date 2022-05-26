import sys, os, re, time
from key import *
os.chdir(sys.path[0])


base_string = input('input: ')

def decrypt(string):
    global base_string
    global database_dict

    encrypted = []
    decrypted = []
    n = 4
    for index in range(0, len(base_string), n):
        encrypted.append(base_string[index : index + n])
        if len(base_string[index : index + n]) < n:
            print('error detected, please make sure you copied the whole encrypted text')
            exit()
    #print(encrypted)
    a = open('decrypted.txt', 'w')
    a.flush()
    a.close()
    b = open('dummy.py', 'w')
    b.write('compiled_string = \'')
    b.flush()
    b.close()
    for block in encrypted:
        item = [k for k, v in database_dict.items() if v == block][0][:-1]
        decrypted.append(item)
        a = open('decrypted.txt', 'a')
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
    
    
    
decrypt(base_string)
from dummy import *
print(compiled_string)