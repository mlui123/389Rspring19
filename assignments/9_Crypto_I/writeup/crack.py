#!/usr/bin/env python3

import hashlib
import string

def crack():
    # open and read hashes.txt
    with open("hashes.txt", "r") as f:
        hashes = f.read().splitlines()

   # open and read passwords.txt
    with open("passwords.txt", "r") as f2:
        passwords = f2.read().splitlines()

    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            # crack hashes
            input = c + p
            temp_hash = hashlib.sha256((input).encode()).hexdigest()

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

            if temp_hash in hashes:
                print(input + ":" + temp_hash)

            

if __name__ == "__main__":
    crack()
