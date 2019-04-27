#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():

    # open and read hashes.txt
    with open("hashes.txt", "r") as f:
        hashes = f.read().splitlines()

   # open and read passwords.txt
    with open("passwords.txt", "r") as f2:
        passwords = f2.read().splitlines()


    characters = string.ascii_lowercase
    server_ip = '134.209.128.58 1337'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)
    # parse data
    # crack 3 times

if __name__ == "__main__":
    server_crack()
