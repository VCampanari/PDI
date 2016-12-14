# -*- coding: iso-8859-15 -*-

import cv2
import trabalho2 as t2
import util


# Importando imagem RGB
imagem_original_bgr = cv2.imread('02.jpg', cv2.CV_LOAD_IMAGE_COLOR)

# Abrindo imagem RGB e ajustando o tamanho da janela
util.exibir_imagem("Trabalho 2 - Imagem Original", imagem_original_bgr)
util.fechar_imagem("Trabalho 2 - Imagem Original")

# Convertendo imagem RGB para HSI
imagem_original_hsi = cv2.cvtColor(imagem_original_bgr, cv2.COLOR_BGR2HSV)

# Separando as bandas HSI
matiz_original, saturacao_original, intensidade_original = cv2.split(imagem_original_hsi)

# Alterando a escala
matiz_normalizada = t2.normalizar(matiz_original, t2.ESCALA_MATIZ, 30)
saturacao_normalizada = t2.normalizar(saturacao_original, t2.ESCALA_SATURACAO, 32)

# Juntando as bandas HSI
imagem_normalizada_hsi = cv2.merge((matiz_normalizada, saturacao_normalizada, intensidade_original))

# Convertendo imagem HSI para RGB
imagem_normalizada_bgr = cv2.cvtColor(imagem_normalizada_hsi, cv2.COLOR_HSV2BGR)

# Exibindo imagem final
util.exibir_imagem("Trabalho 2 - Imagem Normalizada", imagem_normalizada_bgr)
util.fechar_imagem("Trabalho 2 - Imagem Normalizada")

util.fechar_imagens()

