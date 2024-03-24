import os
import cv2
import time
import uuid

IMAGE_PATH = 'CollectedImages'

labels = ['Hello', 'Yes', 'No','Thanks', 'I Miss You','I Love You', 'Please']

no_of_images = 5

for label in labels:
    img_path = os.path.join(IMAGE_PATH,label)
    os.makedirs(img_path)


    #open camera to record
    print(f"Collecting Images for  {label}")
    cap =  cv2.VideoCapture(0)
    time.sleep(5)


    for imgnum in range(no_of_images):
        ret, frame = cap.read()
        Img_name=os.path.join(IMAGE_PATH, label, label+"."+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(Img_name,frame)
        cv2.imshow('frame', frame)
        time.sleep(3) 

        if cv2.waitKey(2) & 0xFF==ord('q'):
            break

    cap.release()
