# -*- coding: iso-8859-15 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt
import prova_q1 as p
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../Trabalho3")
import trabalho3 as t3

# Importa a imagem
imagem = cv2.imread('digital.jpeg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

max = 4

for n in range(1, max):
    # Aplica Fourier no domínio de frequência
    fourier = np.fft.fft2(imagem)
    componente_dc = np.fft.fftshift(fourier)
    espectro_fourier = 20 * np.log(np.abs(componente_dc))

    mascara = p.filtro_passa_alta_butterworth((imagem.shape[1], imagem.shape[0]), 50, n)

    componente_dc = mascara * componente_dc

    retorno_componente_dc = np.fft.ifftshift(componente_dc)
    inversa_fourier = np.fft.ifft2(retorno_componente_dc)
    inversa_fourier = np.abs(inversa_fourier)

    imagem_final = t3.aplicar_threshold(inversa_fourier, 1)

    plt.subplot(max, 5, (n-1)*5+1), plt.imshow(imagem, cmap='gray')
    plt.title("Imagem de entrada N:{}".format(n)), plt.xticks([]), plt.yticks([])
    plt.subplot(max, 5, (n-1)*5+2), plt.imshow(espectro_fourier, cmap='gray')
    plt.title('Transformada de Fourier'), plt.xticks([]), plt.yticks([])
    plt.subplot(max, 5, (n-1)*5+3), plt.imshow(mascara, cmap='gray')
    plt.title('Filtro Passa Alta Butterworth'), plt.xticks([]), plt.yticks([])
    plt.subplot(max, 5, (n-1)*5+4), plt.imshow(inversa_fourier, cmap='gray')
    plt.title('Imagem com filtro'), plt.xticks([]), plt.yticks([])
    plt.subplot(max, 5, (n-1)*5+5), plt.imshow(imagem_final, cmap='gray')
    plt.title('Imagem final'), plt.xticks([]), plt.yticks([])

plt.show()






