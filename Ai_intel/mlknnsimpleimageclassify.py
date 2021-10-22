import cv2
import numpy as np

##### FIRSTLY importing all cards
red_card = cv2.imread("images/cardred_close.png")
green_card = cv2.imread("images/cardgreen_close.png")
black_card = cv2.imread("images/cardblack_close.png")
background = cv2.imread("images/cardnone.png")

### DEFINING A MEAN FUNC
def averagecolor(image):
    return np.mean(image, axis=(0, 1))
# a = np.ones((1,2))
# print(np.mean(a,axis=(0,1)))
# print(a)

###### NOW FIND THE FEATURES OF EACH CLOSE CARD
# print("RED CARD:",averagecolor(red_card)) #  [ 27.35627604   4.48305664 154.21746094]
# print("GREEN CARD:",averagecolor(green_card))  # [119.53976563 133.40338216  61.1089388 ]
# print("BLACK CARD:",averagecolor(black_card))  # [70.36474609 61.85563477 67.1775651 ]
# print("NO CARD:",averagecolor(background)) # [247.9326888  241.13666016 241.89832357]


########## -----> SHAPE OF EACH IS SAME ie (480, 640, 3)


# # Store the features (average color) and corresponding label (red/green/black/none) for classification
trainX = []
trainY = []
for (card,label) in zip((red_card,green_card,black_card,background),("red","green","black","none")):
    trainX.append(averagecolor(card))
    trainY.append(label)
# print("ALL CARDS FEATURES",trainX) #[array([ 27.35627604,   4.48305664, 154.21746094]), array([119.53976563, 133.40338216,  61.1089388 ]), array([70.36474609, 61.85563477, 67.1775651 ]), array([247.9326888 , 241.13666016, 241.89832357])]
# print("All Colors",trainY)

# print("Shape of trainx",np.array(trainX).shape)
# print("Shape of colors",np.array(trainY).shape)



################################################################## TESTINg
# LOADiNG NEW IMAGE
new_card = cv2.imread("images/cardtestagain.png")
new_card_features = averagecolor(new_card)
print("GIVEN CARD ARRAY::---",new_card_features)

# between the features (average color) of that new image against the features of the images we know
differences = []
for card in trainX:
    differences.append(np.linalg.norm(new_card_features-card))
print("DIFFERENCES APPROX-->",differences)
print("COLOR OF CARD IS::--->",trainY[np.argmin(differences)])


"""RED CARD: [ 27.35627604   4.48305664 154.21746094]
GREEN CARD: [119.53976563 133.40338216  61.1089388 ]
BLACK CARD: [70.36474609 61.85563477 67.1775651 ]
NO CARD: [247.9326888  241.13666016 241.89832357]
All Colors ['red', 'green', 'black', 'none']"""
