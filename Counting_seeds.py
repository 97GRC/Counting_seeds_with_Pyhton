#!/usr/bin/env python3

#####
#Gabriela R Campos
#CEN0336 - Introdução a programação de computadores aplicadas a ciências biológicas
#Prof. Dr. Diego M. Riãno-Pachón
#Trabalho Final: 'CONTANDO SEMENTES COM PYTHON'
####

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
images.sort() #Organiza a lista em ordem alfabética

if len(images) >= 1:  #Verifica a existencia de imagens a serem analisadas 
	print(f'Há {len(images)} arquivos a serem analisados')
else:
	print('Não há arquivos com a extensão desejada no diretório')
	sys.exit() #Se não há arquivos com a extesão desejada o código será abortado

#VERIFICANDO SE A NOMENCLATURA DOS ARQUIVOS ESTÁ CORRETA
found = re.compile(r'\w.+?\d\d\d') #Padrão necessário para nomear os arquivos
names = list(filter(found.match, images)) #Lista com os arquivos que seguem o padrão requerido
	
if len(names) != len(images):
	print('Os arquivos não estão nomeados da forma necessária')
	sys.exit() #Se a quantidade de imagens a serem analisadas não bate com a quantidade de imagens com a nomenclatura correta o código aborta
else: 
	print('As imagens estão nomeadas da forma correta')
#CONTANDO AS SEMENTES EM CADA ARQUIVO
value = 0
num_seeds = [] #Lista onde a quantidade de sementes de cada imagem irá ser salvo

for i in images: #lê uma imagem por vez e armazena a saída na lista 'num_list'
	imagem = images[value]
	value += 1	
	num_seeds.append(seeds_number(imagem))
	
#CRIANDO ARQUIVO CSV
trat = [] #Lista para armazenar a identificação do 'tratamento' de cada imagem
value = 0

for i in images:
	names = images[value]
	value += 1
	match = re.findall(r'^\w.+_', names) #Procura por um padrão que compõe o nome do tratamento e é delimitado por _
	trat.append(match) #Gera uma lista de lista
trat2 = [valores for sublista in trat for valores in sublista] #Transforma a lista de lista em apenas uma lista

Id = [] #Lista para armazenar a indentificação da parcela/repetição de cada imagem
value = 0

for i in images:
	ID = images[value]
	value += 1
	match2 = re.findall(r'\d\d\d', ID) #Probura o padrão referente à parcela
	Id.append(match2) #Gera uma lista de lista 
Id2 = [val for sublist in Id for val in sublist] #Transforma a lista de lista em apenas uma lista
 
#SALVANDO OS DADOS NUM ARQUIVO CSV

df = pd.DataFrame(data={'Trat': trat2, 'Id': Id2, 'num_seeds': num_seeds})
print(df)

df.to_csv("./Seeds.csv", sep = ',', index = False) #Salva o dataFrame no diretório como um arquivo .csv

#ANÁLISE EXPLORATÓRIA
#Bloxplot
boxplot = df.boxplot(by = 'Trat',column = ['num_seeds'], grid='false')
plt.savefig('boxplot.png') #Salva o gráfico com uma imagem .png no diretório

#Histograma
hist = df.hist(column = 'num_seeds')
plt.savefig('hist') #Salva o gráfico como uma imagem .png





