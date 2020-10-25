import Model
import copy
import math 

def dfs2(graph, domain):
    vertices = graph.getVertices()
    used_domain = []
    dfsUtil2(vertices, 0, domain, used_domain)

def dfsUtil2(vertices, k, domain, used_domain):
    if len(used_domain) == len(domain) or k ==len(vertices):
        return 
    for i in domain:
        if i not in used_domain:
            print(str(vertices[k]) + "=" , str(i) )
            used_domain_copy = copy.deepcopy(used_domain)
            used_domain_copy.append(i)

            dfsUtil2(vertices, k+1, domain, used_domain_copy)


def getSortedVericesMRV(graph):
    vertices = graph.getVertices()
    vertices.sort( key = lambda x:graph.degree(x), reverse = True)
    return vertices

if __name__ == "__main__":
    G = Model.Graph(["a","b","c","d"])
    G.addEdge("a", "b")
    G.addEdge("b", "c")
    
    #G.addEdge("b", "d")
    d = [1,2,3,4]
    print(getSortedVericesMRV(G))
    print(G.getVertices())

    #dfs2(G, d)
    print("finish")