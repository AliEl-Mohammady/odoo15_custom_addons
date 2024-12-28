#This code to convert image to binary numbers


import os
import base64
import pyperclip

image_path=os.path.join(os.getcwd(),"IMG_0514.jpeg")

with open(image_path,"rb") as image_file:
    image_data=image_file.read()

base64_image=base64.b64encode(image_data)
base64_str=base64_image.decode("utf-8")

pyperclip.copy(base64_str)


