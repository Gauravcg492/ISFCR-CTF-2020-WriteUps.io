from PIL import Image
import cv2
import math
import numpy

def press(image_filename, new_height):
    orig_img=cv2.imread(image_filename)
    final_img=numpy.zeros((new_height, math.ceil(orig_img.shape[0]*orig_img.shape[1]/new_height),3))

    for i in range(orig_img.shape[0]):
        for j in range(orig_img.shape[1]):
            index=i*orig_img.shape[1]+j
            final_img[index//final_img.shape[1]][index%final_img.shape[1]]=orig_img[i][j][::-1]
    
    final=Image.fromarray(final_img.astype(numpy.uint8), mode="RGB")
    if(image_filename.count(".")<2):
        final.save(image_filename.split(".")[0]+"_as_"+str(new_height)+"x"+str(final_img.shape[1])+".png")
    else:
        final.save(image_filename.split(".")[-2]+"_as_"+str(new_height)+"x"+str(final_img.shape[1])+".png")

press(input("Enter image name/path with extension: "), int(input("Enter new height: ")))