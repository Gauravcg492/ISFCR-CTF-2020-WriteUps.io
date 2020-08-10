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

