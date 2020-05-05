# B==P B==P ...

+ View the text file.
+ Notice the padded == at the end.
+ The heading of the question was a huge giveaway in itself
+ Decrypt using base64
+ It would again end up as base64.
+ Run it multiple times.
+ Find the number of times needed to decrypt.
+ The correct number is 30.
+ Decrypt 30 times to get the flag.

	Python Script to  Determine the Number Of Times to Decrypt

	import base64
	import codecs 

	l = open('flag.txt','r')
	temp = l.read()
	for j in range(100):
	    try:
	        temp = base64.b64decode(temp)
	    except:
	        print(j)
	        break
