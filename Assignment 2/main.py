import cv2
import numpy as np

class Image:    
    def __init__(self,path):
        self.image=cv2.imread(path,0)
        self.E=4
        self.k0=0.4
        self.k1=0.02
        self.k2=0.4


    def show_image(self):
        cv2.imshow('Before modification',self.image)
        cv2.waitKey(0)
        # print(np.array(self.image))


    def G_avg_intensity(self):
        self.tot=0
        for i in range (self.image.shape[0]):
            for j in range (self.image.shape[1]):
                self.tot+=self.image[i][j]
        self.global_mean=self.tot/(self.image.shape[0]*self.image.shape[1])
        # print('Avg instesity for global img', self.global_mean)


    def G_standard_dev(self):
        self.std=0
        self.global_std=0
        for i in range (self.image.shape[0]):
            for j in range (self.image.shape[1]):
                self.std+=(self.image[i][j]-self.global_mean)**2
        self.global_std=(self.std/(self.image.shape[0]*self.image.shape[1]))**0.5
        # print('standard dev for global img', self.global_std)


    def padding(self):
        self.imgarr=np.array(self.image)
        self.imgarr=np.insert(self.imgarr,0,np.zeros(self.imgarr.shape[1]),axis=0)
        self.imgarr=np.insert(self.imgarr,0,np.zeros(self.imgarr.shape[0]),axis=1)
        self.imgarr=np.append(self.imgarr,[np.zeros(self.imgarr.shape[1])],axis=0)
        self.imgarr=np.append(self.imgarr,np.zeros((self.imgarr.shape[0],1)),axis=1)
        self.imgarr=self.imgarr.astype(np.uint8)
        # cv2.imshow('01',self.imgarr)
        # cv2.waitKey(0)


    def local_mean(self):
        self.localmean_array=[]
        tot_list=[]
        for i in range (1,self.imgarr.shape[0]-1):
            for j in range (1,self.imgarr.shape[1]-1):
                Ltot=0
                for s in range(3):
                    for t in range (3):
                        Ltot+=self.imgarr[i+s-1][j+t-1]
                tot_list.append(Ltot)
        for i in range (len(tot_list)):
            self.localmean_array.append(tot_list[i]/9)
        # print('local mean ',np.array(self.localmean_array))


    def local_std(self):
        self.local_stdarry = []
        std_list = []
        h = 0
        for i in range(1, self.imgarr.shape[0]-1):
            for j in range(1, self.imgarr.shape[1]-1):
                std = 0
                for s in range(3):
                    for t in range(3):
                        if h < len(std_list):
                            h += 1
                        std += ((self.imgarr[i+s-1][j+t-1]-self.localmean_array[h])**2)
                std_list.append(std)
        for i in range(len(std_list)):
            self.local_stdarry.append((std_list[i]/9)**0.5)
        # print('local std ',np.array(self.local_stdarry))

    def check_condition(self):
        h=0
        ct=0
        # print(self.image)
        for i in range (self.image.shape[0]):
            for j in range (self.image.shape[1]):
                if (self.localmean_array[h]<=(self.k0*self.global_mean)) and ((self.k1*self.global_std)<=self.local_stdarry[h]<=(self.k2*self.global_std)):
                    self.image[i][j]=self.E*self.image[i][j]
                    ct+=1
                if h < len(self.localmean_array):
                    h+=1
        cv2.imshow('After modification',self.image)
        cv2.waitKey(0)
        # print(self.image)
        # print('count ', ct)


img=Image("D:\desktop\Sixth Semester\Image Processing\Assignments\Assignment 2/01.jpg")
img.show_image()
img.G_avg_intensity()
img.G_standard_dev()
img.padding()
img.local_mean()
img.local_std()
img.check_condition()

