import csv
import networkx as nx

class MotorRutasIA:
    def __init__(self, archivo_datos):
        self.grafo = nx.DiGraph() 
        self.archivo_datos = archivo_datos
        self.cargar_sistema_experto()

    def cargar_sistema_experto(self):
        try:
            with open(self.archivo_datos, mode='r', encoding='utf-8-sig') as f:
                contenido = f.read().strip()
                lineas = contenido.splitlines()
                header = [h.strip() for h in lineas[0].split(';')]
                idx_ruta = header.index('Ruta')
                idx_paradas = header.index('Estaciones de Parada')

                for i in range(1, len(lineas)):
                    columnas = [c.strip() for c in lineas[i].split(';')]
                    if len(columnas) > max(idx_ruta, idx_paradas):
                        nombre_ruta = columnas[idx_ruta]
                        paradas_texto = columnas[idx_paradas].rstrip('.')
                        paradas = [p.strip() for p in paradas_texto.split(',')]
                        
                        for j in range(len(paradas) - 1):
                            u, v = paradas[j], paradas[j+1]
                            
                            # CLAVE TÉCNICA:
                            # Creamos nodos específicos por ruta para obligar al algoritmo
                            # a preferir mantenerse en la misma línea en lugar de cambiar de ruta en caso de que ya vaya en una que se dirija al destino.
                            nodo_u = f"{u} ({nombre_ruta})"
                            nodo_v = f"{v} ({nombre_ruta})"
                            
                            # Conexión interna de la ruta (Tiempo mas bajo = 1)
                            self.grafo.add_edge(nodo_u, nodo_v, ruta=nombre_ruta, weight=1)
                            
                            # Conexión para entrar/salir de la estación (Trasbordo)
                            # Le damos un tiempo alto (50) para que la IA evite cambiar de bus
                            self.grafo.add_edge(u, nodo_u, ruta="Transfer", weight=50)
                            self.grafo.add_edge(nodo_v, v, ruta="Transfer", weight=50)

            print(f"✅ Conocimiento cargado: {len(self.grafo.nodes)} nodos de red detectados.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def buscar_mejor_ruta(self, inicio, fin):
        try:
            # Dijkstra buscará el camino con menor peso total (evitando los tiempos de 50)
            camino_nodos = nx.shortest_path(self.grafo, source=inicio, target=fin, weight='weight')
            
            resultado = []
            for i in range(len(camino_nodos) - 1):
                u, v = camino_nodos[i], camino_nodos[i+1]
                datos = self.grafo.get_edge_data(u, v)
                
                # Solo nos interesan los tramos que no son "Transfer"
                if datos['ruta'] != "Transfer":
                    # Limpiamos el nombre de la estación (quitamos el "(Ruta)")
                    estacion_origen = u.split(" (")[0]
                    estacion_destino = v.split(" (")[0]
                    resultado.append({
                        "de": estacion_origen, 
                        "a": estacion_destino, 
                        "ruta": datos['ruta']
                    })
            return resultado
        except:
            return None