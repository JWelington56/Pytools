import cv2
import numpy as np

#criando a imagem limpa de 300x300
imagem = np.zeros((300, 300, 3), np.uint8)
#colocando o retangulo vermelho
cv2.rectangle(imagem, (0,0), (100,300), (0,0,255), -1)
#colocando o retangulo branco
cv2.rectangle(imagem, (100,0), (200,300), (255,255,255), -1)
#colocando o retangulo azul
cv2.rectangle(imagem, (200,0), (300,300), (255,0,0), -1)

cv2.imshow("quadrado", imagem)
cv2.imwrite('../img/blankRectangle.jpg', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()