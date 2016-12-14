# -*- coding: iso-8859-15 -*-

import cv2
import scipy.ndimage as mm
from matplotlib import pyplot as plt

# Importa a imagem
imagem = cv2.imread('.\\Prova\\arroz.tif', cv2.CV_LOAD_IMAGE_GRAYSCALE)

# Aplicando o threshold direto na imagem original
retorno, imagem_threshold = cv2.threshold(imagem, 30, 255, cv2.THRESH_OTSU)

# Criando elemento estruturante circular
elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (60, 60))

# Realizando a abertura
abertura = mm.grey_opening(imagem, structure=elemento_estruturante)

# Realizando o Top-Hat
tophat = imagem - abertura

# Aplicando o threshold na imagem final
retorno, opening_th = cv2.threshold(tophat, 30, 255, cv2.THRESH_OTSU)

# Exibindo resultados
plt.subplot(2, 3, 1), plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 2), plt.imshow(imagem_threshold, cmap='gray')
plt.title('Imagem Threshold'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 4), plt.imshow(abertura, cmap='gray')
plt.title('Imagem Aberta'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 5), plt.imshow(tophat, cmap='gray')
plt.title('Imagem TopHat'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 6), plt.imshow(opening_th, cmap='gray')
plt.title('Imagem Final'), plt.xticks([]), plt.yticks([])

plt.show()
