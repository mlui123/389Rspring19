# Writeup 2 - OSINT

Name: *Mitchell Lui*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *Mitchell Lui*

## Assignment Writeup

### Part 1 (45 pts)

* 1. v0idcache's real name is Elizabeth Moffet. I found this on twitter through namechk osintframework .
  2. She works at 13/37th national bank  also found on her twitter profile. The website is 1337bank.money.
  3. v0idcache has a twitter account (@v0idcache) and is followed by UMD Cyber Security Club. They also have a github (github.com/v0idcache) and their email found on 1337bank.money was v0idcache@protonmail.com. Their pastebin is https://pastebin.com/WghDuAr7 and  
  4.  From https://ipinfo.info/html/ip_checker.php, I found that the ip address for the website is 142.93.136.81. The geolocation is Ontario Canada.
 It is registered with namecheap and was creted February 6, 2019, last updated February 11, 2019, and expires February 6, 2020.
  5. I checked the robots.txt file which I led me to to 1337bank.money/secret_directory. This had a flag of CMSC389R-{h1ding_fil3s_in_r0bots_L0L}. I also found CMSC389R-{h1dd3n_1n_plain_5ight} from viewing the page source. 
  6. Ports 22(service: ssh), 80(http), 1337(waste) are open. Port 135 (msprc) and 445 had a filtered state. I ran the command nmap 142.93.136.81 -p 1-2000.*
  7. The operating system is Ubuntu. I found this from the details about OpenSSH on shodan.io.
  8. I found CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5} in the txt records from dnsdumpster.com.
### Part 2 (75 pts)

*After running my stub.py file, I found that the password was linkinpark. I then logged in by running the command nc 142.93.136.81 1337 and using v0idcache as the username and linkinpark as the password. I navigated to the home directory where I found the flag.txt file which contained the flag CMSC389R-{bRuT3_f0rce_m4ster}. From the pastebin link https://pastebin.com/WghDuAr7, I proceeded to open AB4300.txt where I found the flag CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}.*
