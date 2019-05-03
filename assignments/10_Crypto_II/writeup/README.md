# Crypto II Writeup

Name: *Mitchell Lui*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Mitchell Lui*

## Assignment Writeup

### Part 1 (70 Pts)

I used the commands "gpg --import key.asc" and "gpg --decrypt message.txt.gpg"

The flag that I found was CMSC389R-{m3ss@g3_!n_A_b0ttl3}.

### Part 2 (30 Pts)

![original image](original.bmp)
![ecb image](ecb.bmp)
![cbc image](cbc.bmp)


1. In the ECB encrypted image, the shapes are still visible while while the in the CBC encrypted image, you cannot make out the shapes at all.

2. ECB block cipher mode is less secure. ECB mode works by encrypting each block of the plaintext separately. As a result, the ECB mode encrypts identical plaintext to indentical ciphertext. This explains why we can make out the shapes in the ECB encrypted image because the pixels of the same color are being encrypted the same. The CBC mode is more secure because each block of plaintext is XORed with the previous ciphertext before being encrypted. So each ciphertext depends on the previous plaintext operations. Additionally, the CBC uses an initiialization vector to be XORed with the first plaintext, ensuring that each message is unique.
