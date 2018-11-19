import matplotlib.pyplot as plt
import numpy as np
#agora com pontos
#valores no eixo y
y5M_axis  = [0.474, 0.820, 1.134, 1.508, 1.275, 1.482, 0.956]
y10M_axis = [0.277, 0.415, 0.639, 0.692, 0.669, 0.609, 0.539]
y15M_axis = [0.468, 0.504, 0.772, 0.927, 0.799, 0.752, 0.731]
#no eixo x precisa variar de 0 a 3, pois tem 4 valores em y
x_axis = np.arange(len(y5M_axis))

#os parametros podem ser verificados no site do matplotlib
#pode incluir um parâmetro linestyle='dashed' pra ficar pontilhado
#o marker também pode ser outro ex: marker='x'
#pode usar quantas vezes for necessário se precisar incluir outros dados
plt.plot(x_axis, y5M_axis, marker='.', label='5m',
         linewidth=1, markersize=5)
plt.plot(x_axis, y10M_axis, marker=',', label='10m',
         linewidth=1, markersize=5)
plt.plot(x_axis, y15M_axis, marker='o', label='15m',
         linewidth=1, markersize=5)
#se tiver legendas (labels no plot), precisa ter esse comando aqui
plt.legend()

plt.xlabel('Tamanho do Envio')
#Se tiver acento ou caracteres especiais, precisa ter esse u antes da string
plt.ylabel(u'Goodput (Mbit/s)')
#substitui os labels por esses rótulos no eixo x
#se quiser usar os valores de 0 a n não precisa dessa linha
plt.xticks(x_axis, ['50K', '100K', '250K', '500K', '1M', '2.5M', '10M'])

#essa função apenas exibe o gráfico
#plt.show()
plt.savefig('goodputXtamanhoEnvio.pdf')
