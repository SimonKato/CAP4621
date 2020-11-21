import os
import shutil
import sys
import cv2
import numpy as np
import argparse
import pandas as pd
#get arguments
args = sys.argv
if len(args) != 3:
    raise Exception("Structure: python decouple.py maskedPath unmaskedPath")

masked = args[1]
unmasked = args[2]
counter = 0
#print(masked)
#print(unmasked)

# for root, subDir, files in os.walk(masked):
#     if files:
#         for file in files:
#             shutil.copyfile(root + '/' + file, "/content/pytorch-CycleGAN-and-pix2pix/datasets/cap_dataset/masked/" + str(counter) + file)
#             counter += 1
#     else:
#         continue

# counter = 0
# for root, subDir, files in os.walk(unmasked):
#     if files:
#         for file in files:
#             shutil.copyfile(root + '/' + file, "/content/pytorch-CycleGAN-and-pix2pix/datasets/cap_dataset/unmasked/" + str(counter) + file)
#             counter += 1
#     else:
#         continue

# is there a face that is of reasonable size in the photo?
# could modify to crop image to enlargen faces

# this uses cv2 Cacade Classifier. Does not do too well.
def isFace(file):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(file)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.03,3)
    # if len(faces) > 1:
    #     return False
    #get shape of image
    (x1,y1,depth) = img.shape
    print(img.shape)
    print(faces)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()
    # for (x,y,w,h) in faces:
    #     if ((x1*y1)*0.7 > (x*y)):
    #         return False
    # return True

def isFaceAdvanced(file):
    #preload the model
    net = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt','res10_300x300_ssd_iter_140000.caffemodel')

    #read in data, get statistics
    img = cv2.imread(file)
    (h,w) = img.shape[:2]
    print("size of original: ",h," ",w)
    blob = cv2.dnn.blobFromImage(cv2.resize(img , (300, 300)),
                                1.0,
                                (300,300),
                                (104.0,177.0,123.0))
    net.setInput(blob)
    detections = net.forward()

    faces = []
    for i in range(0,detections.shape[2]):
        confidence = detections[0,0,i,2]
        
        if confidence > 0.9:
            print(confidence)
            box = detections[0,0,i, 3:7]*np.array([w,h,w,h])
            
            box = box.astype("int")
            print(box)
            faces.append(box)
            # newimg = img[startY:endY, startX:endX]
            # #resize the new image
            # r = 256 / newimg.shape[1]
            # dim = (256, int(newimg.shape[0]* r))
            # resized = cv2.resize(newimg,dim,interpolation=cv2.INTER_AREA)
            # newimages.append(resized)
    # if len(faces) != 1:
    #     return False
    # if ((h*w) * 0.7)
    cv2.imshow("output",img)
    cv2.waitKey(0)


if __name__=="__main__":
    isFaceAdvanced("0001.jpg")