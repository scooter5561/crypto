import sys, os, time, subprocess, random, requests
os.chdir(sys.path[0])

print('e : encrypt')
print('d : decrypt')
choice = input('input: ')
while choice not in ('e', 'd'):
    print('not a valid choice')
    choice = input('input: ')
if choice == 'e':
    p = subprocess.Popen(['python', 'crypto.py'])
    p.wait()
if choice == 'd':
    p = subprocess.Popen(['python', 'decrypto.py'])
    p.wait()