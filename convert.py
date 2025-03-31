import os
from PIL import Image

folder = "images"

for filename in os.listdir(folder):
    if filename.endswith(".jfif"):
        path = os.path.join(folder, filename)
        img = Image.open(path)
        new_name = filename.replace(".jfif", ".jpg")
        img.save(os.path.join(folder, new_name), "JPEG")
        os.remove(path)
