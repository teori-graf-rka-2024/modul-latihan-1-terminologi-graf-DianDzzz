import graph as g
"""
g.create_graph([(a, b), (b, c)]) => membuat graph dengan edge yang menghubungkan vertex a dan b, b dan c
g.get_degree(grafik, a) => mencari derajat vertex dari grafik vertex a
g.dfs_traversal(grafik, a) => melakukan pencarian dfs menggunakan stack mulai dari vertex a
g.dfs_new(grafik, a) => melakukan pencarian dfs menggunakan library networkx mulai dari vertex a
g.bfs_traversal(grafik, a) => melakukan pencarian bfs menggunakan queue mulai dari vertex a
g.bfs_new(grafik, a) => melakukan pencarian bfs menggunakan library networkx mulai dari vertex a
g.visualize_graph(grafik) => menampilkan graph dengan matplolib, graph ada di direktori yang sama
"""
print("Grafik yang di inisialisasi:")
grafik = g.create_graph([(0, 5), (0, 4), (0, 2), (1, 5), (1, 4), (2, 4), (2, 3), (4, 5)])

print("derajat dari vertex 0:")
g.get_degree(grafik, 0)

print("dfs dengan stack(start node=5):")
g.dfs_traversal(grafik, 5)

print("dfs dengan library(start node=5):")
g.dfs_new(grafik, 5)

print("bfs dengan queue(start node=2):")
g.bfs_traversal(grafik, 2)

print("bfs dengan library(start node=2):")
g.bfs_new(grafik, 2)

print("mencari path terpendek dari vertex 3 ke 5:")
g.find_shortest_path(grafik, 3, 5)

g.visualize_graph(grafik)