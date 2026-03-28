# Actividad2IA
Estudiante: Dadey Arturo Vanegas Mendieta / Carrera Ingenieria de Software / ID Banner: 100029953
Desarrollo de la "Actividad 2 - Búsqueda y sistemas basados en reglas": Materia "Inteligencia artificial"; Docente JOAQUIN SANCHEZ


🚌 Sistema Inteligente de Rutas - Trans-IArthur
Este proyecto fue desarrollado para la Actividad 2: Búsqueda y sistemas basados en reglas del curso de Inteligencia Artificial. 
Consiste en un sistema capaz de calcular la ruta óptima entre cualquier par de estaciones de un sistema de transporte masivo, en este caso las rutas de transmilenio, utilizando lógica de grafos y algoritmos de búsqueda.


Descripción del Proyecto
El sistema utiliza una Base de Conocimiento estructurada en un archivo CSV para construir un modelo de red en el cual se incluyeron las rutas del sistema transmilenio desde su origen, hasta punto de destino y a su vez las estaciones o paradas correspondientes de cada una. 
A través de un motor lógico desarrollado en Python, el programa infiere las conexiones entre estaciones y determina no solo el camino más corto, sino también en qué puntos el usuario debe realizar trasbordos de ruta.

📖 Guía de Uso del Sistema
Para interactuar con el buscador, el usuario debe ingresar los nombres de las estaciones siguiendo estas reglas de formato:

Sintaxis Exacta: El sistema busca coincidencias exactas con la base de conocimiento (rutas.csv). Se deben incluir tildes, mayúsculas y espacios (Ejemplo: escribir Portal Américas y no portal americas).

Nombres Compuestos: Las estaciones con guiones o números deben escribirse tal como aparecen en el sistema oficial (Ejemplo: NQS - Calle 38 Sur o Av. 68).

Salida del Sistema: El programa arrojará una lista secuencial de paradas. Cuando el algoritmo detecte que es necesario un cambio de bus, mostrará la instrucción "TOMA la ruta: [Nombre]". De lo contrario, solo listará las estaciones intermedias bajo la ruta actual.


⚠️ Posibles Errores y Soluciones:

El sistema está diseñado para capturar eventos inesperados y guiar al usuario:

Error de columna: No se encuentra la columna...: Este error ocurre si el archivo rutas.csv tiene una fila en blanco al principio o si los nombres de los encabezados fueron modificados.

⚠️ ERROR: Una de las estaciones no se encuentra: Aparece si el usuario comete un error de ortografía o si la estación ingresada no existe en ninguna de las rutas cargadas.

⚠️ No hay una ruta disponible: Ocurre si el origen y el destino pertenecen a redes que no tienen ningún punto de conexión lógico en el grafo (aunque con 150 estaciones cargadas, esto es poco probable).

FileNotFoundError: Si el archivo rutas.csv no está en la misma carpeta que el código, el sistema no podrá cargar la base de conocimiento.


Componentes del Sistema:

1. rutas.csv (Base de Conocimiento): Contiene los hechos del sistema. Incluye los nombres de las rutas y la secuencia exacta de sus estaciones de parada.

2. motor_logico.py (Cerebro del Sistema): - Utiliza la librería NetworkX para representar el sistema de transporte como un Grafo.

➛ Reglas de Adyacencia: El motor interpreta que si dos estaciones son consecutivas en una ruta, existe una conexión directa (arista) entre ellas.
   
➛ Búsqueda Heurística: Implementa el Algoritmo de Dijkstra para encontrar la ruta con el menor número de estaciones (mínimo desplazamiento).

3. main.py (Interfaz de Usuario): Permite la interacción con el sistema experto, solicitando un origen y un destino para devolver las instrucciones de viaje detalladas.
   

🛠️ Tecnologías Utilizadas:

Python 3.10+

NetworkX: Para la creación, manipulación y estudio de la estructura de redes complejas.

CSV Module: Para la gestión y carga de la base de conocimiento.
