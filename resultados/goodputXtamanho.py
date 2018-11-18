import matplotlib.pyplot as plt
import numpy as np

#agora com pontos
#valores no eixo y já calculada a média das cinco execuções
y50k_axis  = [0.474, 0.277, 0.468]
y100k_axis = [0.820, 0.415, 0.504]
y250k_axis = [1.134, 0.639, 0.772]
y500k_axis = [1.508, 0.692, 0.927]
y1M_axis   = [1.275, 0.669, 0.799]
y2_5M_axis = [1.482, 0.609, 0.752]
y10M_axis  = [0.956, 0.539, 0.731]
#no eixo x precisa variar de 0 a 3, pois tem 4 valores em y
x_axis = np.arange(3)

#os parametros podem ser verificados no site do matplotlib
#pode incluir um parâmetro linestyle='dashed' pra ficar pontilhado
#o marker também pode ser outro ex: marker='x'
#pode usar quantas vezes for necessário se precisar incluir outros dados
plt.plot(x_axis, y50k_axis, marker='.', label='50K',
         linewidth=1, markersize=5)
plt.plot(x_axis, y100k_axis, marker=',', label='100K',
         linewidth=1, markersize=5)
plt.plot(x_axis, y250k_axis, marker='o', label='250K',
         linewidth=1, markersize=5)
plt.plot(x_axis, y500k_axis, marker='v', label='500K',
         linewidth=1, markersize=5)
plt.plot(x_axis, y1M_axis, marker='s', label='1M',
         linewidth=1, markersize=5)
plt.plot(x_axis, y2_5M_axis, marker='D', label='2.5M',
         linewidth=1, markersize=5)
plt.plot(x_axis, y10M_axis, marker='x', label='10M',
         linewidth=1, markersize=5)

#se tiver legendas (labels no plot), precisa ter esse comando aqui
plt.legend()

plt.xlabel('Distância')
#Se tiver acento ou caracteres especiais, precisa ter esse u antes da string
plt.ylabel(u'Goodput')
#substitui os labels por esses rótulos no eixo x
#se quiser usar os valores de 0 a n não precisa dessa linha
plt.xticks(x_axis, ['5m', '10m', '15m'])

#essa função apenas exibe o gráfico
#plt.show()
plt.savefig('goodputXtamanho.pdf')
