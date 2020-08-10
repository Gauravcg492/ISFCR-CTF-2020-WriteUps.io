# Steganography Challenges
# Can You Read Me?
Challenge Description
------
Mr. Cuddles is a master of psychological manipulation and is probably involved in more crimes than Macavity.
He's hiding something.
Can you read between those [cute eyes](https://github.com/hat-im/ISFCR-Stegano-Writeups/blob/master/Can%20You%20Read%20Me/mr_cuddles.jpg)?

Hint
------
```
Reading helps make things easier to understand
```

Solution
------
Opening the file in a hex editor (or even a text editor) will show you the following text at the end of the file:
```
psst,
hey kid, here's the key: ctf{2228333}
```

Thus we have obtained the flag as **ctf{2228333}**



# Composite Files
Challenge Description
------
I'm hiding
I'm not your prime suspect
I'm not what you think I am

P.S. don't forget to enclose your file in ctf{}
eg: ctf{28392}

Hints
------
```
Is the file really the kind it says it is?
```
```
Can you determine the type of file purely from the content?
```

Solution
------
Run the following command on a Linux terminal:
```
:- $ file prime_candidate.pdf
ASCII text
```

On opening the file in a text editor, we see a list of all five-digit prime numbers except for one which has been replaced with a composite number.
```
...
70111
70117
70121
70123
70139
70141
70157
70163
70179
70181
70183
70199
70201
70207
70223
70229
70237
...
```
On cross-comparing the list with the actual list of prime numbers between 9999 and 99999, we see that 70179 is not a prime number (70179 = 3 * 23393).

Place it inside ctf{} to obtain the flag as **ctf{70179}**



# Dit Dah Bit
Challenge Description
------
All is not what it seems in this image.

Hints
------
```
What's the most common form of human communication with two characters?
```

Solution
-------
Reading the LSB of pixels, we get 
```
11000111101100011110111111010
```

According to [Wikipedia](https://en.wikipedia.org/wiki/Morse_code#Letters,_numbers,_punctuation,_prosigns_for_Morse_code_and_non-English_variants) we can translate this into morse code as **CTF(GIMMEGIMMEMORE)**
Since we know that the flag format is ctf{<flag>}, and that the Morse code for parentheses doesn't specify what kind of parentheses they are, we can assume the flag to be **ctf{gimmegimmemore}**



# Goodbye, Everybody
Challenge Description
------
I can't open this page for some reason and it keeps crashing it's really frustrating really please check it out [here](https://github.com/hat-im/ISFCR-Stegano-Writeups/blob/master/Goodbye%2C%20Everybody/my_home.html)

Hints
------
```
Does the page do anything before it closes?
```
```
Can you stop the page from closing before it does?
```

Solution
------
Inspect the code, especially the script tag.
``` html
<!DOCTYPE html>
<html>
    <script type="text/javascript">
        var _0x51a0=['icaGicaGicaGia==','D3jPDgu=','AxrSzt4k','icaGicaGicbJDa==','Dgv4Dd0ID2HPDa==','icaGidWVAgvHza==','icaGidXIB2r5ia==','icaGicaGica8Da==','zsi+cG==','icaGidWVyM9KEq==','zNSXmZi3m30k','icbnEsb0Aw1Lia==','pgHLywq+cG=='];(function(_0x524e62,_0x51a010){var _0x4a3639=function(_0x2bec63){while(--_0x2bec63){_0x524e62['push'](_0x524e62['shift']());}};_0x4a3639(++_0x51a010);}(_0x51a0,0x1be));var _0x4a36=function(_0x524e62,_0x51a010){_0x524e62=_0x524e62-0x0;var _0x4a3639=_0x51a0[_0x524e62];if(_0x4a36['eySsTa']===undefined){var _0x2bec63=function(_0x3840fc){var _0x5b6a0='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=',_0xf0e295=String(_0x3840fc)['replace'](/=+$/,'');var _0x2326d8='';for(var _0x3726c2=0x0,_0x62c1af,_0x532495,_0x1bf20e=0x0;_0x532495=_0xf0e295['charAt'](_0x1bf20e++);~_0x532495&&(_0x62c1af=_0x3726c2%0x4?_0x62c1af*0x40+_0x532495:_0x532495,_0x3726c2++%0x4)?_0x2326d8+=String['fromCharCode'](0xff&_0x62c1af>>(-0x2*_0x3726c2&0x6)):0x0){_0x532495=_0x5b6a0['indexOf'](_0x532495);}return _0x2326d8;};_0x4a36['muSeYm']=function(_0x33fca9){var _0x4ec82a=_0x2bec63(_0x33fca9);var _0x28e7a0=[];for(var _0x497bf7=0x0,_0x562e9b=_0x4ec82a['length'];_0x497bf7<_0x562e9b;_0x497bf7++){_0x28e7a0+='%'+('00'+_0x4ec82a['charCodeAt'](_0x497bf7)['toString'](0x10))['slice'](-0x2);}return decodeURIComponent(_0x28e7a0);},_0x4a36['UvvxQR']={},_0x4a36['eySsTa']=!![];}var _0x2dd1ca=_0x4a36['UvvxQR'][_0x524e62];return _0x2dd1ca===undefined?(_0x4a3639=_0x4a36['muSeYm'](_0x4a3639),_0x4a36['UvvxQR'][_0x524e62]=_0x4a3639):_0x4a3639=_0x2dd1ca,_0x4a3639;};document[_0x4a36('0xa')](_0x4a36('0x8')),document['write'](_0x4a36('0x3')+_0x4a36('0xb')),document['write'](_0x4a36('0x9')+_0x4a36('0x7')+'is\x20limited'+'\x0a'),document[_0x4a36('0xa')]('\x20\x20\x20\x20\x20\x20\x20\x20</'+'title>\x0a'),document[_0x4a36('0xa')](_0x4a36('0x1')+'>\x0a'),document[_0x4a36('0xa')](_0x4a36('0x2')+_0x4a36('0x0')+_0x4a36('0x4')),document[_0x4a36('0xa')](_0x4a36('0xc')+_0x4a36('0x6')),document[_0x4a36('0xa')](_0x4a36('0x5')+'>');


        alert("I don't wanna talk to you.");
        var fav_song="call it what you want - taylor swift - reputation";
        this[fav_song[0]+fav_song[2]+fav_song[14]+fav_song[31]+fav_song[40]]();
        </script>
</html>
```
Even if we cannot decipher what the obfuscated part of the code does, the part after the alert clearly closes the page. We remove it and open the page again.

Inspecting the code again shows
```html
<body text="white">
  ctf{13273}
</body>
```

Which yields the flag as **ctf{13273}**



# Never Look In The Comments
Challenge Description
------
There's something paranormal about this audio, can you find it?
[head_and_shoulders.wav](https://github.com/hat-im/ISFCR-Stegano-Writeups/blob/master/Never%20Look%20In%20The%20Comments/head__shoulders.wav)

Hints
------
```
All files come with something more than their contents.
```
```
First rule of YouTube, never check the comments.

This is not YouTube.
```

Solution
------
Using [an online tool](https://www.metadata2go.com/) to view the metadata results in:
```
File Name           head_&_shoulders.wav 
File Size           13 MB 
File Type           WAV 
File Type           Extension wav 
Mime Type           audio/x-wav 
Encoding            Microsoft PCM 
Num Channels        2 
Sample Rate         44100 
Avg Bytes Per Sec   176400 
Bits Per Sample     16 
Title               Head & Shoulders 
Product             Audio Diaries: 2003 
Artist              Wayne Kerr 
Comment             ctf{392812} 
Date Created        2003 
Genre               N/A 
Duration            0:01:19 
Category            audio 
Raw Header          52 49 46 46 F4 C8 D3 00 57 41 56 45 66 6D 
                    74 20 10 00 00 00 01 00 02 00 44 AC 00 00 
                    10 B1 02 00 04 00 10 00 64 61 74 61 70 C7 
                    D3 00 04 00 F4 FF 05 00 03 00 F4 FF F3 FF 
                    04 00 06 00 00 00 08 00 
```

Looking at the comments field gives us the flag which is **ctf{392812}**



# Squashed Pizza
Challenge Description
------
There's something paranormal about this audio, can you find it?
[head_and_shoulders.wav](https://github.com/hat-im/ISFCR-Stegano-Writeups/blob/master/Never%20Look%20In%20The%20Comments/head__shoulders.wav)

Hints
------
```
All files come with something more than their contents.
```
```
First rule of YouTube, never check the comments.

This is not YouTube.
```

Solution
------
Using [an online tool](https://www.metadata2go.com/) to view the metadata results in:
```
File Name           head_&_shoulders.wav 
File Size           13 MB 
File Type           WAV 
File Type           Extension wav 
Mime Type           audio/x-wav 
Encoding            Microsoft PCM 
Num Channels        2 
Sample Rate         44100 
Avg Bytes Per Sec   176400 
Bits Per Sample     16 
Title               Head & Shoulders 
Product             Audio Diaries: 2003 
Artist              Wayne Kerr 
Comment             ctf{392812} 
Date Created        2003 
Genre               N/A 
Duration            0:01:19 
Category            audio 
Raw Header          52 49 46 46 F4 C8 D3 00 57 41 56 45 66 6D 
                    74 20 10 00 00 00 01 00 02 00 44 AC 00 00 
                    10 B1 02 00 04 00 10 00 64 61 74 61 70 C7 
                    D3 00 04 00 F4 FF 05 00 03 00 F4 FF F3 FF 
                    04 00 06 00 00 00 08 00 
```

Looking at the comments field gives us the flag which is **ctf{392812}**



# We Need To Go Deeper Part I
Challenge Description
------
Here's a special challenge.
One of the remaining challenges contains an extra hidden key that is stored separately from the other keys. Find it.

A working knowledge of Mr. Robot might be useful.
Hints
------
```
What kind of file among the given challenges has the most space to hide more flags?
```
```
If you need it, the password is the largest prime number formed by the digits {4, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8}
```

Solution
------
This challenge is an extension of [an earlier challenge](https://github.com/hat-im/ISFCR-Stegano-Writeups/tree/master/Can%20You%20Read%20Me). Given the digits in the hints, we find that the biggest prime combination is 8888888888888747.

Now we use [DeepSound](http://jpinsoft.net/deepsound), a steganography tool to extract the encoded file.

When we enter the password, we see that the encoded file is called
```
ctf{38734}.pdf
```
Which gives us the key: **ctf{38734}**
