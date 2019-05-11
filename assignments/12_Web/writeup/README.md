# Crypto II Writeup

Name: *Mitchell Lui*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Mitchell Lui*

## Assignment Writeup

### Part 1 (40 Pts)

I noticed all the links ended in id = some number. From the hint in the title, I figured that I had to use SQL injection. The following link: ```http://1337bank.money:5000/item?id=0'||'1=1```  
gave me the flag ```CMSC389R-{y0u_ar3_th3_SQ1_ninj@}``` <br /> I tried this particular injection from looking up SQL injection on w3schools and using the example they provided.


### Part 2 (60 Pts)

For level 1, simply entering ```<script>alert("Yo!")</script>``` worked. The mission objective pretty much told us to do this and following it worked. <br />

For level 2

