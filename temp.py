from PIL import Image
import os
import re
import glob as blob

def main(): 
    try: 
        path="images/"
        slNo=[1,2,3,4,5]
        items=["Apple","Banana","Candy","Drumstick","Eggplant"]
        price=[10,2,1,5,4]
        path = 'images'
        files=[]
        for filename in blob.glob(os.path.join(path, '*.png')):  
            files.append(filename)
        totalPrice=0
        for x in files:
            array = re.findall(r'[0-9]+', x)
            a=int(array[0])
            print("Item is : ",items[a-1]," Price : ",price[a-1])
            totalPrice=totalPrice+price[a-1]
            print("Total Amount : ",totalPrice)
        print("GRAND TOTAL : ",totalPrice)
            
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main()