# -*- coding: iso-8859-15 -*-

import numpy as np


# Definindo Filtro
def filtro_passa_baixa_butterworth(tamanho, d0, n):
    largura, altura = tamanho[0], tamanho[1]
    (u, v) = np.meshgrid(range(altura), range(largura))
    d = np.sqrt((u - altura / 2) ** 2 + (v - largura / 2) ** 2)

    return 1 / (1 + d / d0 ** 2 * n)


def filtro_passa_alta_butterworth(tamanho, d0, n):
    filtro = filtro_passa_baixa_butterworth(tamanho, d0, n)

    filtro = 1 - filtro

    return filtro

"""
REFERÊNCIAS:
http://iris.sel.eesc.usp.br/sel5895/Aula%207%20-%20Processamento%20do%20Dominio%20da%20Frequencia.pdf
http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
http://adessowiki.fee.unicamp.br/adesso/wiki/ia636-2009/lionisEX09/edit/
"""



