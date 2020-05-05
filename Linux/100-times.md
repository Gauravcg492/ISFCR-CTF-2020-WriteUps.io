# Challenge:
 + There is a secret key (S) stored in a file '-'.
 + There are 2 executables c1, c2
 + To unlock the flag, you have to do the following:
	+ Execute c1, which takes S as input.
	+ Run this 100 times
		+ Feed the output of c1 as input to c2
		+ Feed the output of c2 as input to c1

# Solution:
 + 	#!/bin/sh 
   	LIMIT=100
	INP2=$(python p1.py<./-)
	echo "$INP2" > "inp2"
	while [ "$LIMIT" -ne 0 ]
	do
		INP1=$(python p2.py <inp2)
		echo "$INP1" > "inp1"
		((LIMIT=LIMIT-1))
		echo $LIMIT
		INP2=$(python p1.py <inp1)
		echo "$INP2" > "inp2"
	done
# Note: 
 + Initially only binary executables were supposed to be handed out, not python scripts
 + However, due to incompatibility with various architectures and lack of cloud servers to host Linux challenges, we ended up giving the original python scripts. 
 + Hence for this particular case, a python script could've also been written to get the desired output. 
 + It is highly advised that you learn shell scripting to tackle such problems in the future.