# -*- coding: iso-8859-15 -*-

import numpy as np
import cv2

# Calculando método OTSU
def calcular_otsu_threshold(imagem):
    # Normalizando histograma
    histograma = cv2.calcHist([imagem], [0], None, [256], [0, 256])
    histograma_normalizado = histograma.ravel() / histograma.max()
    Q = histograma_normalizado.cumsum()

    bins = np.arange(256)

    fn_min = np.inf
    threshold = -1

    for i in range(0, 255):
        p1, p2 = np.hsplit(histograma_normalizado, [i])
        q1, q2 = Q[i], Q[255] - Q[i]
        b1, b2 = np.hsplit(bins, [i])

        m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
        v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2

        fn = v1 * q1 + v2 * q2

        if fn < fn_min:
            fn_min = fn
            threshold = i

    return threshold

# Aplicando threshold
def aplicar_threshold(imagem, threshold):
    nova_imagem = np.copy(imagem)

    preto = np.abs(nova_imagem) < threshold
    nova_imagem[preto] = 0
    branco = np.abs(nova_imagem) > threshold
    nova_imagem[branco] = 255

    return nova_imagem

# Aplicando correção de contraste
def aplicar_correcao_contraste_linear(imagem, imagem_otsu):
    nova_imagem = np.copy(imagem)

    valores = np.where(imagem_otsu == 0)
    correcao_linear = nova_imagem[valores]

    minimo = np.min(correcao_linear)
    maximo = np.max(correcao_linear)

    a = 255

    if (maximo - minimo):
        a = 255 / (maximo - minimo)

    b = -a*minimo
    correcao = np.uint8(a*correcao_linear + b)
    nova_imagem[valores] = correcao

    return nova_imagem

"""
REFERÊNCIAS:
http://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html
https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html
http://wiki.icmc.usp.br/images/b/bb/Otsu_e_derivadas.pdf
http://www2.ic.uff.br/~aconci/OtsuTexto.pdf
"""