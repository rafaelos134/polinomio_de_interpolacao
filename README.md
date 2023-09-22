# polinomio_de_interpolacao
A partir de dois pontos distintos ($x_1, y_1$) e ($x_2, y_2$), é possível determinar um único polinômio de primeiro grau (uma reta) que passa por esses pontos, contanto que $x_1 \neq x_2$. Agora, exigindo que $p(x_1) = y_1$ e $p(x_2) = y_2$ é possível analisar um sistema linear não-homogêneo de 2 equações e 2 incógnitas, pois $ax_1+b=y_1$ e $ax_2+b = y_2$.

![image](https://github.com/rafaelos134/polinomio_de_interpolacao/assets/62451921/892cebba-e5d7-4bec-885c-43d6c45efa81)

E o resultado do escalonamento dessa matriz é:

![image](https://github.com/rafaelos134/polinomio_de_interpolacao/assets/62451921/b594616d-ef6f-4811-8b4b-309b001cb364)

Dessa forma, podemos concluir que o sistema é determinado, com $b = \frac{x_2y_1 - x_1y_2}{x_2 - x_1}$ e $a = \frac{y_2 - y_1}{x_2 - x_1}$. Como resultado, o polinômio interpolador para os pontos ($x_1, y_1$) e ($x_2, y_2$) é:

$p(x) =(\frac{y_2-y_1}{x_2-x_1}) x + \frac{x_2y_1-x_1y_2}{x_2-x_1}$




