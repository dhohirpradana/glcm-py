import numpy as np
import cv2
# import os
# import re
from skimage import io

# -------------------- Utility function ------------------------
# def normalize_label(str_):
#     str_ = str_.replace(" ", "")
#     str_ = str_.translate(str_.maketrans("","", "()"))
#     str_ = str_.split("_")
#     return ''.join(str_[:2])

# def normalize_desc(folder, sub_folder):
#     text = folder + " - " + sub_folder
#     text = re.sub(r'\d+', '', text)
#     text = text.replace(".", "")
#     text = text.strip()
#     return text

# def print_progress(val, val_len, folder, sub_folder, filename, bar_size=10):
#     progr = "#"*round((val)*bar_size/val_len) + " "*round((val_len - (val))*bar_size/val_len)
#     if val == 0:
#         print("", end = "\n")
#     else:
#         print("[%s] folder : %s/%s/ ----> file : %s" % (progr, folder, sub_folder, filename), end="\r")


# # -------------------- Load Dataset ------------------------

# dataset_dir = "DATASET/"

imgs = []  # list image matrix
# labels = []
# descs = []
# for folder in os.listdir(dataset_dir):
#     for sub_folder in os.listdir(os.path.join(dataset_dir, folder)):
#         sub_folder_files = os.listdir(os.path.join(dataset_dir, folder, sub_folder))
#         len_sub_folder = len(sub_folder_files) - 1
#         for i, filename in enumerate(sub_folder_files):
# img = cv2.imread(os.path.join(dataset_dir, folder, sub_folder, filename))

img = io.imread(
    'https://images.unsplash.com/photo-1607690424560-35d967d6ad7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZWdnfGVufDB8fDB8fA%3D%3D&w=1000&q=80')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = gray.shape
ymin, ymax, xmin, xmax = h//3, h*2//3, w//3, w*2//3
crop = gray[ymin:ymax, xmin:xmax]

resize = cv2.resize(crop, (0, 0), fx=0.5, fy=0.5)

imgs.append(resize)
# labels.append(normalize_label(os.path.splitext(filename)[0]))
# descs.append(normalize_desc(folder, sub_folder))

# print_progress(i, len_sub_folder, folder, sub_folder, filename)

print(imgs[0])
