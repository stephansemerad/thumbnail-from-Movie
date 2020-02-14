#!/usr/bin/python3
import os
import time
import datetime
import getpass
import cv2
from PIL import Image

ext = ['.mov', '.mp4']

path = r'C:\Users\ssemerad\Videos\4K Video Downloader'
file_path = path + r'\1.mp4'

file_id = 'IURHIR'
thumbnail ='thumbnail_'+file_id+'.jpeg'
new_file_path = path + '\\' + thumbnail


cap = cv2.VideoCapture(file_path)
video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
ret, frame = cap.read()
cv2.imwrite(new_file_path, frame)
cap.release()
img = Image.open(new_file_path) # image extension *.png,*.jpg
img = img.resize((192, 108), Image.ANTIALIAS)
img.save(new_file_path)
print('thumbnail: ', thumbnail)
