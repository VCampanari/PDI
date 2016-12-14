# -*- coding: iso-8859-15 -*-

import cv2
import trabalho1 as t1
import util


# Importa a imagem
imagem = cv2.imread('01.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

# Pega a altura m�xima da imagem
altura = imagem.shape[0]

# Exibir imagem
util.exibir_imagem("Trabalho 1 - Imagem Original", imagem)
util.fechar_imagem("Trabalho 1 - Imagem Original")

# Diminuindo a resolu��o da imagem
for i in range(1, altura):
    imagem2 = t1.amost_up(t1.amost_down(imagem, i), i)
    util.exibir_imagem("Trabalho 1 - Diminuindo Resolu��o", imagem2, 0.1)

util.fechar_imagem("Trabalho 1 - Diminuindo Resolu��o")

# Aumentando a resolu��o da imagem
for i in reversed(range(1, altura)):
    imagem2 = t1.amost_up(t1.amost_down(imagem, i), i)
    util.exibir_imagem("Trabalho 1 - Aumentando Resolu��o", imagem2, 0.1)

util.fechar_imagem("Trabalho 1 - Aumentando Resolu��o")
util.fechar_imagens()

