import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import create_pca
import create_kmeans


def main():
  #importa o arquivo do excel
    arquivo = str(input('Digite o local do arquivo(arquivo excel): '))
    dados =create_pca. PCA(pd.read_excel(arquivo))
#aplica pca na base de dados
    while True:
      pc = int(input('Digite o número de PC desejada(1, 2 ou 3): '))
      if pc > 0 and pc < 4:
        break
    dados.pca(pc)
#dados com pca ja aplicado
    dados.dados_pca
#recebe o número de clusters e número de iterações
    iteracoes = int(input('Digite o número de iterações(inteiro e positivo): '))
#aplica o elbow method na base de dados e plota gráfico de cluster x distorção
    dados_k_means = create_kmeans.KMeans3D(pd.DataFrame(dados.dados_pca),iteracoes)
    dados_k_means.elbow_method()
#recebe número de clusters
    while True:
      dados_k_means.k = int(input("selecione um valor de k (o valor deve ser entre 1 e 10): "))
      if dados_k_means.k > 1 and dados_k_means.k < 10:
        break
#aplica k-means na base de dados com k clusters
    dados_k_means.fit()
#plota os graficos
    if len(dados_k_means.data.columns) == 3:
      dados_k_means.plot3d()
      dados_k_means.plot1_2()
      dados_k_means.plot1_3()
      dados_k_means.plot2_3()
    else:
      dados_k_means.plot2d()

if __name__ == '__main__':
    main()