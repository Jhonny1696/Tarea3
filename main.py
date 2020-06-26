import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats 
from mpl_toolkits import mplot3d

A = []
Matriz_xy = []
Matriz_xyp = []

# Se lee el archivo xy.csv
with open('xy.csv', newline='') as archivo:
  lineas = archivo.read().splitlines()
  lineas.pop(0)

  for l in lineas:
    linea = l.split(',')
    A.append(linea[1:22])


for sublist in A:
 float_sublist = []  
 for x in sublist:
   float_sublist.append(float(x))    
 Matriz_xy.append(float_sublist)

'''
fx y fy son vectores que contienen los puntos de la pdf de cada variable.
'''
# pmf de X y de Y.
fx = np.sum(Matriz_xy, axis = 1)
fy = np.sum(Matriz_xy, axis = 0)

# vector X y Y
vector_x = np.arange(5, 16, 1)
vector_y = np.arange(5, 26, 1)

'''
Se determina que el ajuste de la pdf es una distribución normal en ambos casos. A continuación se define la función de la distribución.
'''
# Distribución gaussiana
def gaussiana(a, mu, sigma):
  return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(a - mu)**2/(2*sigma**2))

'''
Se obtienen los parámetros para cada distribución.
'''
# Parámetros pdf de X y Y
param_x, _ = curve_fit(gaussiana, vector_x, fx)
param_y, _ = curve_fit(gaussiana, vector_y, fy)

mu_x = param_x[0]
sigma_x = param_x[1]

mu_y = param_y[0]
sigma_y = param_y[1]


# Se grafican las pdf del modelo encontrado para x y y.
plt.plot(vector_x, stats.norm.pdf(vector_x, mu_x, sigma_x), label = 'Modelo probabilístico')
plt.plot(vector_y, stats.norm.pdf(vector_y,mu_y, sigma_y), label = 'Modelo probabilístico')

# Se grafica la pdf sin ajuste de x y y.
plt.plot(vector_x, fx, 'o', label = 'Función de densidad marginal')
plt.plot(vector_y, fy,  'o', label = 'Función de densidad')
plt.xlabel('y')
plt.ylabel('f(y)')
plt.legend()
# plt.show()


'''
La ecuación de densidad conjunta se obtiene al multiplicar
la función de densidad marginal de cada variable.
'''
# Ecuacion de la densidad conjunta de x y y.
def gaussiana_xy(a, mux, sigmax, b, muy, sigmay):
  return (1/(np.sqrt(2*np.pi*sigmax**2)) * np.exp(-(a - mux)**2/(2*sigmax**2)))*(1/(np.sqrt(2*np.pi*sigmay**2)) * np.exp(-(b - muy)**2/(2*sigmay**2)))

# Se grafica la pdf conjunta de x y .
X, Y = np.meshgrid(vector_x, vector_y)

f = gaussiana_xy(X, mu_x, sigma_x, Y, mu_y, sigma_y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, f, rstride=1, cstride=1,
cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
ax.view_init(30, 40)

# plt.show()

# Se lee el archivo xyp.csv
with open('xyp.csv') as f:

  lineas = f.read().splitlines() 
  lineas.pop(0)
  
  
  for row in lineas:
    linea = row.split(',')
    Matriz_xyp.append([float(linea[0]), float(linea[1]), float(linea[2])])

Rxy = []

for i in range(len(Matriz_xyp)):
  Rxy.append(Matriz_xyp[i][0] * Matriz_xyp[i][1] * Matriz_xyp[i][2])

correlacion = np.sum(Rxy, axis = 0)




Cxy = []

for i in range(len(Matriz_xyp)):
  Cxy.append((Matriz_xyp[i][0] - mu_x) * (Matriz_xyp[i][1] - mu_y) * Matriz_xyp[i][2])
  
covarianza = np.sum(Cxy, axis = 0)

coef_correlacion = covarianza / (sigma_x * sigma_y)

print('Correlacion: ', correlacion, '\n', 'covarianza: ', covarianza, '\n', 'coeficiente de correlacion: ',  coef_correlacion, '\n')