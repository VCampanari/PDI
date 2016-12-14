# -*- coding: iso-8859-15 -*-

import numpy as np


# Define fun��o que diminui a resolu��o da imagem
def amost_down(imagem, n):
    return imagem[::n, ::n]


# Define fun��o que aumenta a resolu��o da imagem
def amost_up(imagem, n):
    return np.repeat((np.repeat(imagem, n, axis=0)), n, axis=1)

"""
REFER�NCIAS:
https://wiki.python.org/moin/
https://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html?highlight=repeat#numpy.repeat
http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
"""