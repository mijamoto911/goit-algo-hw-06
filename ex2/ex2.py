import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue

def dfs(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == end:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, end, visited, path)
            if new_path:
                return new_path

    path.pop()
    return None

def bfs(graph, start, end):
    visited = set()
    queue = Queue()

    queue.put([start])

    while not queue.empty():
        path = queue.get()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.put(new_path)

            visited.add(node)

    return None

# Creating the graph
G = nx.Graph()
metros = ["Charlottenburg", "Savignyplatz", "Zoologischegarten", "Tiergarten", 
          "Bellevue", "Hauptbahnhof", "Friedrichstrasse", "Hakescher Markt", 
          "Alexanderplatz", "Jannowitzbrücke", "Ostbahnhof", "Warschauer Strasse", 
          "Pankow", "Schönchauser Allee", "Klosterstrasse", "Markischer Museum", 
          "Spittelmarkt", "Stadtmittel", "Mohrenstrasse", "Ernst-Reuter-Platz", 
          "Deutscher Oper", "Kaiserdamm", "Wittenau", "Rathaus Reinickendorf", 
          "Nervenklinik", "Lindauer Allee", "Paracelsus-Bad", "Osloer Str", 
          "Pankstr", "Bernauer Str", "Rosenthaler Platz", "Moritzplatz", "Hermannstr"]

G.add_nodes_from(metros)
G.add_edges_from([('Charlottenburg', 'Savignyplatz'), ('Savignyplatz', 'Zoologischegarten'), ('Zoologischegarten', 'Tiergarten'),
                  ('Tiergarten', 'Bellevue"'), ('Bellevue', 'Hauptbahnhof'), ('Hauptbahnhof', 'Friedrichstrasse'),
                  ('Friedrichstrasse', 'Hakescher Markt'), ('Hakescher Markt', 'Alexanderplatz'),
                  ('Alexanderplatz', 'Jannowitzbrücke'), ('Jannowitzbrücke', 'Ostbahnhof'), ('Ostbahnhof', 'Warschauer Strasse'),
                  ('Pankow', 'Schönchauser Allee'), ('Schönchauser Allee', 'Alexanderplatz'), ('Alexanderplatz', 'Klosterstrasse'),
                  ('Klosterstrasse', 'Markischer Museum'), ('Markischer Museum', 'Spittelmarkt'), ('Spittelmarkt', 'Stadtmittel'), 
                   ('Stadtmittel', 'Mohrenstrasse'), ('Mohrenstrasse', 'Zoologischegarten'), ('Zoologischegarten', 'Ernst-Reuter-Platz'),
                  ('Ernst-Reuter-Platz', 'Deutscher Oper'), ('Deutscher Oper', 'Kaiserdamm'), ('Wittenau', 'Rathaus Reinickendorf'), 
                   ('Rathaus Reinickendorf', 'Nervenklinik'), ('Nervenklinik', 'Lindauer Allee'), ('Lindauer Allee', 'Alexanderplatz'), 
                  ('Alexanderplatz', 'Klosterstrasse'), ('Klosterstrasse', 'Paracelsus-Bad'), ('Paracelsus-Bad', 'Osloer Str'), 
                   ('Osloer Str', 'Pankstr'), ('Pankstr', 'Bernauer Str'), ('Bernauer Str', 'Rosenthaler Platz'), ('Rosenthaler Platz', 'Moritzplatz'), 
                    ('Moritzplatz', 'Hermannstr')])

# Visualizing the graph
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 9))
nx.draw_networkx(G, pos=pos, with_labels=True, font_weight='normal', node_color='orange', edge_color='aqua', node_size=400)
plt.title("Original Graph")
plt.axis('off')
plt.tight_layout()
plt.show()

# Finding paths using DFS and BFS
start_node = 'Charlottenburg'
end_node = 'Moritzplatz'

dfs_path = dfs(G, start_node, end_node)
bfs_path = bfs(G, start_node, end_node)

print("DFS Path:", dfs_path)
print("BFS Path:", bfs_path)

# Visualizing the paths
plt.figure(figsize=(10, 9))
nx.draw_networkx(G.subgraph(dfs_path), pos=pos, with_labels=True, font_weight='normal', node_color='green', edge_color='red', node_size=400)
plt.title("DFS Path")
plt.axis('off')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 9))
nx.draw_networkx(G.subgraph(bfs_path), pos=pos, with_labels=True, font_weight='normal', node_color='blue', edge_color='green', node_size=400)
plt.title("BFS Path")
plt.axis('off')
plt.tight_layout()
plt.show()
