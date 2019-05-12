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

For level 2, trying what I did in level 1 did not work. I had to use the last hint which told me to use the onerror attribute. Entering ```<img src="myImage" onerror="alert('hello!')">``` into the status bar worked. This works by loading an image that doesn't exist, thus trigerring the onerror function. <br />

In level 3, I noticed in the target code that the one of the img tags was vulnerable because the variable ```num``` is not checked before being used in the tag. Knowing this, I replaced the frame number with ```my.jpg' onerror='alert("Yo")'/>``` in the url. <br />

For level 4, inspecting the target code was once again helpful. I realized that the startTimer function doesn't check the parameter ```seconds``` before using it. Similar to the previous level, I use the vulnerable image tag to my advantage and put ```3'); alert('Yo``` into the textbox. <br />

For level 5, I noticed that next=confirm in the url. When inspecting the source code, I also saw that the value of the "next" link is also confirm. Knowing this and using the hints, I went to the url ```https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert("Yo")``` and then typed a random email and clicked next. 