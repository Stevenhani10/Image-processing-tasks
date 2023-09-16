import cv2
import numpy as np
from matplotlib import pyplot as plt
import tkinter
from tkinter import *
import PIL
from PIL import Image, ImageTk

root = Tk()
# from skimage.util import img_as_ubyte

image=cv2.imread(r"D:\desktop\Sixth Semester\Image Processing\Assignments\Assignment 1\Dollar.png",0)
# cv2.imshow('dollar',image)
cv2.waitKey(0)

binary= [[0 for i in range(image.shape[1])] for j in range(image.shape[0])]
for i in range(image.shape[0]):
  for j in range(image.shape[1]):
    binary[i][j]=format(image[i][j],'08b')

plane = [[[0 for i in range(image.shape[1])] for j in range(image.shape[0])] for k in range(8)]

for k in range (8):
  for i in range(len(plane[k])):
    for j in range(len(plane[k][i])):
      string = ''
      for s in range(8):
        if(s == k):
          string += binary[i][j][k]
        else:
          string += '0'

      plane[k][i][j] = string

# print(plane[2])

decplane= [[[0 for i in range(image.shape[1])] for j in range(image.shape[0])] for k in range(8)]
for k in range (8):
  for i in range(len(plane[k])):
    for j in range(len(plane[k][i])):
      decplane[k][i][j]=int(plane[k][i][j],2)
decplane=np.array(decplane)
decplane=decplane.astype(np.uint8)
# for k in range (8):
#   print(decplane[k])
im0=Image.fromarray(decplane[0])
im1=Image.fromarray(decplane[1])
im2=Image.fromarray(decplane[2])
im3=Image.fromarray(decplane[3])
im4=Image.fromarray(decplane[4])
im5=Image.fromarray(decplane[5])
im6=Image.fromarray(decplane[6])
im7=Image.fromarray(decplane[7])

# print(im)
# im.show()
root.state('zoomed')
root.configure(background='#7B8FA1')
im0=im0.resize((300,200))
im1=im1.resize((300,200))
im2=im2.resize((300,200))
im3=im3.resize((300,200))
im4=im4.resize((300,200))
im5=im5.resize((300,200))
im6=im6.resize((300,200))
im7=im7.resize((300,200))
img0 = ImageTk.PhotoImage(im0)
img1 = ImageTk.PhotoImage(im1)
img2 = ImageTk.PhotoImage(im2)
img3 = ImageTk.PhotoImage(im3)
img4 = ImageTk.PhotoImage(im4)
img5 = ImageTk.PhotoImage(im5)
img6 = ImageTk.PhotoImage(im6)
img7 = ImageTk.PhotoImage(im7)
flags=[]
for i in range(8):
  flags.append(False)
  
borders=[]
borders.append (LabelFrame(root, bd = 6, bg = "red")) 
borders[0].grid(padx = 10,pady = 5,row=0,column=0)
borders.append(LabelFrame(root, bd = 6, bg = "red"))
borders[1].grid(padx = 10,row=0,column=1,pady = 5)
borders.append(LabelFrame(root, bd = 6, bg = "red")) 
borders[2].grid(row=0,column=2,padx = 10,pady = 5)
borders.append(LabelFrame(root, bd = 6, bg = "red"))
borders[3].grid(row=0,column=3,padx = 10,pady = 5)
borders.append(LabelFrame(root, bd = 6, bg = "red"))
borders[4].grid(row=1,column=0,padx = 10,pady = 5)
borders.append(LabelFrame(root, bd = 6, bg = "red"))
borders[5].grid(row=1,column=1,padx = 10,pady = 5)
borders.append(LabelFrame(root, bd = 6, bg = "red"))
borders[6].grid(row=1,column=2,padx = 10,pady = 5)
borders.append(LabelFrame(root, bd = 6, bg = "red"))
borders[7].grid(row=1,column=3,padx = 10,pady = 5)
label0=Button(borders[0] ,image=img0, command= lambda t= "label0 Clicked": get_button(t,0))
label1=Button(borders[1] ,image=img1, command= lambda t= "label1 Clicked": get_button(t,1))
label2=Button(borders[2] ,image=img2, command= lambda t= "label2 Clicked": get_button(t,2))
label3=Button(borders[3] ,image=img3, command= lambda t= "label3 Clicked": get_button(t,3))
label4=Button(borders[4] ,image=img4, command= lambda t= "label4 Clicked": get_button(t,4))
label5=Button(borders[5] ,image=img5, command= lambda t= "label5 Clicked": get_button(t,5))
label6=Button(borders[6] ,image=img6, command= lambda t= "label6 Clicked": get_button(t,6))
label7=Button(borders[7] ,image=img7, command= lambda t= "label7 Clicked": get_button(t,7))
label0.image=img0
label1.image=img1
label2.image=img2
label3.image=img3
label4.image=img4
label5.image=img5
label6.image=img6
label7.image=img7
label0.grid(row=0,column=0)
label1.grid(row=0,column=1)
label2.grid(row=0,column=2)
label3.grid(row=0,column=3)
label4.grid(row=1,column=0)
label5.grid(row=1,column=1)
label6.grid(row=1,column=2)
label7.grid(row=1,column=3)
border = LabelFrame(root, bd = 6, bg = "black")
border.grid(pady = 10)
construct_btn= Button(border,bg="#54FA9B",activebackground="purple", text= "construct", command= lambda t= "construct Clicked": const_button(t))
construct_btn.config(height=10,width=20)
construct_btn.grid(row=3,column =0)

def get_button(t,index):
  if flags[index]==False:
    borders[index].config(bg="green")
    flags[index]=True
  else:
      borders[index].config(bg="red")
      flags[index]=False

reimage=[]
# rimg=[]
def const_button(t):
  for i in range(len(flags)):
    if flags[i]==True:
      reimage.append(np.copy(decplane[i]))
  if len(reimage)>0:
    rimg=np.copy(reimage[0])
    for k in range(1,len(reimage)):
      rimg+=np.copy(reimage[k])
    result=Image.fromarray(rimg)
    result=result.resize((300,200))
    fimg = ImageTk.PhotoImage(result)

    labelf=Label(image=fimg)
    labelf.image=fimg
    labelf.grid(padx=10,pady=20,row=2,column=1)
    reimage.clear()  



root.mainloop()