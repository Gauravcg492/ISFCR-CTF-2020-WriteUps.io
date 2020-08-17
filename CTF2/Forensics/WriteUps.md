# Forensics Challenges

## Wait a minute...who are you?
```
Please don't take this meme too seriously, there are other things to consider here...
```
+ The link given in the GIF is given so that the partcipants can relax a bit while solving the challenges(By the way here's the link: https://bit.ly/2EEQHU6) xD
+ On looking at the metadata of GIF, using
```bash
exiftool way.gif
```
one would find some numbers at the "Comments" part in the Format: UTF-16
+ Converting it from UTF-16->UTF-8->To Text would do the trick. The decoded text is actually a link, containing a downloadable image which has the flag.
+ Flag:
```
CTF{1'm_4_hum4n_l1k3_y0u}
```

---

## Anime Legacy
```
Hey , have you watched Naruto? Password : (First name of Anime Character shown)
```

+ An image and a password is provided. Password is "kakashi"
+ One may use the website https://www.mobilefish.com/services/steganography/steganography.php to decode the image(Although there may be several other methods for this). Amidst all the gibberish there is some hexadecimal data.
+ Decoding it to text would give us the flag. 
+ Flag:
```
CTF{4n1m3s_4r3_fun_t0_w4tch}
```

## Blank Space
```
Grammy artist Taylor Swift is trying to communicate something through her number on single! Can you figure out what it is?
```
+ Download the file attached [swifties_only.txt](swifties_only.txt)
+ Run ``` exiftool swifties_only.txt``` to get the following output:
```
E645F5F5F5FE645FE645F5F5F E645F5FE645FE645FE645FE645FE645FE645F E645F5F5FE645FE645F5FE645FE645F E645F5FE645F5F5F5F5F5F E645F5F5FE645FE645FE645FE645F5F E645F5F5FE645F5F5F5FE645F E645F5F5FE645FE645F5FE645FE645F E645F5FE645F5F5F5F5F5F E645FE645F5F5FE645FE645F5F5F E645F5F5FE645F5F5FE645F5F E645F5F5F5FE645FE645FE645FE645F E645F5F5F5FE645F5FE645FE645F E645F5F5F5F5FE645FE645F5F E645F5FE645F5F5F5F5F5F E645FE645F5F5FE645FE645FE645F5F E645F5F5FE645FE645F5F5FE645F E645F5F5FE645FE645FE645F5F5F E645F5F5FE645FE645FE645FE645F5F E645F5F5FE645FE645F5FE645FE645F E645FE645F5F5FE645FE645FE645F5F E645FE645F5F5FE645FE645F5F5F E645FE645F5F5FE645F5FE645FE645F E645FE645F5F5FE645F5FE645FE645F E645F5F5FE645FE645FE645F5F5F E645FE645F5F5FE645FE645F5FE645F E645FE645F5F5FE645F5FE645F5F E645F5F5FE645FE645FE645FE645F5F E645FE645F5F5FE645FE645FE645F5F E645FE645F5F5FE645FE645F5FE645F E645FE645F5F5FE645FE645F5FE645F E645F5F5FE645FE645FE645FE645F5F E645FE645F5F5FE645FE645FE645FE645F E645FE645F5F5FE645FE645FE645FE645F E645FE645F5F5FE645F5F5F5F E645FE645F5F5FE645FE645F5FE645F E645FE645F5F5FE645FE645FE645F5F E645F5F5FE645FE645F5FE645F5F E645FE645F5F5FE645F5FE645FE645F E645F5F5FE645FE645FE645FE645F5F E645F5F5FE645FE645F5F5FE645F E645FE645F5F5F5FE645FE645FE645F E645FE645F5F5FE645F5F5FE645F E645F5F5FE645FE645F5FE645FE645F E645F5F5FE645FE645F5FE645F5F E645FE645F5F5FE645FE645FE645F5F E645FE645F5F5FE645FE645F5F5F
```
+ Observe a pattern where 0's are E645F and 1's are 5F. Replace and you'll get:
```
01110011 01000000 01100100 01011111 01100001 01101110 01100100 01011111 00110011 01101101 01110000 01110100 01111001 01011111 00110001 01100110 01100011 01100001 01100100 00110001 00110011 00110100 00110100 01100011 00110010 00110101 01100001 00110001 00110010 00110010 01100001 00110000 00110000 00110111 00110010 00110001 01100101 00110100 01100001 01100110 00111000 00110110 01100100 01100101 00110001 00110011
```

+ Decode this to ascii and you get:
``` 
s@d_and_3mpty_1fcad1344c25a122a00721e4af86de13
```
+ Place this within ctf{}

## Shark Attack

```
I went sea diving, and Chomper the friendly shark handed me this capture. He said he's received this top secret over the wire. Can you help me figure out what it is?
```
+ Download the file attached [secret.pcapng](https://github.com/sivagirish81/ISFCR-CTF-2020-WriteUps.io/blob/master/CTF2/Forensics/secret.pcapng)
+ Open this using any packet tracing tool like Wireshark
+ Follow the UDP stream from 10.0.2.4 to 10.0.2.11
+ You'll get the flag ``` ctf{y0u_dee_P33} ```