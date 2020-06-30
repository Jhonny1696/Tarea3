# Tarea3
## 1. A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.

Para encontrar la función de densidad marginal de <img src="https://latex.codecogs.com/gif.latex?X" title="X" /> y <img src="https://latex.codecogs.com/gif.latex?Y" title="Y" /> se aplicó las siguientes propiedades:

<img src="https://latex.codecogs.com/svg.latex?f(x)&space;=&space;\int_{-\infty}^{&plus;\infty}&space;f_{x,y}(x,y)&space;\cdot&space;dy" title="f(x) = \int_{-\infty}^{+\infty} f_{x,y}(x,y) \cdot dy" />

<img src="https://latex.codecogs.com/gif.latex?f(y)&space;=&space;\int_{-\infty}^{&plus;\infty}&space;f_{x,y}(x,y)&space;\cdot&space;dx" title="f(y) = \int_{-\infty}^{+\infty} f_{x,y}(x,y) \cdot dx" />

Al ser variables discretas, las ecuaciones anteriores se traducen como sumatorias de la probabilidad conjunta para cada <img src="https://latex.codecogs.com/gif.latex?X" title="X" /> y cada <img src="https://latex.codecogs.com/gif.latex?Y" title="Y" />. De esta manera, al sumar las probabilidades para una determinada <img src="https://latex.codecogs.com/gif.latex?x_i" title="x_i" /> se encuentra el valor de la pdf en ese punto. Esto se hizo para cada <img src="https://latex.codecogs.com/gif.latex?x_i" title="x_i" /> y <img src="https://latex.codecogs.com/gif.latex?y_j" title="y_j" />.
A nivel de programación, para realizar las sumatorias se utilizó la función `numpy.sum()` con la matríz de probabilidades obtenida del archivo `xy.csv`.
Teniendo la pdf marginal de las vriables se procedió a encontrar el modelo que mejor se ajustara; por la forma de las pdf se determinó que una distribución normal se ajusta bastante bien en ambos casos, por lo que se encontraron los parámetros de los modelos usando el método `curve_fit()` del paquete numpy.
A continuación se presenta un cuadro que incluye el valor de los parámetros del modelo para cada variable:

|Varible|<img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />|<img src="https://latex.codecogs.com/gif.latex?\sigma" title="\sigma" />|
|:---:|:---:|:---:|
|X|9,905|2,299|
|Y|15,08|6,027|

Una vez obtenidos los parámetros se puede construir los modelos:

<img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;\frac{1}{\sqrt{2\pi(2,299)^2}}&space;*&space;exp[\frac{-(x-9,905)^2}{2(2,299)^2}]" title="f(x) = \frac{1}{\sqrt{2\pi(2,299)^2}} * exp[\frac{-(x-9,905)^2}{2(2,299)^2}]" />

<img src="https://latex.codecogs.com/gif.latex?f(y)&space;=&space;\frac{1}{\sqrt{2\pi(6,027)^2}}&space;*&space;exp[\frac{-(x-15,08)^2}{2(6,027)^2}]" title="f(y) = \frac{1}{\sqrt{2\pi(6,027)^2}} * exp[\frac{-(x-15,08)^2}{2(6,027)^2}]" />

## 2. Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?

Al asumir independencia de <img src="https://latex.codecogs.com/gif.latex?X" title="X" /> y <img src="https://latex.codecogs.com/gif.latex?Y" title="Y" />, la función de densidad conjunta se puede obtener al multiplicar las funciones de densidad marginales de cada varible.

<img src="https://latex.codecogs.com/gif.latex?f(x,y)&space;=&space;f(x)&space;*&space;f(y)&space;=&space;\frac{1}{\sqrt{2\pi(2,299)^2}}&space;*&space;exp[\frac{-(x-9,905)^2}{2(2,299)^2}]&space;*&space;\frac{1}{\sqrt{2\pi(6,027)^2}}&space;*&space;exp[\frac{-(x-15,08)^2}{2(6,027)^2}]" title="f(x,y) = f(x) * f(y) = \frac{1}{\sqrt{2\pi(2,299)^2}} * exp[\frac{-(x-9,905)^2}{2(2,299)^2}] * \frac{1}{\sqrt{2\pi(6,027)^2}} * exp[\frac{-(x-15,08)^2}{2(6,027)^2}]" />

## 3. Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado.

