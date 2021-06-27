import networkx as nx
from matplotlib import pyplot as plt

G = nx.grid_2d_graph(4,4)

plt.figure(figsize=(6,6))
# pos = {(x,y):(y,-x) for x,y in G.nodes()}
# print(pos)
# print(G.nodes)
# print(G.edges)
pos = {(0, 0): (-1, 10), (0, 1): (-2, 9), (0, 2): (2, 0)}
# G.add_edges_from([((0.5, 0.5), (1, 0)), ((0.5, 0.5), (0, 1)), ((0, 1), (1, 1)), ((0, 1), (0, 2)), ((0, 2), (1, 2)), ((0, 2), (0, 3)), ((0, 3), (1, 3)), ((1, 0), (2, 0)), ((1, 0), (1, 1)), ((1, 1), (2, 1)), ((1, 1), (1, 2)), ((1, 2), (2, 2)), ((1, 2), (1, 3)), ((1, 3), (2, 3)), ((2, 0), (3, 0)), ((2, 0), (2, 1)), ((2, 1), (3, 1)), ((2, 1), (2, 2)), ((2, 2), (3, 2)), ((2, 2), (2, 3)), ((2, 3), (3, 3)), ((3, 0), (3, 1)), ((3, 1), (3, 2)), ((3, 2), (3, 3))])
nx.draw(G, pos=pos, node_color='lightgreen', with_labels=True, node_size=600)

plt.show()