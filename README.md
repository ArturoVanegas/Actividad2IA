# Actividad2IA
Estudiante: Dadey Arturo Vanegas Mendieta / Carrera Ingenieria de Software / ID Banner: 100029953
Desarrollo de la "Actividad 2 - Búsqueda y sistemas basados en reglas": Materia "Inteligencia artificial"; Docente JOAQUIN SANCHEZ

🚌 Sistema Inteligente de Rutas - Trans-IArthur
Este proyecto fue desarrollado para la Actividad 2: Búsqueda y sistemas basados en reglas del curso de Inteligencia Artificial. 
Consiste en un sistema capaz de calcular la ruta óptima entre cualquier par de estaciones de un sistema de transporte masivo, en este caso las rutas de transmilenio, utilizando lógica de grafos y algoritmos de búsqueda.

Descripción del Proyecto
El sistema utiliza una Base de Conocimiento estructurada en un archivo CSV para construir un modelo de red en el cual se incluyeron las rutas del sistema transmilenio desde su origen, hasta punto de destino y a su vez las estaciones o paradas correspondientes de cada una. 
A través de un motor lógico desarrollado en Python, el programa infiere las conexiones entre estaciones y determina no solo el camino más corto, sino también en qué puntos el usuario debe realizar trasbordos de ruta.

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
