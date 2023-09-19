import numpy as np
import matplotlib.pyplot as plt

# Crie um conjunto de valores x
x = np.linspace(-2, 15, 400) # Gere 400 pontos entre -5 e 5

# Calcule os valores de y usando o polinômio
y = 8 - (2735/468) * x + (775/702) * x**2 - (73/1404)*x**3

# Crie o gráfico do polinômio
plt.plot(x, y, label='f(x) = 8-(2735/468)x+(775/702)x²-(73/1404)x³')

points_x = [-1, 0,3,12]  # Coordenadas x dos pontos
points_y = [ 15,8,-1,7]  # Coordenadas y dos pontos
plt.scatter(points_x, points_y, color='red', label='Pontos interpolados') 


# Adicione rótulos de eixos e uma legenda
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Exiba o gráfico
plt.grid(True)
plt.show()






