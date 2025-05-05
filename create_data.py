from itertools import count

import cv2, os
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'
sub_data = 'Hanis'

path = os.path.join(datasets, sub_data) #inside the dataset folder
if not os.path.isdir(path):
    os.mkdir(path)
    (width, height) = (130, 100)


    face_cascade = cv2.CascadeClassifier(haar_file)

    webcam = cv2.VideoCapture(0)

    count = 1
    while count < 51:
        print(count)
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
