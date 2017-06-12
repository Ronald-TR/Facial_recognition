import cv2


def drawRectsInface(imagem):
    mask_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('c:\haarcascade_frontalface_default.xml').detectMultiScale(mask_cinza, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(imagem, 'Testando Haar CV intel', (x, y + h), cv2.FONT_ITALIC, 1, (255, 255, 255), 2, cv2.LINE_AA)
        rosto_cinza = mask_cinza[y:y + h, x:x + w]
        rosto_colorido = imagem[y:y + h, x:x + w]
        olhos = cv2.CascadeClassifier('c:\haarcascade_eye.xml').detectMultiScale(rosto_cinza)
        for (ex, ey, eh, ew) in olhos:
            cv2.rectangle(rosto_colorido, (ex, ey), (ex + ew, ey + eh), (255, 255, 255), 2)

    return imagem
