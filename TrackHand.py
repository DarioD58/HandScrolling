import cv2
import mediapipe as mp
import time


video = cv2.VideoCapture(0)

handCap = mp.solutions.mediapipe.python.solutions.hands
hands = handCap.Hands()
drawHands = mp.solutions.mediapipe.python.solutions.drawing_utils

while True:
    success, img = video.read()
    imgColor = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgColor)

    #print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            drawHands.draw_landmarks(img, hand, handCap.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)