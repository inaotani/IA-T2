import random
import math

def create_graph (v, k):
    list_vertices = []
    list_edges = []
    for i in range(v):
        x = random.randint(0,v)
        y = random.randint(0,v)
        list_vertices.append((x,y))

    for vertex in list_vertices:
        low_distances = []
        count = 0
        for aux_vertex in list_vertices:
            distance = math.sqrt(math.pow((vertex[0] - aux_vertex[0]), 2) + math.pow((vertex[1] - aux_vertex[1]), 2))
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

def deep_search(graph, initial_v, end_v, past_vertices):
    print(f"Entrei no vertice {initial_v}")
    edges = get_edges(graph,initial_v)
    print(f"Edges {edges} \n\n")
    past_vertices.append(initial_v)
    if(end_v == initial_v): 
        print(f"Achei final {end_v}")
        return 1
    for edge in edges:
        if(edge[2] not in past_vertices):
            print(f"Vou para o vertice {edge[2]}")
            found = deep_search(graph, edge[2],end_v, past_vertices)
            if(found): 
                return 1
            print(f"Voltei para o vertice {initial_v}")
    return 0


def get_edges(graph, vertex):
    edges = []
    for edge in graph[1]:
        if(edge[1] == vertex ):
            edges.append(edge)
    return edges
    

graph = create_graph(500,3)
past_vertices = []
# print(graph[0])
# print('-------')
print(graph[1])

print(graph[0][0])
print(graph[0][3])

search = deep_search(graph, graph[0][0], graph[0][3], past_vertices)



