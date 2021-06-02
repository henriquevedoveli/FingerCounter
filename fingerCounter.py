# Criado em  : 2021-05-26
# Ult. att   : 2021-06-02
# 
# Autor      : Henrique Vedoveli <henriquevedoveli@gmail.com>
# Notas      : Realiza a contagem de quatos dedos estao levantados em uma das maos


# bibliotecas necessarias
import cv2
import time
import os
import HandTracking as ht 

###############
# setando configurancoes da camera
wCam, hCam = 640, 480
detectionCon = 0.7 # confianca de detecao em porcento

################
# lendo video da webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)


pTime = 0
detector = ht.handDetector(detectionCon=detectionCon )

tipIds = [4,8,12,16,20] #thumb, index, middle, ring, pinky

while True:
    sucess, img = cap.read()
    img = detector.findHands(img)
    img = cv2.flip(img, 1)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []
        hand = []

        # PRIMEIRO LOOP
        # Detecta qual a mao esta na imagem utilizando a distancia da
        # base do dedao a base do dedo minimo.
        # 1 direita; 0 esquerda
        #
        ## SEGUNDO LOOP 
        # Verifica se o dedao esta levantado, com base na distancia
        # da landmark mais extrema dele com a de baixo, caso esteja
        # levantado e adicionado na lista fingers 1, caso esteja abaixado
        # e adicionado na lista 0
        # Como os resultados sao diferentes para a mao direita e esquerda
        # foram criados dois loops                    
        if lmList[2][1] > lmList[17][1]:
            hand.append(1)
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        elif lmList[2][1] <= lmList[17][1]: 
            hand.append(0)
            if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Verificando se os outros quatro dedos estao levantados
        # Quando a landmark mais extrema dos dedos esta abaixo de duas
        # landmarks abaixo significa que o dedo esta abaixado
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Total de dedos levantados
        # se a lista fingers resultante foi [0,1,1,1,1]
        # o numero de dedos levantados na mao sao quatro
        totalFingers = fingers.count(1)
        
        # Escrevendo na imagem
        ## Escrevendo o numero
        cv2.putText(img, f'Number: {totalFingers}', (70,70), cv2.FONT_HERSHEY_PLAIN,
                2, (255, 0, 0), 2)
        ## Escrevendo qual mao esta levantada
        if hand[0] == 0:
            cv2.putText(img, 'Left Hand', (400,420), cv2.FONT_HERSHEY_PLAIN,
                2, (255, 0, 0), 2)
        elif hand[0] == 1:
            cv2.putText(img, 'Right Hand', (400,420), cv2.FONT_HERSHEY_PLAIN,
                2, (255, 0, 0), 2)
                
    # calculando e escrevendo o fps na imagem
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (400,70), cv2.FONT_HERSHEY_PLAIN,
                2, (255, 0, 0), 2)
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)