# polinomio_de_interpolacao
\documentclass[a4paper,12pt]{article}
\usepackage[brazil]{babel}
\usepackage{indentfirst}
\usepackage{graphicx}
\usepackage[lmargin = 3cm, tmargin = 3cm, rmargin= 2cm, bmargin = 2cm]{geometry}
\setlength{\parindent}{1.25cm}
\usepackage{amsmath, amsfonts, amssymb}
\usepackage[utf8]{inputenc}
\usepackage{color,colortbl,multirow}
\usepackage{subfigure}
\usepackage[table, x11names]{xcolor}
\usepackage{array}
\usepackage{caption}
\usepackage{hhline}
\usepackage{calrsfs}
\usepackage{natbib}
\usepackage{graphicx}
\usepackage{setspace}
\usepackage{subfig}
\usepackage{amsmath}
\usepackage{scalefnt}
\usepackage{hyperref}

\usepackage[T1]{fontenc} % Codificação da Saída
\usepackage{booktabs}
\usepackage{subfig}


\renewcommand\thesubsection{\Alph{subsection}.}


\begin{document}
\begin{figure}[h]
    \begin{minipage}{0.5\textwidth}
        \includegraphics[width=7cm]{UFMG.png}
    \end{minipage}
    \hspace{-1ex}
    \begin{minipage}{0.5\textwidth}
        \begin{flushright}
        \centering
             Métodos da Física Teórica \\
            \textbf{Aluno:} Rafael Santos Oliveira
        \end{flushright}
    \end{minipage}
\end{figure}

\vspace{-1ex} % Reduz o espaço após a figura
\hrule % Linha horizontal
\vspace{-1ex} % Reduz o espaço após a linha horizontal

\begin{center}
    \Large \textbf{Problema Numérico Interpolação Polinomial}
\end{center}

\vspace{-1ex} % Reduz o espaço após o título
\hrule % Linha horizontal
\vspace{1 cm}
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

E o resultado do escalonamento dessa matriz é:
\begin{equation}
\begin{pmatrix}
1 & 0 &\frac{x_2y_1-x_1y_2}{x_2-x_1} \\
1 & 0 & \frac{y_2-y_1}{x_2-x_1}  \\
\end{pmatrix}
\end{equation}

Assim, é possível concluir que o sistema é determinado, com $b = \frac{x_2y_1 - x_1y_2}{x_2-x_1}$ e $a = \frac{y_2 - y_1}{x_2-x_1}$. Por consequência, o polinômio interpolador dos pontos ($x_1, y_1$) e ($x_2, y_2$) é:

\begin{equation}
    p(x) =(\frac{y_2-y_1}{x_2-x_1}) x + \frac{x_2y_1-x_1y_2}{x_2-x_1}
\end{equation}

Agora para o problema de 4 pontos, sendo eles (-1,15), (0,8), (3,-1) e (12,7), é possível montar a seguinte matriz.


\begin{equation}
\begin{pmatrix}
1 & x_0 & x_0^{2} & x_0^{3}\\
1 & x_1 &  x_1^{2} &x_1^{3}\\
1 & x_2 &   x_2^{2} &x_2^{3}\\
1 & x_3 &  x_3^{2} &x_3^{3}\\
\end{pmatrix}
\begin{pmatrix}
a_0 \\
a_1 \\
a_2 \\
a_3\\
\end{pmatrix}
=
\begin{pmatrix}
y_1 \\
y_2 \\
y_3 \\
y_4 \\
\end{pmatrix}
\end{equation}

Subsistindo os valores, podemos chegar na seguinte matriz escalonada


\begin{equation}
\begin{pmatrix}
1 & -1 & 1 & -1 & 15\\
1 & 0 &  0 & 0 & 8\\
1 & 3 &  9 & 27 & -1\\
1 & 12 &  12^{2} &12^{3} & 7\\
\end{pmatrix}
\sim
\begin{pmatrix}
1 & 0 & 0 &  0 & 8\\
0 & 1 &  0 & 0 & \frac{-2735}{468}\\
0 & 0 &  1 & 0 & \frac{775}{702}\\
0 & 0 &  0 & 1 & \frac{-73}{1404}\\
\end{pmatrix}
\end{equation}

Assim o polinômio de menor grau que passa pelos pontos (-1,15), (0,8), (3,-1) e (12,7) é:

\begin{equation}
    p(x) = 8 - \frac{2735}{468} x + \frac{775}{702} x^2 - \frac{73}{1404}x^3
\end{equation}

Com esse resultado, foi gerado um gráfico usando Python, como mostrado na Figura \ref{fig: plot}. O código utilizado para gerar esse gráfico está disponível na Figura \ref{codigo} e pode ser acessado por meio do \href{https://www.google.com}{\textcolor{blue}{link}} no GitHub.

\begin{figure}[!ht]
    \centering
        \includegraphics[width=10cm]{Imagens/Figure 2023-09-18 203854.png}\\
    \caption{Polinômio de menor grau que que passa pelos pontos (-1,15), (0,8), (3,-1) e (12,7).}
    \label{fig: plot}
\end{figure}


\begin{figure}[!ht]
    \centering
        \includegraphics[width=10cm]{Imagens/code.png}\\
    \caption{Código Python utilizado para gerar o gráfico.}
    \label{fig: codigo}
\end{figure}





\vspace{0.5cm}

\nocite{*}
\nocite{B}
\bibliographystyle{plain}
\bibliography{ref}
\end{document}


