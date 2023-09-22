# polinomio_de_interpolacao
A partir de dois pontos distintos ($x_1, y_1$) e ($x_2, y_2$), é possível determinar um único polinômio de primeiro grau (uma reta) que passa por esses pontos, contanto que $x_1 \neq x_2$. Agora, exigindo que $p(x_1) = y_1$ e $p(x_2) = y_2$ é possível analisar um sistema linear não-homogêneo de 2 equações e 2 incógnitas, pois $ax_1+b=y_1$ e $ax_2+b = y_2$.

<div align="center">
    <img width="300 cm" title="titulo da imagem" src="https://github.com/rafaelos134/polinomio_de_interpolacao/assets/62451921/929aa225-0b60-4bfb-a2ea-aad8c8b23311"/>
</div>


E o resultado do escalonamento dessa matriz é:

<div align="center">
    <img width="300 cm" title="titulo da imagem" src="https://github.com/rafaelos134/polinomio_de_interpolacao/assets/62451921/84d22332-f1a2-43ae-b75c-d47c8356c71d"/>
</div>

Dessa forma, podemos concluir que o sistema é determinado, com $b = \frac{x_2y_1 - x_1y_2}{x_2 - x_1}$ e $a = \frac{y_2 - y_1}{x_2 - x_1}$. Como resultado, o polinômio interpolador para os pontos ($x_1, y_1$) e ($x_2, y_2$) é:

 <p align="center">$p(x) =(\frac{y_2-y_1}{x_2-x_1}) x + \frac{x_2y_1-x_1y_2}{x_2-x_1}$</P>

 Agora, considerando o problema com quatro pontos dados: (-1, 15), (0, 8), (3, -1) e (12, 7), podemos criar a seguinte matriz:

<div align="center">
    <img width="300 cm" title="titulo da imagem" src="https://github.com/rafaelos134/polinomio_de_interpolacao/assets/62451921/2895147d-7f76-46e6-a2f8-fa4b0c9088f9"/>
</div>

Subsistindo os valores, chegamos à seguinte matriz escalonada:
<div align="center">
    <img width="300 cm" title="titulo da imagem" src="https://github.com/rafaelos134/polinomio_de_interpolacao/assets/62451921/c6bb019e-d10f-497c-93c8-5aa3b60c337b"/>
</div>
Portanto, o polinômio de menor grau que passa pelos pontos (-1, 15), (0, 8), (3, -1) e (12, 7) é:

 <p align="center"> $p(x) = 8 - \frac{2735}{468} x + \frac{775}{702} x^2 - \frac{73}{1404}x^3$</P>

<div align="center">
    <img width="500 cm" title="titulo da imagem" src="https://github.com/rafaelos134/polinomio_de_interpolacao/assets/62451921/40081dc6-a05b-41eb-93b9-303d9ff4d6ab"/>
</div>

referencia: Rodrigo Fresneda. *Notas de Álgebra Linear v.18-abr-2023*. https://sites.google.com/ufabc.edu.br/fresneda/recursos, 2023.


