from PIL import Image
import os
print("Resize images in the folder")
folder = input("folder: ")
w = int(input("width: "))
h = int(input("height: "))
for i in os.listdir(folder):
    print(i)
    file = f"{folder}\\{i}"
    im = Image.open(file)
    im = im.resize((w, h), Image.ANTIALIAS)
    im.save(file)
