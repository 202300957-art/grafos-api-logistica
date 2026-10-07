import csv

def cargar_grafo(archivo="rutas.csv"):
    grafo = {}
    with open(archivo, encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            origen = fila["origen"].strip()
            destino = fila["destino"].strip()
            distancia = int(fila["distancia"])
            
            grafo.setdefault(origen, [])
            grafo.setdefault(destino, [])
            
            # Grafo no dirigido (ida y vuelta)
            grafo[origen].append({"destino": destino, "distancia": distancia})
            grafo[destino].append({"destino": origen, "distancia": distancia})
            
    return grafo