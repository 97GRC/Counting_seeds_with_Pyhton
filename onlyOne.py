#!/usr/bin/env python3

#Bibliotecas
import cv2                          
import numpy as np
import sys
import os
import pandas as pd
import re
import matplotlib.pyplot as plt

#FUNÇÃO
files = 'feijao_001.jpg' 

def seeds_number(files):
	img = cv2.imread(files)
	blur = cv2.blur(img, (50, 50))
	grey = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
	th = cv2.threshold(grey, 110, 255, cv2.THRESH_BINARY)[1]
	sp = cv2.morphologyEx(th,
                       cv2.MORPH_OPEN,
                       np.ones((10, 10), np.uint8),
                       iterations = 4)
	contours, hierarchy = cv2.findContours(th,
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
	return len(contours)


#LENDO VÁRIOS ARQUIVOS 
os.chdir(sys.argv[1]) #Verificar se só tem imagens e como o nome eh
files = os.listdir()
files.sort()
print(files)
value = 0

num_seeds = []

for i in files:
	imagem = files[value]
	value += 1	
	num_seeds.append(seeds_number(imagem))
	
print(num_seeds)

#CRIANDO ARQUIVO CSV
trat = []
value = 0

for i in files:
	names = files[value]
	value += 1
	match = re.findall(r'^\w.+_', names)
	trat.append(match)
trat2 = [valores for sublista in trat for valores in sublista]
print(trat2)

Id = []
value = 0

for i in files:
	ID = files[value]
	value += 1
	match2 = re.findall(r'\d\d\d', ID)
	Id.append(match2)
Id2 = [val for sublist in Id for val in sublist]
print(Id2) 

#SALVANDO OS DADOS NUM ARQUIVO CSV

df = pd.DataFrame(data={'Trat': trat2, 'Id': Id2, 'num_seeds': num_seeds})
#df.to_csv("./Seeds.csv", sep = ',', index = False)

#ANÁLISE EXPLORATÓRIA
#Bloxplot
boxplot = df.boxplot(by = 'Trat',column = ['num_seeds'], grid='false')
plt.savefig('boxplot.png')	

#Histograma





