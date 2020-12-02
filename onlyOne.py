#!/usr/bin/env python3

#Bibliotecas
import cv2              #Leitura e manipulação das imagens                     
import numpy as np      #Manioulação de arrays 
import sys              
import os               #Manipular caminhos
import pandas as pd     #Análise de dados
import re               #Regular Expressions
import matplotlib.pyplot as plt #Criar, manipular e salvar plots
import glob             #Encontra arquivos com um padr~so específico

#FUNÇÃO seeds_number
files = 'feijao_001.jpg' #arquivo base para criar a função

def seeds_number(files):
	img = cv2.imread(files) #Leitura da imagem
	blur = cv2.blur(img, (50, 50)) #Desfoque da imagem
	grey = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY) #Transformação em preto e branco
	th = cv2.threshold(grey, 110, 255, cv2.THRESH_BINARY)[1] #Transformação da imagem em binária, usando um threshold de 110
	sp = cv2.morphologyEx(th, #Remove o ruido presente na imagem binária
                       cv2.MORPH_OPEN,
                       np.ones((10, 10), np.uint8), #Transforma th num array
                       iterations = 4)
	contours, hierarchy = cv2.findContours(th, #Encontra os contornos presentes na imagem
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
	return len(contours) #Retorna a quantidade de contornos encontrados


#LENDO VÁRIOS ARQUIVOS 
os.chdir(sys.argv[1]) #Muda o diretório de trabalho para aquele contendo as imagens 

#VERIFICANDO SE A IMAGENS NO DIRETÓRIO
images = glob.glob('*.jpg') #Filtra apenas as imagens .jpg e retorna os nomes numa lista

if len(images) >= 1:
	print(f'Há {len(images)} arquivos a serem analisados')
else:
	print('Não há arquivos com a extensão desejada no diretório')
	sys.exit() #Se não há arquivos com a extesão desejada o código é parado

#VERIFICANDO SE A NOMENCLATURA DOS ARQUIVOS ESTÁ CORRETA
found = re.compile(r'\w.+?\d\d\d') #Padrão necessário para nomear os arquivos
names = list(filter(found.match, images)) #Lista com os arquivos que seguem o padrão requerido
	
if len(names) != len(images):
	print('Os arquivos não estão nomeados da forma necessária')
	sys.exit() #Se a quantidade de imagens a serem analisadas não bate com a quantidade de imagens com a nomenclatura correta o código aborta

#CONTANDO AS SEMENTES EM CADA ARQUIVO
value = 0
num_seeds = []

for i in images:
	imagem = images[value]
	value += 1	
	num_seeds.append(seeds_number(imagem))
	
#print(num_seeds)

#CRIANDO ARQUIVO CSV
trat = []
value = 0

for i in images:
	names = images[value]
	value += 1
	match = re.findall(r'^\w.+_', names)
	trat.append(match)
trat2 = [valores for sublista in trat for valores in sublista]

Id = []
value = 0

for i in images:
	ID = images[value]
	value += 1
	match2 = re.findall(r'\d\d\d', ID)
	Id.append(match2)
Id2 = [val for sublist in Id for val in sublist]
 

#SALVANDO OS DADOS NUM ARQUIVO CSV

df = pd.DataFrame(data={'Trat': trat2, 'Id': Id2, 'num_seeds': num_seeds})
print(df)

df.to_csv("./Seeds.csv", sep = ',', index = False)

#ANÁLISE EXPLORATÓRIA
#Bloxplot
boxplot = df.boxplot(by = 'Trat',column = ['num_seeds'], grid='false')
plt.savefig('boxplot.png')

#Histograma
hist = df.hist(column = 'num_seeds')
plt.savefig('hist')





