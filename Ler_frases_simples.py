import pytesseract as ocr

from PIL import Image


frase = ocr.image_to_string(Image.open('img/frase4.jpg'), lang='por')
print(frase)
