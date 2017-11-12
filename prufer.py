try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx

def draw(G):
    pos=nx.spring_layout(G) # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G,pos,node_size=700)
    # edges
    nx.draw_networkx_edges(G,pos,edgelist=G.edges(),
                        width=6)
    nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
    plt.axis('off')
    #plt.savefig("weighted_graph.png") # save as png
    plt.show() # display

def fitness(G):
    return sum([d['weight'] for u,v,d in G.edges(data=True)])

def encode(G):
    E=[]
    while(G.size()!=1):
        leaf = [x for x in G.nodes_iter() if G.degree(x)==1]
        w = str(min(int(s) for s in leaf))
        E.append(G.neighbors(w)[0])
        G.remove_node(w)

    return E

def decode(s, G):
    T = nx.Graph()
    s = [int(x) for x in s]
    t = [x for x in range(1,len(s)+3) if x not in s]
    while(s):
        pop = s.pop(0)
        lowt = t.pop(minIndex(t))
        try:
            T.add_edge(str(pop), str(lowt), weight=G.get_edge_data(str(pop), str(lowt)).values()[0])
        except AttributeError:
            return False
        if pop not in s:
            t.append(pop)
    try :
        T.add_edge(str(t[0]), str(t[1]), weight=G.get_edge_data(str(t[0]), str(t[1])).values()[0])
    except AttributeError:
        return False
    return T

def minIndex(number):
    m = 0
    for i in range(len(number)):
        if number[i]<number[m]:
            m=i
    return m
