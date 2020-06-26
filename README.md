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

|Varible|mu|sigma|
|---|---|---|
|X|||
|Y|||


## 2. Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?



$$a+b=c$$
1. Elemento 1
2. Elemento 2

**palabra en negrita**

## 3. Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado.

## 4. Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).

![Función de densidada de probabilidd conjunta de X y Y.](https://github.com/Jhonny1696/Tarea3/blob/master/f(x%2Cy).png)
