from sklearn.metrics import classification_report
import numpy as np
import cv2 
import os

realtestY = np.array(["black","black","black","black","black",
                     "red","red","red","red","red",
                     "green","green","green","green","green",
                     "none","none","none","none","none"])


red_card = cv2.imread("images/cardred_close.png")
green_card = cv2.imread("images/cardgreen_close.png")
black_card = cv2.imread("images/cardblack_close.png")
background = cv2.imread("images/cardnone.png")

def evalaccuracy(f_names,predictedY):
    predictedY = np.array(predictedY)
    if (np.sum(realtestY!=predictedY)>0):
        print ("Wrong Predictions: (filename, labelled, predicted) ")
        print (np.dstack([filenames,realtestY,predictedY]).squeeze()[(realtestY!=predictedY)])
    # Calculate those predictions that match (correct), as a percentage of total predictions
    return "Correct :"+ str(np.sum(realtestY==predictedY)) + ". Wrong: "+str(np.sum(realtestY!=predictedY)) + ". Correctly Classified: " + str(np.sum(realtestY==predictedY)*100/len(predictedY))+"%"

def averagecolor(image):
    return np.mean(image, axis=(0, 1))
trainX2 = []
trainY2 = []
path = "images/"
for label in ('red','green','black','none'):
    print ("Loading training images for the label: "+label)
    for filename in os.listdir(path+label+"/"): 
        img = cv2.imread(path+label+"/"+filename)
        img_features = averagecolor(img)
        trainX2.append(img_features)
        trainY2.append(label)   

print(len(trainX2))
print(len(trainY2))


########### RE RUNNING AFTER MORE PICS
path = "images/test/"
filenames = []
predictedY = []
for filename in os.listdir(path):
    img = cv2.imread(path+filename)
    img_features = averagecolor(img)
    calculated_distances = []
    for card in (trainX2):
        calculated_distances.append(np.linalg.norm(img_features-card))
    prediction =  trainY2[np.argmin(calculated_distances)]
    
    print (filename + ": " + prediction)
    filenames.append(filename)
    predictedY.append(prediction)

# Evaluate Accuracy (the sklearn package provides a useful report)
print ()
print(classification_report(realtestY, predictedY))

# Evaluate Accuracy
print (evalaccuracy(filenames,predictedY))
# from sklearn.metrics import classification_report