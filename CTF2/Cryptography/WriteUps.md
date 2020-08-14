# Crypto Challenges

## AbXORb The Energy
```
I met Bhargav and his friend Sanky at the supermarket, to see them purchasing an energy drink.
After asking what was the energy drink, they replied in a monotone "....". What was their reply?
```

+ The challenge name has a hint about the XOR operation
+ Two images were provided. XORing them out would give out the flag.
+ Solution:
```bash
convert sup5.jpg 16.png -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" res_chk.jpg
```
+ Flag:
```
CTF{b0057_15_7h3_53cr37_0f_0ur_3n3rgy}
```

## Bobby and Alice
```
Alice gives Bobby a new encrypted message.
She tells him that she encrypted CTF{xxxx} and that those 'x' are lowercase.
Bobby now challenges you to decrypt the message.
Can you do it?
```
+ Here it was given that CTF{xxxx} was encrypted using RSA algorithm.
+ Since we have the cipher text and the values of n and e, we can try out all 4 letter permutations and place between 'CTF{' and '}'.
+ By encrypting all the permutations and comparing it with the cipher text we can get the right combination which gives us the flag.
+ The python code which could be used is as follows:

```
from Crypto.Util.number import *

n = "given"
e = "given"
c = "given"

alpha = "abcdefghijklmnopqrstuvwxyz"
for i in alpha:
	for j in alpha:
		for k in alpha:
			for l in alpha:
				flag = "CTF{" + i + j + k + l + "}"
				flag_enc = pow(bytes_to_long(flag.encode()), e, n)
				if flag_enc == c:
					print("The flag is " + flag)
					exit(0)
```
+ Flag:
```
CTF{leet}
```

## The Final Gambit
```
Bobby decides to take the matter in his own hands.
He encrypts the key using RSA encryption.
Since his message is long he uses 256 bit public key.
Can you decrypt the cipher?
```
+ Here the flaw of RSA is that it uses 256 bit keys which can be easily cracked by modern tools.
+ One of the tools which can be used to crack the RSA is called YAFU.
+ Since 'n' is small, YAFU can factorize it into 'p' and 'q' in minutes.
+ With the help of 'p' and 'q' we can use online web tools which will generate 'd'.
+ Then using 'd' we can do pow(c,d,n) to get the message.
<img src = "./yafu.PNG" alt = "Error"/>
+ Flag:
```
CTF{Y0u'r3_4_tru3_crpt0_l33t}
```