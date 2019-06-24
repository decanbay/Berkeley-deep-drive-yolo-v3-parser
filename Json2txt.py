#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 21:19:30 2019

@author: deniz
"""

import matplotlib.patches as patches
import json
import os
import cv2
import math
#os.chdir("C:/BBD100K")
#os.chdir("/media/deniz/02B89600B895F301/BBD100K")
cwd=os.getcwd()

train_path = cwd+"/bdd100k_labels_images_train.json"
val_path = cwd+"/bdd100k_labels_images_val.json"

with open(train_path,"r") as ftr:
    trlabel = json.load(ftr)
    
with open(val_path,"r") as fval:
    valabel = json.load(fval)
        

BBDlabeldict = {"bike":5,
             "bus":2,
             "car":0,
             "motor":3,
             "person":1,
             "rider":1,
             "traffic light":[],
             "traffic sign":[],
             "train":[],
             "truck":4,
             "drivable area":[],
             "lane":[]}

#BDDdir = "S:/PyTorch-YOLOv3/data/BDD"   #windows
labels_dir = cwd+"/BDD_labels_6classes"

os.chdir(labels_dir)
os.mkdir("train")
os.mkdir("val")
os.chdir(labels_dir)

for ind1 in range(len(trlabel)):
    imname = trlabel[ind1]["name"]
    txtfile = open(labels_dir+"/train/"+imname.split(".")[0]+".txt","a")
    for ind2 in range(len(trlabel[ind1]["labels"])):
        lbl = BBDlabeldict[trlabel[ind1]["labels"][ind2]["category"]]   #traffic sign
        if lbl != []:
            a=trlabel[ind1]["labels"][ind2]["box2d"]   #traffic sign
            x1,y1,x2,y2 = list(a.values())
            resx = 1280 #im.shape[1] #1280
            resy = 720# im.shape[0] #720
            cx = (x1+x2)/(2*resx)
            cy = (y1+y2)/(2*resy)
            width = abs(x1-x2) /resx
            height = abs(y1-y2) /resy
            txtfile.write("{} {:.6f} {:.6f} {:.6f} {:.6f}\n".format(lbl,cx,cy,width,height))
    txtfile.close()
    
    
for ind1 in range(len(valabel)):
    imname = valabel[ind1]["name"]
    txtfile = open(labels_dir+"/val/"+imname.split(".")[0]+".txt","a")
    for ind2 in range(len(valabel[ind1]["labels"])):
        lbl = BBDlabeldict[valabel[ind1]["labels"][ind2]["category"]]   #traffic sign
        if lbl != []:
            a=valabel[ind1]["labels"][ind2]["box2d"]   #traffic sign
            x1,y1,x2,y2 = list(a.values())
            resx = 1280 #im.shape[1] #1280
            resy = 720# im.shape[0] #720
            cx = (x1+x2)/(2*resx)
            cy = (y1+y2)/(2*resy)
            width = abs(x1-x2) /resx
            height = abs(y1-y2) /resy
            txtfile.write("{} {:.6f} {:.6f} {:.6f} {:.6f}\n".format(lbl,cx,cy,width,height))
    txtfile.close()

########################################################
    
os.chdir(labels_dir)

txtfile = open("train_BDD.txt","a")
for ind1 in range(len(trlabel)):
    imname = trlabel[ind1]["name"]
    txtfile.write("/data/obj/"+imname+'\n')
txtfile.close()
 
txtfileval = open("train_BDD.txt","a")    
for ind1 in range(len(valabel)):
    imname = valabel[ind1]["name"]
    txtfileval.write("/data/obj/"+imname+'\n')
txtfileval.close()


