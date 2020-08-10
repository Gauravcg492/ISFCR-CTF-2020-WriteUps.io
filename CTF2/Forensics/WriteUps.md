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
