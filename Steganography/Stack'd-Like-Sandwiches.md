Take the two least significant bits out of every pixel, and normalise them to a new image.

Example code to extract image:
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
