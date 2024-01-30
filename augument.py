# without app


import albumentations as A
from PIL import Image
import numpy as np
import os

pillow_image = Image.open("image\lion.png")
image = np.array(pillow_image)


choice =input("choose ur choice 1)All 2)spcific operation:")

def output():
    transformed_image_1 = transform(image=image)['image']
    result_img = Image.fromarray(transformed_image_1)
    des=r"D:\FresherTraian_ing\backend training\Augumentation\result\output"
    file_path=os.path.join(des +"_"+ name +".png")
    result_img.save(file_path)
if choice == "1":
    for req in range(1,11):
        if req == 1:
            name="HorizontalFlip"
            transform = A.Compose([
            A.HorizontalFlip(always_apply=True)
            ])
            output()
            continue
        elif req == 2:   
            name="VerticalFlip" 
            transform = A.Compose([
            A.VerticalFlip(always_apply=True)
            ])
            output()
            
        elif req == 3:
            name="rotate90"
            transform = A.Compose([
            A.RandomRotate90(always_apply=True,p=1.0)    
            ])
            output()
            
        elif req == 4:
            name="rotate"
            transform = A.Compose([
            A.Rotate(limit=180, p=1.0),    
            ])
            output()
            
        elif req == 5:
            name="crop"
            transform=A.Compose([
            A.RandomCrop(width=500, height=500)
            ])
            output()
            
        elif req == 6:
            name="shear"
            transform = A.Compose([
            A.ElasticTransform(alpha=100,sigma=10,alpha_affine=100,p=1.0)
            ])   
            output()
            
        elif req == 7:
            name="Blur"
            transform=A.Compose([
                A.Blur(blur_limit=20,always_apply=True,p=1.0)
            ])
            output()
            
        elif req == 8:
            name="Exposure"
            transform=A.Compose([
            A.CLAHE(always_apply=False, p=1.0, clip_limit=(1, 4), tile_grid_size=(8, 8))
            ])
            output()
            
        elif req == 9:
            name="noise"
            transform = A.Compose([
            A.MultiplicativeNoise(multiplier=(0.5, 1.5), p=0.5)
            ])
            output()
            
        elif req == 10:
            name="cutout"
            transform=A.Compose([
                A.Cutout(num_holes=5,max_h_size=50,max_w_size=50,p=1.0)
            ])
            output()
        
        else:
            print("choose correct number")
            break
elif choice == "2":
    print("1.HorizontalFlip\
       2.VerticalFlip\
       3.90 degree rotation\
       4.Random rotation\
       5.Random crop\
       6.Random shear\
       7.Blur\
       8.Exposure\
       9.Random noise\
       10.cutout"
      )
    input_string = input('Enter elements of a list separated by space \n')
    need = input_string.split()
    for req in need:
        while(True):
            if req == "1":
                name="HorizontalFlip"
                transform = A.Compose([
                A.HorizontalFlip(always_apply=True)
                ])
                output()
                break
            elif req == "2":   
                name="VerticalFlip" 
                transform = A.Compose([
                A.VerticalFlip(always_apply=True)
                ])
                output()
                break
            elif req == "3":
                name="rotate90"
                transform = A.Compose([
                A.RandomRotate90(always_apply=True,p=1.0)    
                ])
                output()
                break
            elif req == "4":
                name="rotate"
                transform = A.Compose([
                A.Rotate(limit=180, p=1.0),    
                ])
                output()
                break
            elif req == "5":
                name="crop"
                transform=A.Compose([
                A.RandomCrop(width=500, height=500)
                ])
                output()
                break
            elif req == "6":
                name="shear"
                transform = A.Compose([
                A.ElasticTransform(alpha=100,sigma=10,alpha_affine=100,p=1.0)
                ])   
                output()
                break
            elif req =="7":
                name="Blur"
                transform=A.Compose([
                    A.Blur(blur_limit=20,always_apply=True,p=1.0)
                ])
                output()
                break
            elif req == "8":
                name="Exposure"
                transform=A.Compose([
                A.CLAHE(always_apply=False, p=1.0, clip_limit=(1, 4), tile_grid_size=(8, 8))
                ])
                output()
                break
            elif req == "9":
                name="noise"
                transform = A.Compose([
                A.MultiplicativeNoise(multiplier=(0.5, 1.5), p=0.5)
                ])
                output()
                break
            elif req == "10":
                name="cutout"
                transform=A.Compose([
                    A.Cutout(num_holes=5,max_h_size=50,max_w_size=50,p=1.0)
                ])
                output()
                break
            else:
                print("choose correct number")
                break


    
