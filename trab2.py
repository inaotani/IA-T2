import random
import math
import time

def create_graph (v, k):
    list_vertices = []
    list_edges = []
    for i in range(v):
        x = random.randint(0,v)
        y = random.randint(0,v)
        if (x,y) not in list_vertices:
            list_vertices.append((x,y))

    for vertex in list_vertices:
        low_distances = []
        count = 0
        for aux_vertex in list_vertices:
            if(vertex != aux_vertex):
                distance = '{0:.3g}'.format(math.sqrt(math.pow((vertex[0] - aux_vertex[0]), 2) + math.pow((vertex[1] - aux_vertex[1]), 2)))
                low_distances.append((distance, vertex, aux_vertex))
        
        i = 1
        count = 0

        low_distances = sorted(low_distances, key=lambda x: x[0])

        while count < k and i < v:
            edge = (low_distances[i][0], low_distances[i][2], low_distances[i][1])
            if(edge not in list_edges):
                list_edges.append(low_distances[i])
                count += 1
            i += 1

    return (list_vertices, list_edges)

def get_edges(graph, vertex):
    edges = []
    for edge in graph[1]:
        if(edge[1] == vertex ):
            edges.append(edge)
    return edges

def DFS(graph, initial_v, end_v, past_vertices):
    # print(initial_v)
    edges = get_edges(graph,initial_v)
    past_vertices.append(initial_v)
    if(end_v == initial_v): 
        print(f"Achei final (deep Search) {end_v}")
        return 1
    for edge in edges:
        if(edge[2] not in past_vertices):
            found = DFS(graph, edge[2],end_v, past_vertices)
            if(found): 
                return 1
    return 0

def BFS (graph, index_initial, index_end):
    visited = [False] * (len(graph[0]))
    vertex = graph[0][index_initial]
    vertex_end = graph[0][index_end]
    queue = [] 
    queue.append(vertex)
    visited[index_initial] = True
    while queue: 
        vertex = queue.pop(0) 
        # print(vertex, " ")
        edges = get_edges(graph,vertex)
        for edge in edges:
            index = graph[0].index(edge[2])
            if(vertex_end == vertex):
                print(f"Achei final (BFS) {vertex}")
                return 1
            if visited[index] == False: 
                queue.append(edge[2]) 
                visited[index] = True
    return 0

def func_euclidiana(inicio, fim):   #Função que retorna a distância euclidiana dos parâmetros pedidos
    dist_euclid = math.dist(inicio, fim)
    return dist_euclid

def find_best_index(lista, heuristica):
    menor_valor = 10000000
    melhor_opcao = None
    for i in range(0, len(lista)):
        if heuristica[lista[i]] < menor_valor:
            menor_valor = heuristica[lista[i]]
            melhor_opcao = i

    #print(f"Melhor opção é: {lista[melhor_opcao]}")
    return melhor_opcao

def printar_resultado(caminho, inicio, fim):
    print("Resultado da busca A*:")
    print(f"Estado inicial: {inicio}    Estado final: {fim}")
    print(f"Caminho percorrido: {caminho}")
    print(f"Tamanho do caminho percorrido: {len(caminho)}")
    return

def alg_A_estrela(graph, inicio, fim):
    distancia_percorrida = {}
    euclidiana = {}
    heuristica = {}   #h=distancia_percorrida+distancia_euclidiana
    lista = []      #Lista com todos os vértices que foram encontrados
    caminho = []    #Lista de caminhos já percorridos pelo programa

    #inicializa as variáveis com valores corretos
    lista.append(inicio)
    euclidiana[inicio] = func_euclidiana(inicio, fim)
    distancia_percorrida[inicio] = 0
    heuristica[inicio] = distancia_percorrida[inicio] + euclidiana[inicio]

    while len(lista)!=0:
        #print(f"lista = {lista}")
        best_index = find_best_index(lista, heuristica)
        indice_at = lista.pop(best_index)
        caminho.append(indice_at)

        if(fim == indice_at):
            printar_resultado(caminho, inicio, fim)
            return 1
        
        edges = get_edges(graph, indice_at)
        for edge in edges:
            if edge[2] not in lista and edge[2] not in caminho: #Para conferir que seja analisado somente 1 vez cada nó
                lista.append(edge[2])
                distancia_percorrida[edge[2]] = distancia_percorrida[indice_at] + func_euclidiana(indice_at, edge[2])
                euclidiana[edge[2]] = func_euclidiana(edge[2], fim)
                heuristica[edge[2]] = euclidiana[edge[2]] + distancia_percorrida[edge[2]]
                #print(f"analisando nó atual: {edge[2]} --> heuristica= {heuristica[edge[2]]}\n")
    
    print("Caminho não encontrado!!")

    return 1


graph = create_graph(1000,7)
past_vertices = []

print(f"Inicio: {graph[0][0]}, fim: {(graph[0][3])}")
#print(f"Grafo: {graph}\n")

start = time.time()
search = DFS(graph, graph[0][0], graph[0][3], past_vertices)
end = time.time()
print(end - start)

print(f"Inicio: {graph[0][0]}, fim: {(graph[0][3])}")
start = time.time()
search = BFS (graph, 0, 3)
end = time.time()
print(end - start)

print(f"Inicio: {graph[0][0]}, fim: {(graph[0][3])}")
start = time.time()
search = alg_A_estrela (graph, graph[0][0], graph[0][3])
end = time.time()
print(end - start)



