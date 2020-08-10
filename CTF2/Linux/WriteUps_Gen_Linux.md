General Linux
=============

Challenge 1
-----------

Some fool lost the flag in the logs. Find it ASAP!

[logs][Files/logs]

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
