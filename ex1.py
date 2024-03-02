import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

metros = ["Charlottenburg", "Savignyplatz", "Zoologischegarten", "Tiergarten", "Bellevue", "Hauptbahnhof", "Friedrichstrasse", "Hakescher Markt", "Alexanderplatz", "Jannowitzbrücke", "Ostbahnhof", "Warschauer Strasse", "Pankow", "Schönchauser Allee", "Klosterstrasse", "Markischer Museum", "Spittelmarkt", "Stadtmittel", "Mohrenstrasse", "Ernst-Reuter-Platz", "Deutscher Oper", "Kaiserdamm", "Wittenau", "Rathaus Reinickendorf", "Nervenklinik", "Lindauer Allee", "Paracelsus-Bad", "Osloer Str", "Pankstr", "Bernauer Str", "Rosenthaler Platz", "Moritzplatz", "Hermannstr"]
for metro in metros:
    G.add_node(metro)
G.add_edges_from([('Charlottenburg', 'Savignyplatz'), ('Savignyplatz', 'Zoologischegarten'), ('Zoologischegarten', 'Tiergarten'),
                  ('Tiergarten', 'Bellevue"'), ('Bellevue', 'Hauptbahnhof'), ('Hauptbahnhof', 'Friedrichstrasse'),
                  ('Friedrichstrasse', 'Hakescher Markt'), ('Hakescher Markt', 'Alexanderplatz'),
                  ('Alexanderplatz', 'Jannowitzbrücke'), ('Jannowitzbrücke', 'Ostbahnhof'), ('Ostbahnhof', 'Warschauer Strasse'),
                  ('Pankow', 'Schönchauser Allee'), ('Schönchauser Allee', 'Alexanderplatz'), ('Alexanderplatz', 'Klosterstrasse'),
                  ('Klosterstrasse', 'Markischer Museum'), ('Markischer Museum', 'Spittelmarkt'), ('Spittelmarkt', 'Stadtmittel'), ('Stadtmittel', 'Mohrenstrasse'), ('Mohrenstrasse', 'Zoologischegarten'), ('Zoologischegarten', 'Ernst-Reuter-Platz'),
                  ('Ernst-Reuter-Platz', 'Deutscher Oper'), ('Deutscher Oper', 'Kaiserdamm'), ('Wittenau', 'Rathaus Reinickendorf'), ('Rathaus Reinickendorf', 'Nervenklinik'), ('Nervenklinik', 'Lindauer Allee'), ('Lindauer Allee', 'Alexanderplatz'), ('Alexanderplatz', 'Klosterstrasse'), ('Klosterstrasse', 'Paracelsus-Bad'), ('Paracelsus-Bad', 'Osloer Str'), ('Osloer Str', 'Pankstr'), ('Pankstr', 'Bernauer Str'), ('Bernauer Str', 'Rosenthaler Platz'), ('Rosenthaler Platz', 'Moritzplatz'), ('Moritzplatz', 'Hermannstr')])

pos = nx.spring_layout(G)

plt.figure(figsize=(10, 9))
nx.draw_networkx(G, pos=pos, with_labels=True, font_weight='normal', node_color='blue', edge_color='red', node_size=400)

plt.axis('off')
plt.title("Underground")
plt.tight_layout()
plt.show()