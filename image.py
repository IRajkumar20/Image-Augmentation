import datetime
from flask import Blueprint,request,abort
from models import db, Document
import albumentations as A
from PIL import Image
import numpy as np
import os

IMG_UPLOAD = Blueprint("img",__name__)

def output(name,transform,image,filename,need):
    transformed_image_1 = transform(image=image)['image']
    result_img = Image.fromarray(transformed_image_1)
    des=r"D:\FresherTrain_ing\backend training\Augumentation\result\output"
    fname=os.path.splitext(filename)[0]
    file_path=os.path.join(des,fname +"_"+ name +".png")
    result_img.save(file_path)
    


@IMG_UPLOAD.route("/upload",methods=["post"])
def upload_png():    
    allowed_exd=[".png",".jpeg",".jpg"]    
    file_name=request.files.getlist('file')
    choice=request.form['choice']
    return_msg= {"msg":"Augmentation completed"}
    
    for file in file_name:        
        extention=os.path.splitext(file.filename)[1]

        if extention in allowed_exd:

            pillow_image = Image.open(file)
            image = np.array(pillow_image)
            # # if choice in Document.query.filter_by(operation=file.filename).operation:
            # document=Document.query.filter_by(filename=file.filename).first()
            # print(document)
            # # for i in document:
            # #     print (i.operation)  
            check = Document.query.filter_by(filename=file.filename).first()
            if choice == "1":
                need=["All"]
                
                if not check:
                    for req in range(1,11):
                        if req == 1:
                            name="HorizontalFlip"
                            transform = A.Compose([
                            A.HorizontalFlip(always_apply=True)
                            ])
                            output(name,transform,image,file.filename,need)
                            continue
                        elif req == 2:   
                            name="VerticalFlip" 
                            transform = A.Compose([
                            A.VerticalFlip(always_apply=True)
                            ])
                            output(name,transform,image,file.filename,need)  
                            continue                  
                        elif req == 3:
                            name="rotate90"
                            transform = A.Compose([
                            A.RandomRotate90(always_apply=True,p=1.0)    
                            ])
                            output(name,transform,image,file.filename,need)   
                            continue                 
                        elif req == 4:
                            name="rotate"
                            transform = A.Compose([
                            A.Rotate(limit=180, p=1.0),    
                            ])
                            output(name,transform,image,file.filename,need)    
                            continue                
                        elif req == 5:
                            name="crop"
                            transform=A.Compose([
                            A.RandomCrop(width=250, height=125)
                            ])
                            output(name,transform,image,file.filename,need)  
                            continue                  
                        elif req == 6:
                            name="shear"
                            transform = A.Compose([
                            A.ElasticTransform(alpha=100,sigma=10,alpha_affine=100,p=1.0)
                            ])   
                            output(name,transform,image,file.filename,need)    
                            continue                
                        elif req == 7:
                            name="Blur"
                            transform=A.Compose([
                                A.Blur(blur_limit=20,always_apply=True,p=1.0)
                            ])
                            output(name,transform,image,file.filename,need)  
                            continue                  
                        elif req == 8:
                            name="Exposure"
                            transform=A.Compose([
                            A.CLAHE(always_apply=False, p=1.0, clip_limit=(1, 4), tile_grid_size=(8, 8))
                            ])
                            output(name,transform,image,file.filename,need)     
                            continue               
                        elif req == 9:
                            name="noise"
                            transform = A.Compose([
                            A.MultiplicativeNoise(multiplier=(0.5, 1.5), p=0.5)
                            ])
                            output(name,transform,image,file.filename,need) 
                            continue                   
                        elif req == 10:
                            name="cutout"
                            transform=A.Compose([
                                A.Cutout(num_holes=5,max_h_size=50,max_w_size=50,p=1.0)
                            ])
                            output(name,transform,image,file.filename,need)
                            continue
                        else:
                            print("choose correct number")
                            break

                    
                    image = Document(filename=file.filename,operation=need,request_time=datetime)
                    db.session.add(image)
                    db.session.commit()
                           
                else:
                    abort(409)
            elif choice == "2":
                # print("1.HorizontalFlip\
                # 2.VerticalFlip\
                # 3.90 degree rotation\
                # 4.Random rotation\
                # 5.Random crop\
                # 6.Random shear\
                # 7.Blur\
                # 8.Exposure\
                # 9.Random noise\
                # 10.cutout"
                # )
                input_string = request.form['input']
                need = input_string.split()
                return_msg={}
                if not check:
                    for req in need:
                        while(True):
                            if req == "1":
                                name="HorizontalFlip"
                                transform = A.Compose([
                                A.HorizontalFlip(always_apply=True)
                                ])
                                output(name,transform,image,file.filename,need)
                                break
                            elif req == "2":   
                                name="VerticalFlip" 
                                transform = A.Compose([
                                A.VerticalFlip(always_apply=True)
                                ])
                                output(name,transform,image,file.filename,need)
                                break
                            elif req == "3":
                                name="rotate90"
                                transform = A.Compose([
                                A.RandomRotate90(always_apply=True,p=1.0)    
                                ])
                                output(name,transform,image,file.filename,need)
                                break
                            elif req == "4":
                                name="rotate"
                                transform = A.Compose([
                                A.Rotate(limit=180, p=1.0),    
                                ])
                                output(name,transform,image,file.filename,need)
                                break
                            elif req == "5":
                                name="crop"
                                transform=A.Compose([
                                A.RandomCrop(width=100, height=100)
                                ])
                                output(name,transform,image,file.filename,need)
                                break
                            elif req == "6":
                                name="shear"
                                transform = A.Compose([
                                A.ElasticTransform(alpha=100,sigma=10,alpha_affine=100,p=1.0)
                                ])   
                                output(name,transform,image,file.filename,need)
                                break
                            elif req =="7":
                                name="Blur"
                                transform=A.Compose([
                                    A.Blur(blur_limit=20,always_apply=True,p=1.0)
                                ])
                                output(name,transform,image,file.filename,need)
                                break
                            elif req == "8":
                                name="Exposure"
                                transform=A.Compose([
                                A.CLAHE(always_apply=False, p=1.0, clip_limit=(1, 4), tile_grid_size=(8, 8))
                                ])
                                output(name,transform,image,file.filename,need)
                                break
                            elif req == "9":
                                name="noise"
                                transform = A.Compose([
                                A.MultiplicativeNoise(multiplier=(0.5, 1.5), p=0.5)
                                ])
                                output(name,transform,image,file.filename,need)
                                break
                            elif req == "10":
                                name="cutout"
                                transform=A.Compose([
                                    A.Cutout(num_holes=5,max_h_size=50,max_w_size=50,p=1.0)
                                ])
                                output(name,transform,image,file.filename,need)
                                break
                            else:
                                return_msg= {"msg":"choose correct number"}
                    image = Document(filename=file.filename,operation=need,request_time=datetime)
                    db.session.add(image)
                    db.session.commit()  

                    return_msg= {"msg":"albumentation completed"}
                else:
                    abort(409)
    return return_msg            
             

            
        
