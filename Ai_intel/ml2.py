from sklearn.metrics import classification_report
import numpy as np
import cv2 
import os

red_card = cv2.imread("images/cardred_close.png")
green_card = cv2.imread("images/cardgreen_close.png")
black_card = cv2.imread("images/cardblack_close.png")
background = cv2.imread("images/cardnone.png")

def averagecolor(image):
    return np.mean(image, axis=(0, 1))

trainX = []
trainY = []
for (card,label) in zip((red_card,green_card,black_card,background),("red","green","black","none")):
    trainX.append(averagecolor(card))
    trainY.append(label)


realtestY = np.array(["black","black","black","black","black",
                     "red","red","red","red","red",
                     "green","green","green","green","green",
                     "none","none","none","none","none"])

# def evalaccuracy(f_names,predictedY):
#     predictedY = np.array(predictedY)
#     if (np.sum(realtestY!=predictedY)>0):
#         print ("Wrong Predictions: (filename, labelled, predicted) ")
#         print (np.dstack([filenames,realtestY,predictedY]).squeeze()[(realtestY!=predictedY)])
#     # Calculate those predictions that match (correct), as a percentage of total predictions
#     return "Correct :"+ str(np.sum(realtestY==predictedY)) + ". Wrong: "+str(np.sum(realtestY!=predictedY)) + ". Correctly Classified: " + str(np.sum(realtestY==predictedY)*100/len(predictedY))+"%"

path = "images/test/"
predictedY = []
filenames = []
for filename in os.listdir(path):
    img = cv2.imread(path+filename)
    img_features = averagecolor(img)
    calculated_distances = []
    for card in (trainX):
        calculated_distances.append(np.linalg.norm(img_features-card))
    prediction = trainY[np.argmin(calculated_distances)]
    
    print (filename + ": " + prediction) #Print out the inferences
    filenames.append(filename)
    predictedY.append(prediction)

# Evaluate Accuracy (the sklearn package provides a useful report)
print ()
print(classification_report(realtestY, predictedY))


def ec(f_names,predictedY):
	return str(np.sum(realtestY==predictedY)*100/len(predictedY))+"%"
# Evaluate Accuracy (our own custom method to output the filenames of the misclassified entries)
print ()
print (ec(filenames,predictedY))


