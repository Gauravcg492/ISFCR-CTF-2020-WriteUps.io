# Steganography Challenges

## Website down for maintenance.

<!---
## Text Challenges
#### There, there
Count the number of unprintable characters between normal ones, and decode them to ASCII characters.

Example code to extract flag: 
```python
def decode(filename):
    f_in=open(filename, "r", encoding="utf-8")
    f_out=open("_decoded.".join(filename.split(sep=".")), mode="w")

    i=1
    s_in="".join(f_in.readlines())
    l=[0]
    while i<len(s_in):
        if s_in[i]!=zero_width_space:
            if l[-1]==i-1:
                break
            l+=[i]
        i+=1
    print("".join([chr(l[i]-l[i-1]-1) for i in range(1,len(l))]), file=f_out)
    
    f_in.close()
    f_out.close()
```
## Audio Challenges
#### Ta1nted L0ve
Convert the wav file to a bit-array and extract the least significant bit of every byte. Decode the byte sequence to ASCII characters.

Example code:
```python
def decode(filename):
    song = wave.open(filename, mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    decoded = string.split("###")[0]
    print("Sucessfully decoded: "+decoded)
    song.close()

    return decoded
```
#### The Closer You Look
View the spectrograph of the audio file, flag will appear between the timestamps 0:35 - 0:45, 1:32 - 1:42, 2:30 - 2:40, 3:40 - 3:51, 4:40 - 4:50, and 6:06 - 6:18
#### What's the bass-word
Listen for the bass tones in the background and translate to Morse Code. Longer tones are dashes and shorter ones are dots.
## Image Challenges
#### Sprinkled Bits of Wax
Extract the least significant bit from each pixel and convert it to a string of ASCII characters.

Example code:
```python
def decode(image_filename):
    message=""
    curr=[0 for i in range(16)]
    img=image_prepared(image_filename)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                curr[(i*img.shape[1]+j*img.shape[2]+k)%16]=img[i][j][k]&1
                if (i*img.shape[1]+j*img.shape[2]+k)%16==15:
                        if(sum(curr)==0):
                            return message
                        message=message+chr(int("".join(map(str, curr)), base=2))
```
#### Stack'd like Sandwiches
Extract the two least significant bits from each pixel, normalise it in a new array and form a new image.
```python
def unblend_images(filename_pack, number_of_bits):
    img=cv2.imread(filename_pack)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if(img[i][j][k]%(2**(number_of_bits))):
                    img[i][j][k]=(img[i][j][k]<<(8-number_of_bits))%255
                else:
                    img[i][j][k]=0
    frame=Image.fromarray(img)
    frame.show()
```
--->