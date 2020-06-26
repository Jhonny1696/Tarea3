# Tarea3
## 1. A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.

Para encontrar la función de densidad marginal de X y Y se aplicó las siguientes propiedades:

\begin{equation}
f(x) = \int_{-\infty}^{+\infty} f_{x,y}(x,y) \cdot dy
\end{equation}

\begin{equation}
f(y) = \int_{-\infty}^{+\infty} f_{x,y}(x,y) \cdot dx
\end{equation}

Al ser variables discretas, las ecuaciones anteriores se traducen como sumatorias de la probabilidad conjunta para cada X y cada Y. De esta manera, al sumar las probabilidades para una determinada $x_i$ se encuentra el valor de la pdf en ese punto. Esto se hizo para cada $x_i$ y $y_j$.
A nivel de programación, para realizar las sumatorias se utilizó la función `numpy.sum()` con la matríz de probabilidades obtenida del archivo xy.csv.
Teniendo la pdf marginal de las vriables se procedió a encontrar el modelo que mejor se ajustara; por la forma de las pdf se determinó que una distribución normal se ajusta bastante bien en ambos casos, por lo que se encontraron los parámetros de los modelos usando el método `curve_fit()` del paquete numpy.
A continuación se presenta un cuadro que incluye el valor de los parámetros del modelo de cada variable:

|Varible|$\mu$|$\sigma$|
|---|---|---|
|X|9,905|2,299|
|Y|15,08|6,027|

Una vez obtenidos los parámetros se puede construir los modelos:

\begin{equation}
f(x) = \frac{1}{\sqrt{2\pi(2,299)^2}} * exp[\frac{-(x-9,905)^2}{2(2,299)^2}]
\end{equation}

\begin{equation}
f(y) = \frac{1}{\sqrt{2\pi(6,027)^2}} * exp[\frac{-(x-15,08)^2}{2(6,027)^2}]
\end{equation}

## 2. Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?

Al asumir independencia de X y Y, la función de densidad conjunta se puede obtener al multiplicar las funciones de densidad marginales de cada varible.

\begin{equation}
f(x,y) = f(x) * f(y) = \frac{1}{\sqrt{2\pi(2,299)^2}} * exp[\frac{-(x-9,905)^2}{2(2,299)^2}] * \frac{1}{\sqrt{2\pi(6,027)^2}} * exp[\frac{-(x-15,08)^2}{2(6,027)^2}]
\end{equation}

## 3. Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado.

### Correlación
Para clcular la correlación entre X y Y se utilizó la ecuación (\ref{ecu:correlacion})
\begin{equation}\label{ecu:correlacion}
R_{xy} = \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}xyf_{x,y}(x,y) \cdot dx dy
\end{equation}

### Covarianza

\begin{equation}
C_{xy} = \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}(x-\bar{X})(y-\bar{Y})f_{x,y}(x,y) \cdot dx dy
\end{equation}

### Coeficiente de correlaxión

\begin{equation}
\rho = \frac{C_{xy}}{\sigma_x \sigma_y}
\end{equation}
## 4. Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).

![](https://github.com/Jhonny1696/Tarea3/blob/master/pdf-x.png)
![Función de densidad marginal de Y](https://github.com/Jhonny1696/Tarea3/blob/master/pdf-y.png)
![Función de densidada de probabilidd conjunta de X y Y.](https://github.com/Jhonny1696/Tarea3/blob/master/f(x%2Cy).png)
