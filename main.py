import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import create_pca
import create_kmeans
#pip install openpyxl

def main():
  #importa o arquivo do excel
    arquivo = str(input('Digite o local do arquivo(arquivo excel): '))
    dados =create_pca. PCA(pd.read_excel(arquivo))
#aplica pca na base de dados
    dados.pca(3)
#dados com pca ja aplicado
    dados.dados_pca
#recebe o número de clusters e número de iterações
    k = int(input('Digite o número de clusters(inteiro e positivo): '))
    iteracoes = int(input('Digite o número de iterações(inteiro e positivo): '))
#aplica os dados no k-means
    dados_k_means = create_kmeans.KMeans3D(pd.DataFrame(dados.dados_pca),k,iteracoes)
    dados_k_means.fit()
#plota os graficos
    print('Grafico 3D')
    dados_k_means.plot3d()
    print('Grafico PC1 X PC2')
    dados_k_means.plot1_2()
    print('Grafico PC1 X PC3')
    dados_k_means.plot1_3()
    print('Grafico PC2 X PC3')
    dados_k_means.plot2_3()

if __name__ == '__main__':
    main()