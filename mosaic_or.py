import datetime
from flask import Blueprint,request,abort
import numpy as np
from PIL import Image
import random,os
from models import db, Document


MOSAIC=Blueprint("mosaic",__name__)

@MOSAIC.route("/mosaic",methods=["post"])
def mosaic_operation():
    list_img=request.files.getlist('file')
    name=request.form['name']
    return_msg={"msg":"augmentation completed"}
    if len(list_img ) >= 4:
        ran=random.sample(list_img,4)
        # width, height = 480, 650
        width=random.randint(100,480)
        height=650
        mosaic = np.zeros((2 * height, 2 * width, 3), dtype=np.uint8)
        for i,image1 in enumerate(ran):
            
            image1=Image.open(image1)
            image1 = image1.resize((width, height))
            image1 = np.array(image1)
            if i==0:
                mosaic[0:height, 0:width] = image1
                
            if i==1:
                mosaic[0:height, width:] = image1
            
            if i==2:
                mosaic[height:, 0:width] = image1
                
            if i==3:
                mosaic[height:, width:] = image1
            
        mosaic_image = Image.fromarray(mosaic)
        des=r"D:\FresherTrain_ing\backend training\Augumentation\result\output"
        
        file_path=os.path.join(des,name +"_" +"mosaic" +".png")
        mosaic_image.save(file_path)
        need=["mosaic"]
        image = Document(filename=name,operation=need,request_time=datetime)
        db.session.add(image)
        db.session.commit() 

        return return_msg
    else:
        abort(400)