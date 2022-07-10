# Handwritten Emoji Captcha Recognition
   
## Steps to test the model:
- Mention the image path in cv2.imread() in [final.ipynb](https://github.com/san2130/Mosaic-22/blob/main/final.ipynb) and then run it.

## Steps to train the model:
- First generate the combined emoji csv file containing all the emoji images using [this](https://github.com/san2130/Mosaic-22/blob/main/emojis.py) to get the [allemojis.csv](https://github.com/san2130/Mosaic-22/blob/main/allemojis.csv) file.
- Run [Augmentation.ipynb](https://github.com/san2130/Mosaic-22/blob/main/Augmentation.ipynb) with input as allemojis.csv to get the augmented emoji csv [finalemojis.csv](https://github.com/san2130/Mosaic-22/blob/main/finalemojis.csv).
- Now run [ComboEmnist.ipynb](https://github.com/san2130/Mosaic-22/blob/main/ComboEmnist.ipynb) to train the model. Both the emnist dataset and the emoji dataset have been merged inside.  

## Special Features 
- This model can recognize captchas with letter rotation upto 30 deg.
- Able to detect captchas having letters of variable thickness and size.

## Character Set  
The character set which has been used to train the model consists of 19 English alphabets lower and uppercase mixed.  
**A,B,d,e,g,G,Z,W,H,I,J,R,t,K,M,S,N,X,b**

## Emoji Map:
Checkmark : 1  
Cloud: 2  
Croissant: 3  
Heart: 4  
Laugh: 5  
Smile: 6  
Sun: 7  

## Dataset
#### Emoji Dataset https://drive.google.com/drive/folders/1sw0XVroXFhJoNAJVj40qE7ZOPSBzve7u
#### Letter Dataset (Using EMNIST Balanced Dataset) https://drive.google.com/file/d/1zqHDRk942mVPFyaPndhr77mescbP8ODw/view?usp=sharing
