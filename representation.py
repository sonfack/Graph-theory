def weighted_graph(vertices):
    edges = []
    weights = []
    number_edges = get_value("Nombre de relations")
    for i in range(number_edges):
        print(f"Relation numero {i+1}")
        u = input("Sommert 1 : ")
        u = u.upper()
        v = input("Sommert 2 : ")
        v = v.upper()
        weight = get_value("Entrez le poid du graph")
        edges.append((u, v))
        weights.append(weight)
        edges.append((v, u))
        weights.append(weight)
    print(edges)
    print(weights)
    return vertices, edges,  weights

def graph(vertices):
    edges = []
    number_edges = get_value("Nombre de relations")
    for i in range(number_edges):
        print(f"Relation numero {i+1}")
        u = input("Sommert 1 : ")
        u = u.upper()
        v = input("Sommert 2 : ")
        v = v.upper()
        edges.append((u, v))
        edges.append((v, u))
    print(edges)
    return vertices, edges, None

def directed_graph(vertices):
    pass

def get_value (message):
    choice = input(message+" : ")
    while not choice.isnumeric():
        choice = input("Entrez une value numerique : ")
    choice = int(choice)   
    return choice

def create_graph():
    
    number_vertices = input("Nombre de sommets : ")
    while not number_vertices.isnumeric():
        number_vertices = input("Nombre de sommets encore : ")
    number_vertices = int(number_vertices)    
    vertices = []
    for i in range(number_vertices):
        vertex = input( f"Sommet numero {i+1} : ")
        vertex = vertex.upper()
        vertices.append(vertex)
    print("La liste des sommets est: ", vertices)
    print("\n\n")
    print("1 graphe oriente\n 2 graph non oriente\n 3 graph a poid\n")
    choix = get_value("Donnez votre choix")
    if choix == 1:
        pass
    if choix == 2:
         vertices, edges, weights = graph(vertices)
    if choix == 3:
        vertices, edges, weights = weighted_graph(vertices)
    return vertices , edges, weights
    
def represent_graph(vertices, edges, graph_type, weights=None):
    adj_mat= []
    for u in vertices:
        row = []
        for v in vertices:
            i = vertices.index(u)
            j = vertices.index(v)
            if (u, v) in edges:
                if graph_type == 3:
                    row.append(str(weights.pop()))
                elif graph_type == 2:
                    row.append("1")
            else:
                row.append("0")
        adj_mat.append(row)
    print(adj_mat)
    return adj_mat

def print_graph(mat):
    print("\n\n")
    for i in mat:
        print("   ".join(i)+"\n")


#sommets, relations, poids = create_graph()
#matrice = represent_graph(sommets, relations, 3, poids )
#print_graph(matrice)
