import cv2
import time
import os
import src.handTracking as ht

def setup_camera(width=640, height=480, cam_source=0):
    """
    Set up the webcam and configure its properties.

    Parameters:
    width (int): Width of the webcam feed.
    height (int): Height of the webcam feed.

    Returns:
    cv2.VideoCapture: The webcam capture object.
    """
    cap = cv2.VideoCapture(cam_source)
    cap.set(3, width)
    cap.set(4, height)
    return cap

def detect_fingers(detector, lmList):
    """
    Detect the number of raised fingers in the hand.

    Parameters:
    detector (Detector): An instance of the Detector class for hand tracking.
    lmList (list): List containing the landmark positions of the hand.

    Returns:
    tuple: A tuple containing two lists - (fingers, hand).
        fingers (list): A list representing the state of each finger (0: closed, 1: open).
        hand (list): A list indicating the hand detected (0: left hand, 1: right hand).
    """
    fingers = []
    hand = []

    if lmList[2][1] > lmList[17][1]:
        hand.append(1)
        if lmList[detector.tip_ids[0]][1] > lmList[detector.tip_ids[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
    elif lmList[2][1] <= lmList[17][1]:
        hand.append(0)
        if lmList[detector.tip_ids[0]][1] < lmList[detector.tip_ids[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

    for id in range(1, 5):
        if lmList[detector.tip_ids[id]][2] < lmList[detector.tip_ids[id]-2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers, hand

def draw_text(img, text, position, font_scale=2, thickness=2, color=(255, 0, 0)):
    """
    Draw text on the image.

    Parameters:
    img (numpy.ndarray): The image to draw the text on.
    text (str): The text to be displayed.
    position (tuple): The (x, y) coordinates of the text's starting point.
    font_scale (int): Scale factor for the font size (default is 2).
    thickness (int): Thickness of the text (default is 2).
    color (tuple): The color of the text in BGR format (default is red).

    Returns:
    None
    """
    cv2.putText(img, text, position, cv2.FONT_HERSHEY_PLAIN, font_scale, color, thickness)

def main():
    """
    Main function to run the finger counting and gesture recognition.

    Returns:
    None
    """
    wCam, hCam = 640, 480
    detectionCon = 0.7

    cap = setup_camera(wCam, hCam)
    detector = ht.Detector(detectionCon=detectionCon)
    
    pTime = 0

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        img = cv2.flip(img, 1)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:
            fingers, hand = detect_fingers(detector, lmList)
            totalFingers = fingers.count(1)

            draw_text(img, f'Number: {totalFingers}', (70, 70))
            if hand[0] == 0:
                draw_text(img, 'Left Hand', (400, 420))
            elif hand[0] == 1:
                draw_text(img, 'Right Hand', (400, 420))

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        draw_text(img, f'FPS: {int(fps)}', (400, 70))

        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
