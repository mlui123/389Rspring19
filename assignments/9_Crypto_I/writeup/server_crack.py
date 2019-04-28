#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    # open and read hashes.txt
    hashes = {}
    # open and read passwords.txt
    with open("passwords.txt", "r") as f2:
        passwords = f2.read().splitlines()

    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    for c in characters:
        for p in passwords:
            input = c + p
            temp_hash = hashlib.sha256((input).encode()).hexdigest()
            hashes[temp_hash] = input
            

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    
    # parse data
    # crack 3 times

    for i in range(0,3):
        data = s.recv(1024).decode()
        hash = data.split('\n')[2]
        print("input: " + hash + ", cracked: " + hashes[hash])

        s.send((hashes[hash] + "\n").encode())
        time.sleep(.1)

    flag = s.recv(1024)
    print(flag.decode())
            

if __name__ == "__main__":
    server_crack()