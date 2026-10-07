from collections import deque

def bfs(grafo, inicio):
    if inicio not in grafo:
        return []
    visitados = set()
    cola = deque([inicio])
    recorrido = []
    
    while cola:
        nodo = cola.popleft()
        if nodo in visitados:
            continue
            
        visitados.add(nodo)
        recorrido.append(nodo)
        
        for conexion in grafo[nodo]:
            vecino = conexion["destino"]
            if vecino not in visitados:
                cola.append(vecino)
                
    return recorrido

def dfs(grafo, inicio):
    if inicio not in grafo:
        return []
    visitados = set()
    recorrido = []
    
    def recorrer(nodo):
        visitados.add(nodo)
        recorrido.append(nodo)
        for conexion in grafo[nodo]:
            vecino = conexion["destino"]
            if vecino not in visitados:
                recorrer(vecino)
                
    recorrer(inicio)
    return recorrido