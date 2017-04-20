# Crop face
# Nguyen Phat Tai
# nptai95@gmail.com

import cv2 as cv
import os
import glob
import config

INPUT = config.RAW_DIR
OUTPUT = config.FACE_DIR

if not os.path.exists(OUTPUT):
    os.mkdir(OUTPUT)

paths = glob.glob('{0}/*/*.jpg'.format(INPUT))
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
paths.sort()

for ifile in paths:
    img = cv.imread(ifile)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    iface = 0
    aface = 0
    for i, (x,y,w,h) in enumerate(faces):
        a = w*h
        if aface < a:
            iface, aface = i, a

    if aface != 0:
        (x, y, w, h) = faces[iface]
        face = img[y:y+h, x:x+w]
        ofile = ifile.replace(INPUT, OUTPUT)
        odir = os.path.dirname(ofile)
        
        if not os.path.exists(odir):
            os.mkdir(odir)

        cv.imwrite(ofile, face)

        print ofile




