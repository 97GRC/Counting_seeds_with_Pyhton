#!/usr/bin/env python3

import sys
import cv2
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


#Pegando os arquivos da pasta
dire = '/home/gcam/Trabalho/Fotos'

imagens = os.listdir(dire) 

#Arquivo para salvar o número de sementes
NumSeeds = np.empty([len(imagens), 3])
seeds = pd.DataFrame(NumSeeds)
seeds.columns = ['imagem', 'face', '#']
 
#Lendo as imagens     

for i in range(0, len(imagens)): #Loop para ler cada imagem dentro da pasta
	img = cv2.imread(dire + imagens[i]) #lendo a imagem
	blur = cv2.blur(img[:, :, 2], (50, 50))   
	grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	th = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)[1]
	sp = cv2.morphologyEx(th, cv2.MORPH_OPEN, np.ones((10, 10), np.uint8))

contours, hierarchy = cv2.findContours(th,
                                       cv2.RETR_EXTERNAL, 
                                       cv2.CHAIN_APPROX_SIMPLE)



