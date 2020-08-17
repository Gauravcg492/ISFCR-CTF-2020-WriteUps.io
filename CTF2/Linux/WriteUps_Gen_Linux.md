General Linux
=============

Challenge 1
-----------

Some fool lost the flag in the logs. Find it ASAP!

[logs](Files/logs)

Points: 50

Solution
--------

`cat logs | grep User:`

Flag: `CTF{1m_W4y_to0_l4zy_2_50lv3}`

---

Challenge 2
-----------

Leonardo is trying to tell you something. What is it?

[Leo's Message](Files/Leo's_message.tar.gz)

Points: 100

Solution
--------

nth character of each file where n is in the Fibonacci series

Flag: `CTF{D4_V1NC1}`

---

Challenge 3
-----------

The flag is in the given text file. Can you find it?

[File](Files/spaces)

Points: 100

Solution
--------

Count number of spaces and convert number to ASCII letter.

```python
with open("flag","r") as f:
    l = f.readlines()
    x = []
    for i in l:
        x.append(len(i) - 1)
    for i in x:
        print(chr(i))
```

Flag: `CTF{1_Se3_y0u}`

---

Challenge 4
-----------

The zip folder contains Bob's monthly bills. The flag is hidden in one of the bills, enclosed within the braces of CTF{}
[File](Files/bills.zip)

Points: 150

Solution
--------

Combine the usage of `find` and `grep` tools. `find` allows you to search for files within directories, `grep` allows you to search for texts within files. 
You should try checking within the bills of every month, but january itself has the flag. 
```
find . -name '*january*' -exec grep -H "CTF" {}
```

Flag: `CTF{m1!!!0nAir3}`

---

Challenge 5
-----------

The flag is hidden in this file. It is enclosed within ctf{}
[File](Files/HaveFun)

Points: 150

Solution
--------

Construct a regex starting with "ctf{" , containing anything in the middle and ending with "}"
```
grep -o "ctf{.*}" HaveFun 
```

Flag: `ctf{day."Asyouknow,NorthK@}`

---

Challenge 6
-----------

This binary was supposed to print the flag but it doesn't for some reason. Can you get the flag anyway?

[Binary](Files/main)

Points: 50

Solution
--------

Strings and grep

`strings main | grep CTF`

Flag: `CTF{R3ad1nG_B1n4Ry_15_345y}`
