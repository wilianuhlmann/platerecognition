import pytesseract as ocr
import numpy as np
import cv2
cv2.waitKey()
from PIL import Image

# tipando a leitura para os canais de ordem RGB
imagem = Image.open('img/frente-caminhao/placas-cortadas/c2.jpg')
#imagem = cv2.imread('img/frente-caminhao/placas-cortadas/c2.jpg')
#imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)


# convertendo em um array editável de numpy[x, y, CANALS]
npimagem = np.asarray(imagem).astype(np.uint8)

# diminuição dos ruidos antes da binarização
npimagem[:, :, 0] = 0  # zerando o canal R (RED)
npimagem[:, :, 2] = 0  # zerando o canal B (BLUE)

# atribuição em escala de cinza
im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)

# aplicação da truncagem binária para a intensidade
# pixels de intensidade de cor abaixo de 127 serão convertidos para 0 (PRETO)
# pixels de intensidade de cor acima de 127 serão convertidos para 255 (BRANCO)
# A atrubição do THRESH_OTSU incrementa uma análise inteligente dos nivels de truncagem
ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# reconvertendo o retorno do threshold em um objeto do tipo PIL.Image
binimagem = Image.fromarray(thresh)

# chamada ao tesseract OCR por meio de seu wrapper
phrase = ocr.image_to_string(binimagem, lang='por')


print("Numero da placa é:")
print(phrase)
#cv2.imshow("Encontrado", imagemCinza)
#cv2.waitKey()