### Correlación
Para clcular la correlación entre <img src="https://latex.codecogs.com/gif.latex?X" title="X" /> y <img src="https://latex.codecogs.com/gif.latex?Y" title="Y" /> se utilizó la ecuación (\ref{ecu:correlacion}), para una variable discreta corresponde a la sumatoria de la multiplicación de cada <img src="https://latex.codecogs.com/gif.latex?x_i" title="x_i" /> por cada <img src="https://latex.codecogs.com/gif.latex?y_j" title="y_j" /> por la respectiva probabilidad conjunta.


<img src="https://latex.codecogs.com/gif.latex?R_{xy}&space;=&space;\int_{-\infty}^{&plus;\infty}\int_{-\infty}^{&plus;\infty}xyf_{x,y}(x,y)&space;\cdot&space;dx&space;dy" title="R_{xy} = \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}xyf_{x,y}(x,y) \cdot dx dy" />

A nivel de programación, se recorrió, por medio de bucles `for`, la matriz de probailidades del archivo `xyp.csv` y se realizó la operación mencionada. El resultado obtenido es <img src="https://latex.codecogs.com/gif.latex?\inline&space;R_{xy}&space;=&space;149,54" title="R_{xy} = 149,54" />, que indica el grado en el cual las variables estan linealmente asociadas. Para probar la independencia de las variables se hece la multiplicación de los valores medios, o parámetros <img src="https://latex.codecogs.com/svg.latex?\mu" title="\mu" /> :

<img src="https://latex.codecogs.com/svg.latex?E[x]E[y]&space;=&space;(9,905)(15,08)&space;=&space;149,37" title="E[x]E[y] = (9,905)(15,08) = 149,37" />

Se observa que el valor obtenido con ambos métodos se aproximan bastante entre sí por lo que la suposición de indepedencia fué correcta.



### Covarianza

La covarianza se calcula de forma similar a la correalción, en este caso a los valores de las variables hay que restarle al respectiva media, como lo describe (\ref{ecu:covarianza}). Es importante mencionar que el valor de la media para una distribución normal es igual al parámetro <img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />, que ya había sido calculado previamente.

<img src="https://latex.codecogs.com/gif.latex?C_{xy}&space;=&space;\int_{-\infty}^{&plus;\infty}\int_{-\infty}^{&plus;\infty}(x-\bar{X})(y-\bar{Y})f_{x,y}(x,y)&space;\cdot&space;dx&space;dy" title="C_{xy} = \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}(x-\bar{X})(y-\bar{Y})f_{x,y}(x,y) \cdot dx dy" />

El resultado de la covarianza es <img src="https://latex.codecogs.com/gif.latex?C_{xy}&space;=&space;0,06669" title="C_{xy} = 0,06669" />, del cual lo más impotante es el signo. Al ser signo positivo indica que la correlación es directa, es decir que a grandes valores de <img src="https://latex.codecogs.com/gif.latex?X" title="X" /> corresponde valores grandes de <img src="https://latex.codecogs.com/gif.latex?Y" title="Y" />, y viceversa. Una vez más se confirma la independencia de las variables puesto que el valor de la covarianza es cercano a cero.
### Coeficiente de correlación
Con el valor de la covarianza, se puede usar (\ref{ecu:coef}) para obtener el coeficiente de correlación. En este caso se necesita el valor de desviación estandar de las variables aleatorias, estos valores para una distribución normal corresponden al parámetro <img src="https://latex.codecogs.com/gif.latex?\sigma" title="\sigma" /> y ya había sido calculado anteriormente.

<img src="https://latex.codecogs.com/gif.latex?\rho&space;=&space;\frac{C_{xy}}{\sigma_x&space;\sigma_y}" title="\rho = \frac{C_{xy}}{\sigma_x \sigma_y}" />

El resultado obtenido es <img src="https://latex.codecogs.com/gif.latex?\rho&space;=&space;0,003354" title="\rho = 0,003354" />, este valor cercano a cero indica que la correlación entre <img src="https://latex.codecogs.com/gif.latex?X" title="X" /> y <img src="https://latex.codecogs.com/gif.latex?Y" title="Y" /> no es tan fuerte. 
## 4. Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).
Para graficar las pdf conjunta y  marginales de <img src="https://latex.codecogs.com/gif.latex?X" title="X" /> y <img src="https://latex.codecogs.com/gif.latex?Y" title="Y" />, se utilizó la librería `matplotlib`. Se graficó la pdf original y el modelo superpuesto para ver la semejansa.

![](https://github.com/Jhonny1696/Tarea3/blob/master/pdf-x.png)

![Función de densidad marginal de Y](https://github.com/Jhonny1696/Tarea3/blob/master/pdf-y.png)

![Función de densidada de probabilidd conjunta de X y Y.](https://github.com/Jhonny1696/Tarea3/blob/master/f(x%2Cy).png)
