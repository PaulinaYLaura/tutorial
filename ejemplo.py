# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np   #Importa librerías de funciones Numpy, python numérico, dándole el nombre de np
import matplotlib.pyplot as plt   
#Librería Matplotlib que permite realizar gráficas 2D y 3D y personalizarlas como se desee, funciona como MATLAB, se le da el nombre plt                           

def escalon(n0,n1,n2):
    """
Implementación de la función llamada escalon, la cual genera x(n) = u(n-n0); n1 <= n <= n2
La función depende de las siguientes variables:
n0: Punto que indica el inicio de la señal
n1: Indica el inicio del vector de muestras 
n2: Indica el final del vector de muestras 
    """
    n = np.arange(n1,n2+1); # Se crea el vector de muestras cuyo rango va desde n1 a n2+1
    x = (n-n0) >= 0;   
#Se crea el vector x que contiene valores de 1 y 0 en función del resultado de la operación (n-n0) >= 0
#Si la diferencia n-n0 es mayor o igual a 0, como resultado se obtiene true es decir se añade 1 al vector x, de lo contrario su valor es 0

    return [x,n]    #Finaliza la ejecución de la función escalon y devuelve [x,n]