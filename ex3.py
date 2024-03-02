import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    shortest_paths = nx.single_source_dijkstra_path_length(graph, start)

    for node, distance in shortest_paths.items():
        print(f"Shortest path from {start} to {node}: {distance}")

def main():
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
    G.add_edges_from([('Charlottenburg', 'Savignyplatz', {'weight': 1}),
                      ('Savignyplatz', 'Zoologischegarten', {'weight': 2}),
                      ('Charlottenburg', 'Pankow', {'weight': 3}),
                     ])

    # Visualizing the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 9))
    nx.draw_networkx(G, pos=pos, with_labels=True, font_weight='normal', node_color='orange', edge_color='blue', node_size=400)
    plt.title("Original Graph")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

    start_node = 'Charlottenburg'

    # Running Dijkstra's algorithm
    dijkstra(G, start_node)

if __name__ == "__main__":
    main()
