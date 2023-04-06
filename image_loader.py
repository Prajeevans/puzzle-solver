import tkinter as tk
from PIL import ImageTk, Image
import os
import random

class ImageInfo:
    def __init__(self, path):
        self.path = path
        self.image = ImageTk.PhotoImage(Image.open(path))

image_array = []

folder_path = "./assets/angles"
file_list = os.listdir(folder_path)
for file in file_list:
    if file.endswith(".jpg") or file.endswith(".png"):
        image_path = os.path.join(folder_path, file)
        info = ImageInfo(image_path)
        image_array.append(info)

# angle_loader()