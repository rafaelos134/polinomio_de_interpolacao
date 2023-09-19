# polinomio_de_interpolacao
A partir de dois pontos distintos ($x_1, y_1$) e ($x_2, y_2$), é possível determinar um único polinômio de primeiro grau (uma reta) que passa por esses pontos, contanto que $x_1 \neq x_2$. Agora, exigindo que $p(x_1) = y_1$ e $p(x_2) = y_2$ é possível analisar um sistema linear não-homogêneo de 2 equações e 2 incógnitas, pois $ax_1+b=y_1$ e $ax_2+b = y_2$.

\begin{equation}
\begin{pmatrix}
1 & x_1 \\
1 & x_2 \\
\end{pmatrix}
\begin{pmatrix}
b \\
a \\
\end{pmatrix}
=
\begin{pmatrix}
y_1 \\
y_2 \\
\end{pmatrix}
\end{equation}



