#Gabriela Vidal - 4277535
#Ingrid Otani - 108189711

import random
import math
import time
from datetime import timedelta
import networkx as nx
from matplotlib import pyplot as plt
import sys
from scipy.spatial.distance import cityblock

sys.setrecursionlimit(10000)

def createGraph (v, k):
    listVertices = []
    listEdgest = []
    for i in range(v):
        x = random.randint(0,v)
        y = random.randint(0,v)
        if (x,y) not in listVertices:
            listVertices.append((x,y))

    for vertex in listVertices:
        lowDistances = []
        count = 0
        for auxVertex in listVertices:
            if(vertex != auxVertex):
                distance = '{0:.3g}'.format(math.sqrt(math.pow((vertex[0] - auxVertex[0]), 2) + math.pow((vertex[1] - auxVertex[1]), 2)))
                lowDistances.append((distance, vertex, auxVertex))
        
        i = 1
        count = 0

        lowDistances = sorted(lowDistances, key=lambda x: x[0])

        while count < k and i < v:
            edge = (lowDistances[i][0], lowDistances[i][2], lowDistances[i][1])
            if(edge not in listEdgest):
                listEdgest.append(lowDistances[i])
                count += 1
            i += 1

    return (listVertices, listEdgest)

def getEdges(graph, vertex):
    edges = []
    for edge in graph[1]:
        if(edge[1] == vertex ):
            edges.append(edge)
    return edges

def printResult(alg,path):
    print(f"Resultado da busca: {alg}")
    print(f"Caminho percorrido: {path}")
    print(f"Tamanho do caminho percorrido: {len(path)}")
    return 0

def printTime(start,end, alg):
    time = end - start
    formatedTime = "{:0>8}".format(str(timedelta(seconds=time)))
    print(f"Tempo de execução do algoritmo {alg}: {formatedTime}")
    print("=========================")

def DFS(graph, initialVertex, endVertex, pastVertices):
    edges = getEdges(graph,initialVertex)
    pastVertices.append(initialVertex)
    if(endVertex == initialVertex): 
        printResult("Busca Profunda",pastVertices)
        return 1
    for edge in edges:
        if(edge[2] not in pastVertices):
            found = DFS(graph, edge[2],endVertex, pastVertices)
            if(found): 
                return 1
    return 0

def BFS (graph, indexInitial, indexEnd):
    visited = [False] * (len(graph[0]))
    vertexEnd = graph[0][indexEnd]
    path = []
    queue = [] 
    vertex = graph[0][indexInitial]
    queue.append(vertex)
    visited[indexInitial] = True
    while queue: 
        vertex = queue.pop(0) 
        path.append(vertex)
        edges = getEdges(graph,vertex)
        for edge in edges:
            index = graph[0].index(edge[2])
            if(vertexEnd == vertex):
                printResult("Busca por Largura",path)
                return 1
            if visited[index] == False: 
                queue.append(edge[2]) 
                visited[index] = True
    return 0

def BestFirst (graph, indexInitial, indexEnd):
    visited = [False] * (len(graph[0]))
    vertexEnd = graph[0][indexEnd]
    path = []
    queue = [] 
    vertex = graph[0][indexInitial]
    queue.append((vertex,0))
    visited[indexInitial] = True
    while queue: 
        queue = sorted(queue, key=lambda x: x[1])
        vertex = queue.pop(0) 
        path.append(vertex[0])
        edges = getEdges(graph,vertex[0])
        for edge in edges:
            index = graph[0].index(edge[2])
            if(vertexEnd == vertex[0]):
                printResult("Best First",path)
                return 1
            if visited[index] == False: 
                queue.append((edge[2],edge[0])) 
                visited[index] = True
    return 0

def funcEuclidean(start, end):   #Função que retorna a distância euclidiana dos parâmetros pedidos
    distEuclid = math.dist(start, end)
    return distEuclid

def findBestIndex(list, heuristic):
    lowerValue = 10000000
    bestOption = None
    for i in range(0, len(list)):
        if heuristic[list[i]] < lowerValue:
            lowerValue = heuristic[list[i]]
            bestOption = i
    return bestOption

