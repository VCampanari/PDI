# -*- coding: iso-8859-15 -*-

import numpy as np


# Escala original
ESCALA_MATIZ = 180
ESCALA_SATURACAO = 256


# Normalizando a escala
def normalizar(valor, escala_original, escala_normalizada):
    tamanho_passo = np.uint8(escala_original / escala_normalizada)
    passo = np.uint8(valor / tamanho_passo)
    valor_normalizado = np.uint8(passo * tamanho_passo)

    return valor_normalizado

"""
REFERÊNCIAS:
http://docs.opencv.org/3.1.0/df/d9d/tutorial_py_colorspaces.html
http://docs.opencv.org/3.1.0/d3/df2/tutorial_py_basic_ops.html
https://docs.scipy.org/doc/numpy/user/basics.types.html
"""