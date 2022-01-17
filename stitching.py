import numpy as np
import cv2

# Import a cat image
cat_img = cv2.imread('cat.jpeg')

# Devide a cat image into two parts
w, h, _ = cat_img.shape
left = cat_img[:,:200,:]
right = cat_img[:100,100:,:]

# Store them
cv2.imwrite('left.jpeg', left)
cv2.imwrite('right.jpeg', right)

# Open windows to show them
cv2.imshow('left',left)
cv2.imshow('right',right)

# Stitching
imgs = []
imgs.append(left)
imgs.append(right)

stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
status, pano = stitcher.stitch(imgs)

if status == cv2.Stitcher_OK:
    cv2.imshow('left',left)
    cv2.imshow('right',right)
    cv2.imshow('pano', pano)
    cv2.waitKey()

else:
    print("can not stich!")