def AStar(graph, start, end):
    travelledDistance = {}
    euclidean = {}
    heuristic = {}   #h=travelledDistance+distancia_euclidean
    list = []      #list com todos os vértices que foram encontrados
    path = []    #list de paths já percorridos pelo programa

    #inicializa as variáveis com valores corretos
    list.append(start)
    euclidean[start] = funcEuclidean(start, end)
    travelledDistance[start] = 0
    heuristic[start] = travelledDistance[start] + euclidean[start]

    while len(list)!=0:
        bestIndex = findBestIndex(list, heuristic)
        indiceAt = list.pop(bestIndex)
        path.append(indiceAt)

        if(end == indiceAt):
            printResult("A*",path)
            return 1
        
        edges = getEdges(graph, indiceAt)
        for edge in edges:
            if edge[2] not in list and edge[2] not in path: #Para conferir que seja analisado somente 1 vez cada nó
                list.append(edge[2])
                travelledDistance[edge[2]] = travelledDistance[indiceAt] + funcEuclidean(indiceAt, edge[2])
                euclidean[edge[2]] = funcEuclidean(edge[2], end)
                heuristic[edge[2]] = euclidean[edge[2]] + travelledDistance[edge[2]]
                #print(f"analisando nó atual: {edge[2]} --> heuristic= {heuristic[edge[2]]}\n")
    
    print("path não encontrado!!")

    return 1

def Manhattan(start, end):
    distManhattan = cityblock(start, end)
    return distManhattan

def AManhattan(graph, start, end):
    travelledDistance = {}
    mink = {}
    heuristic = {}   #h=travelledDistance+mink
    list = []      #list com todos os vértices que foram encontrados
    path = []    #list de paths já percorridos pelo programa

    #inicializa as variáveis com valores corretos
    list.append(start)
    mink[start] = Manhattan(start, end)
    travelledDistance[start] = 0
    heuristic[start] = travelledDistance[start] + mink[start]

    while len(list)!=0:
        bestIndex = findBestIndex(list, heuristic)
        indiceAt = list.pop(bestIndex)
        path.append(indiceAt)

        if(end == indiceAt):
            printResult("A",path)
            return 1
        
        edges = getEdges(graph, indiceAt)
        for edge in edges:
            if edge[2] not in list and edge[2] not in path: #Para conferir que seja analisado somente 1 vez cada nó
                list.append(edge[2])
                travelledDistance[edge[2]] = travelledDistance[indiceAt] + funcEuclidean(indiceAt, edge[2])
                mink[edge[2]] = funcEuclidean(edge[2], end)
                heuristic[edge[2]] = mink[edge[2]] + travelledDistance[edge[2]]
                #print(f"analisando nó atual: {edge[2]} --> heuristic= {heuristic[edge[2]]}\n")
    
    print("path não encontrado!!")

    return 1

def draw(graph):
    G = nx.DiGraph()

    nodes = {}
    for vertex in graph[0]:
        nodes[vertex] = vertex

    edges = []
    for edge in graph[1]:
        edges.append((edge[1],edge[2]))

    G.add_edges_from(edges)

    plt.figure(1,figsize=(20,20)) 
    nx.draw(G, pos=nodes, node_color='lightgreen', with_labels=True, node_size=50, font_size=8)
    plt.show()


#Alterar aqui os valores de V e K
v = 10
k = 2

graph = createGraph(v,k)

#Gera os indices de inicio e fim aleatoriamente
indexStart = random.randint(0,v)
indexEnd = random.randint(0,v)

vertexStart = graph[0][indexStart]
vertexEnd = graph[0][indexEnd]
print("=========================")
print(f"Grafo com v:{v} e k:{k}")
print(f"Indice inicial do vértice: {indexStart}, Indice final do vértice: {indexEnd}")
print(f"Vértice Inicial: {vertexStart}, Vértice Final: {vertexEnd}")
print("=========================")

pastVertices = []

#Busca por Profundidade
start = time.time()
search = DFS(graph, vertexStart, vertexEnd , pastVertices)
end = time.time()
printTime(start,end, "Busca por Profundidade");

#Busca por Largura
start = time.time()
search = BFS(graph, indexStart, indexEnd)
end = time.time()
printTime(start,end, "Busca por Largura");

#Busca Best First
start = time.time()
search = BestFirst(graph, indexStart, indexEnd)
end = time.time()
printTime(start,end, "Busca Best First");

#Busca A*
start = time.time()
search = AStar(graph, vertexStart, vertexEnd)
end = time.time()
printTime(start,end, "Busca A*");

#Busca A
start = time.time()
search = AManhattan(graph, vertexStart, vertexEnd)
end = time.time()
printTime(start,end, "Busca A");


#Função para desenho do gráfico, para executar, basta remover o comentário
draw(graph)
