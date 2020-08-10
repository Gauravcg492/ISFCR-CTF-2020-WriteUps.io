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
+ Final image:
<img src = "./res_chk.JPG" alt = "" />
