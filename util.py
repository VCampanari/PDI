# -*- coding: iso-8859-15 -*-

import cv2
import time


# Exibir imagem e ajustar tamanho da janela
def exibir_imagem(nome, imagem, duracao=0):
    cv2.namedWindow(nome, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(nome, imagem.shape[1], imagem.shape[0])
    cv2.imshow(nome, imagem)

    # Aguardar
    if duracao:
        cv2.waitKey(5)
        time.sleep(duracao)
    else:
        cv2.waitKey(0)


# Fechar imagem
def fechar_imagem(nome):
    cv2.destroyWindow(nome)


def fechar_imagens():
    cv2.destroyAllWindows()
