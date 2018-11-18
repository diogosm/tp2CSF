import matplotlib.pyplot as plt
import numpy as np

#agora com pontos
#valores no eixo y
y_axis  = [51.4, 52.2, 52.2]


#no eixo x precisa variar de 0 a 3, pois tem 4 valores em y
x_axis = np.arange(len(y_axis))

#os parametros podem ser verificados no site do matplotlib
#pode incluir um parâmetro linestyle='dashed' pra ficar pontilhado
#o marker também pode ser outro ex: marker='x'
#pode usar quantas vezes for necessário se precisar incluir outros dados
plt.plot(x_axis, y_axis, marker='.',
         linewidth=1, markersize=5)

#se tiver legendas (labels no plot), precisa ter esse comando aqui
#plt.legend()

plt.xlabel('Distância')
#Se tiver acento ou caracteres especiais, precisa ter esse u antes da string
plt.ylabel(u'Potência do Sinal')
#substitui os labels por esses rótulos no eixo x
#se quiser usar os valores de 0 a n não precisa dessa linha
plt.xticks(x_axis, ['5m', '10m', '15m'])

#essa função apenas exibe o gráfico
#plt.show()
plt.savefig('potenciaXdistancia.pdf')
