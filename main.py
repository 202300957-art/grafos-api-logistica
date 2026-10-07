from fastapi import FastAPI, HTTPException
from grafo import cargar_grafo
from algoritmos import bfs, dfs

app = FastAPI(
    title="API de Grafos",
    description="API educativa para consultar una red de rutas cargada desde CSV.",
    version="1.0.0"
)

grafo = cargar_grafo("rutas.csv")

@app.get("/")
def inicio():
    return {"mensaje": "API de Grafos funcionando"}

@app.get("/ciudades")
def ciudades():
    return {"ciudades": sorted(grafo.keys())}

@app.get("/conexiones/{ciudad}")
def conexiones(ciudad: str):
    if ciudad not in grafo:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    return {
        "ciudad": ciudad,
        "conexiones": grafo[ciudad]
    }

@app.get("/bfs/{ciudad}")
def recorrido_bfs(ciudad: str):
    if ciudad not in grafo:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    return {
        "inicio": ciudad,
        "algoritmo": "BFS",
        "recorrido": bfs(grafo, ciudad)
    }

@app.get("/dfs/{ciudad}")
def recorrido_dfs(ciudad: str):
    if ciudad not in grafo:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    return {
        "inicio": ciudad,
        "algoritmo": "DFS",
        "recorrido": dfs(grafo, ciudad)
    }

# ==========================================
# RETO DE LA SEMANA
# ==========================================
@app.get("/ruta-directa/{origen}/{destino}")
def ruta_directa(origen: str, destino: str):
    # Validar que ambas ciudades existan
    if origen not in grafo or destino not in grafo:
        raise HTTPException(status_code=404, detail="Una o ambas ciudades no existen en el grafo")
    
    # Buscar si el destino está en las conexiones directas del origen
    for conexion in grafo[origen]:
        if conexion["destino"] == destino:
            return {
                "origen": origen,
                "destino": destino,
                "distancia": conexion["distancia"],
                "mensaje": "Conexión directa encontrada"
            }
            
    # Si termina el ciclo y no lo encontró
    return {"mensaje": "No existe conexión directa entre estas ciudades"}