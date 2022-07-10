import os
import numpy as np
import cv2
import pandas as pd

col=[]
for i in range(784):
    col.append(i)
col2=['0']
for i in range(1,784):
    col2.append('0.'+str(i))

mp=[-1,'checkmark','cloud','croissant','heart','laugh','smile','sun']

for i in range(1,len(mp)):
      path='/home/sandeepan/Mosaic/ps1/content/augmented/'+mp[i]
      os.chdir(path)
      df=pd.DataFrame()
      data=[]
      for file in os.listdir(path):
         img=cv2.imread(file)
         img=cv2.resize(img,(28,28),interpolation = cv2.INTER_AREA)
         gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
         flat=gray_img.flatten()
         ser=pd.Series(flat)
         data.append(ser)
      
      df=pd.DataFrame(data,columns=col)
      df.columns=col2
      df.insert(loc=0,column='Target',value=i)
      print(df)
      df.reset_index()
      os.chdir('/home/sandeepan/Mosaic/ps1')
      if not os.path.isfile('finalemojis.csv'):
         df.to_csv('finalemojis.csv',index=False)
      else:
          df.to_csv('finalemojis.csv',mode='a',header=False,index=False)
    #   print(df.keys())