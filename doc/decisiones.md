# Tarea 1

En esta tarea debemos elegir un lenguaje en el que realizar el proyecto.
Hemos dividido en varios puntos a tratar:

1. Lectura de los ficheros hdf5
2. Clases para mantener la información
3. Clase mapa
   - Constructor
   - umt\_YX
   - resize

Hemos elegido Python para aprender más sobre este lenguaje, porque nos parece muy útil, fácil y rápido.

# Clases

- Punto: Representa un punto con coordenadas UMT
- Submapa: Representa un dataset
- Mapa: Colección de submapas
- hdf5\_data\_handler: Para interactuar con los ficheros hdf5 a através de la libreria h5py

# Aspectos importantes de la implementación

Se ha utilizado sobrescritura de métodos de comparación para una mayor legibilidad del código.

Se ha delegado la responsabilidad de comprobar si una coordenada UMT está dento o no de un dataset a la clase submapa y también le corresponde devolver el valor de este punto.

# Problemas

A la hora de probar los ficheros de pruebas, el mapa original no da ningún problema por lo que podemos concluir que hacemos una lectura correcta de datos y la función `umt_YX` también es correcta.
Sin embargo, con los otros mapas redimensionados sí que ocurren discrepancias, pero:

- No es por redondeos, hay casos donde la diferencia es hasta superior a 1.
- No es por prioridad por superposición ya que se comprueban primero los mapas con mayor y y no hay casos de empate.
- Se ha intentado empezar a redimensionar por abajo a la izquierda, da aún más fallos. Curiosamente, esto tarda considerablemente menos.
- No es problema de las funciones transform, ya que ambas fallan y la implementación de estas está proporcionada por python.

# Tarea 2

La implementación de esta es fácil:

1. Estado 
   - Contiene un punto.
   - Guarda una referencia al mapa para poder saber sus sucesores.
   - Es igual a otro estado si el punto es el mismo.
   - Para generar sucesores, iteramos en las posibles direcciones, la creamos, vemos si es válida.

2. Acción
   - Tiene como variables de clase las posibles acciones, el factor y la máxima altura (sujeto a cambios).
   - Al crear una acción, necesitaremos el estado del que partimos, la dirección y el mapa (para saber si es válida).
   - Calculamos la longitud, dependiendo de la dirección, incrementaremos una coordenada la longitud, calculamos la altura y vemos si es válida.

3. Problema
   - Guarda el mapa, el estado inicial y los datos para calcular la función objetivo.

