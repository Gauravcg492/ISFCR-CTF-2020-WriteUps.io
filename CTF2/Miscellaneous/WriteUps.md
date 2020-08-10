Miscellaneous
=============

Challenge 1
-----------

Find the flag from the given file.

[File](Files/linus.c)

Points: 50

Solution
--------

Format the code. Flag can be found in a series of printf statements.

Flag: `CTF{T0rV4lD5_<3_C}`

---

Challenge 2
-----------

Find the flag in the given git repo.

[Repo](Files/Go.tar.gz)

Points: 100

Solution
--------

Flag is in .git/configs

Flag: `CTF{G1t_G00d_n00B}`

---

Challenge 3
-----------

Find the flag in the given git repo.

[Repo](Files/Go2.tar.gz)

Points: 100

Solution
--------

Flag is in stashed insertion sort.

```
git checkout stash
cat insertion_Sort   
```

Flag: `CTF{I_5t1lL_s3e_c0mM1tTs}`

---

Challenge 4
-----------

Loot the flag!

[Store](Files/store.go)

Points: 200

Solution
--------

First buy the 100$ item. When quantity is asked, provide the value as `9223372036854000000`. This will cause an overflow in the int64 variable and give you enough money to buy the million dollar flag.

Flag: `CTF{1_Fe3l_l1k3_4_mur1c4n}`

---

Challenge 5
-----------

Dylan is trying to tell you something. What is it?!

[Message](Files/Flag.jpg)

Points: 50

Solution
--------

The flag is in the metadata, can be found by looking at image properties.

CTF{N0w_Y0u_S3e_M3!}

---

Challenge 6
-----------

Alyssa P Hacker sends secret messages to Ben Bitdiddle through vague binaries. Can you figure out what this one says?

[Binary](Files/main)

Points: 150

Solution
--------

```sh
#! /bin/bash
var=$(python -c "print('a '*142)")
./main $var
```

Execute with a total of 143 shell arguments. This can be brute forced by putting the above script in a loop and changing the number of times a is multiplied.

Flag: CTF{1_kN0w_th3_se3Cr3t_K3y}

---

Challenge 7
-----------

Take a step back. You're probably frustrated enough with life. Points: 100

[Perspective](Files/Perspective.tar.gz)

Solution
--------

cat files into shell variable and then echo

```sh
var1=$(cat BOO)
var2=$(cat OOO)
var3=$(cat GIE)

echo $var1
echo $var2
echo $var3
```

After the echo, zoom out on the terminal to see the artwork!

Flag: CTF{0bFu5c4t3d_A5cii_4RTWORK}

---

Challenge 8
-----------

Let's mess with your mind.  
Points: 150

[M!ND](Files/WHAT_IS_THIS_CRAP)

Solution
--------

Decrypt from Brainf*ck to text and run code in play.golang.org

Flag: CTF{Br41Nf*Ck_1s_R3alLy_W31rD}

---

## After a long time
```
There's something with this image... but which does not appear, just passes by..
```

+ binwalk on the file would show that it has 7z archive data with it.
+ Extracting it using 7z would give us two text files. One of them has a fake flag(FileA), while the other one has the actual flag(FileB)
+ Solution
```bash
binwalk img.jfif
7z e img.jfif
```
+ Note: Format had to be changed(enclosed within CTF{} and not flag{})
+ Flag:
```
CTF{alright_you_have_taken_too_much_time}
```
