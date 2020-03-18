from pyzbar import pyzbar
import argparse
import cv2
import os
import re
import glob

# ap = argparse.ArgumentParser()
# ap.add_argument("-i","--image",required=True,help="Path to input image")
# args=vars(ap.parse_args())
# image=cv2.imread(args["image"])

path='barcodes/'
files=[]
for filename in glob.glob(os.path.join(path, '*.jpg')):  
    files.append(filename)
# print(files)

barCodes=[]
splStr='\\'
for f in files:
    res=f.partition(splStr)[2]
    # print(res)
    barCodes.append(res)
print(barCodes)

for barCode in barCodes:

    a=str('barcodes/'+barCode)

    image=cv2.imread(a)

    bars=pyzbar.decode(image)

    for bar in bars:
        (x,y,w,h)=bar.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        barcodeData=bar.data.decode("utf-8")
        barcodeType=bar.type

        text="{}({})".format(barcodeData,barcodeType)
        print(text)
        cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    
    # cv2.imshow("Image",image)
    cv2.waitKey(2000)



# path='bar1.jpg'
# image=cv2.imread(path)

# barcodes=pyzbar.decode(image)

# for barcode in barcodes:
#     (x,y,w,h)=barcode.rect
#     cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
#     barcodeData=barcode.data.decode("utf-8")
#     barcodeType=barcode.type

#     text="{}({})".format(barcodeData,barcodeType)
#     print(text)
#     cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    
# cv2.imshow("Image",image)
# cv2.waitKey(0)