
"""

Este programa calcula, a partir do sinal gerado usando a biblioteca random, a transformada
rápida de Fourier, e obtem a série multiplicando
a transformada pelo fator 2*deltaT/T,ou 2/N,
pois ck = (1/T)*INT(---*deltaT)=(ak-jbk)/2.

O Gráfico é gerado usando a biblioteca mathplot.

referencia 01: https://github.com/stsievert/python-drawnow
referencia 02: https://matplotlib.org


@autores: Rogério, Jader, Milena, Diego

"""

import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import random 
import function
from drawnow import *
import serial


tensao_array = []
cos=np.cos
sen=np.sin
dpi=2.*np.pi

N=64*4
T=dpi
h=T/N

#Seta o gráfico
fig = plt.figure(0)
fig.canvas.set_window_title('Oscilocópio Digital')


#funcoes
def f(N):
    x=np.arange(0,N)*h
    return x,tensao_array

def DFT(signal,N):
    k=np.arange(N)
    n=k.reshape((N,1))
    zexpo=np.exp(-1j*dpi*n*k/N)
    dftz=np.dot(zexpo,signal)
    return dftz
    
def FFT(signal,Nf):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    
    if Nf % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif Nf <= 16: 
        return DFT(signal,Nf)
    else:
        X_even =FFT(signal[::2],len(signal[::2]))
        X_odd = FFT(signal[1::2],len(signal[1::2]))
        factor = np.exp(-1j * dpi * np.arange(Nf/2) / Nf)
        return np.concatenate([X_even + factor * X_odd,
                               X_even - factor * X_odd])
           
def grafico():

    plt.plot
    plt.title('FFT')
    plt.grid()    
    plt.xlabel('Frequência (HZ)')
    plt.ylabel('Amplitude (V)')
    plt.ylim(-1,1)
    plt.plot(wf[0:Mxp],  np.abs(dftz[0:Mxp]),'b',label='Spectro (W)')
    plt.legend(loc='upper right')

while(1):
    p =0.03
    tensao_array = []
    
    tensao = np.random.rand(1)
    while(len(tensao_array)<256):
        if tensao > p:
            tensao = np.random.rand(1)
            tensao_array.append(tensao)
        else:
            np.random.rand(1)
            tensao = np.random.rand(1)
            tensao_array.append(tensao)
        
        
    x,signal=f(N)
    start = timer()
    dftz=DFT(signal,N)*2/N
    end = timer()
    dftz[0]=dftz[0]/2. # O primeiro termo da série é a0/2 

    ksample=np.linspace(0,N,N)
    wf=ksample*dpi/(N*h)
    Mxp=int(N/2.)

    drawnow(grafico)


            
