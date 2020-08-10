Challenge 1
-----------

Something is wrong with this system. Can you log in and find the flag?  
Points: 50

Solution
--------

Fix PATH ENV.

```

export PATH="$PATH:/bin/"

OR

/bin/ls -al
/bin/cat .flag

```

Flag: `CTF{1_kn0w_d4_w3y}`

---

Challenge 2
-----------

Sheldon Cooper is a VERY organised and punctual person. He's hidden a secret message in this system. Can you find it?

Place the flag in the format CTF{}

Points: 100

Solution
--------

Flag in crontab. All other flags which read `CTF{B4z1nG4!}` were fake!

`cat /etc/crontab`

Flag: `CTF{50fT_K1ttY_W4rM_k1ttY}`

---

Challenge 3
-----------

Robby Russell was messing around with this system and dropped a flag somewhere. Can you help him find it?

Place the flag in the format CTF{}

Points: 100

Solution
--------

Flag in `~/.zshrc`.

Flag: `CTF{1_pr3f3r_4gn05t3r}`

---

Challenge 4
-----------

There's a flag in root. All you have to do is read it.

Points: 150

Solution
--------

Login with different shell through ssh

`ssh hacker@172.17.0.1 -p 5000 -t "bash --noprofile"`

Flag: `CTF{L3t5_5w1tcH_5h3ll5}`

---

Challenge 5
-----------

Han Solo tried using a Linux system once. But Jabba captured Han and by the time he was freed, Chewie messed up the computer and locked Han out!

Han had a secret file which contains the flag you're looking for. Can you find it?

Points: 400

Solution
--------

Flag in `/home/han/.flag`

Password can be cracked using John the ripper. Accessible shadow file is placed in `/opt/`

To login as han, use a custom shell (Any shell apart from default). `/home/han/.bashrc` is broken and exits on source.

Password once cracked from John `!@#$%^&*`

```
su han --shell /bin/sh
cat /home/han/.flag

```

Flag: `CTF{!@#$%^&*_h4n_5h0t_F1r5T!!!!}`
