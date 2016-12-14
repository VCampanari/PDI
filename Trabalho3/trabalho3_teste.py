# -*- coding: iso-8859-15 -*-

import cv2
import trabalho3 as t3
from matplotlib import pyplot as plt

# Importando imagem
imagem_cinza = cv2.imread('mesquita.jpg', cv2.IMREAD_GRAYSCALE)

# Exibindo imagem original
plt.subplot(1, 3, 1), plt.imshow(imagem_cinza, cmap='gray')
plt.title("Trabalho 3 - Imagem Original"), plt.xticks([]), plt.yticks([])

# Calculando o threshold
threshold = t3.calcular_otsu_threshold(imagem_cinza)

# Aplicando o threshold
imagem_threshold = t3.aplicar_threshold(imagem_cinza, threshold)

# Exibindo imagem com threshold
plt.subplot(1, 3, 2), plt.imshow(imagem_threshold, cmap='gray')
plt.title("Trabalho 3 - Imagem Threshold"), plt.xticks([]), plt.yticks([])

# Aplicando correção de contraste
imagem_corrigida = t3.aplicar_correcao_contraste_linear(imagem_cinza, imagem_threshold)

# Exibindo imagem final
plt.subplot(1, 3, 3), plt.imshow(imagem_corrigida, cmap='gray')
plt.title("Trabalho 3 - Imagem Corrigida"), plt.xticks([]), plt.yticks([])

plt.show()
