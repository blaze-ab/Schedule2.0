import Model



if __name__ == "__main__":

    G = Model.Graph(["a","b"])

    print(G.degree("a"))

    G.AddEdge("a","b")

    print(G.degree("a"))
    print("Hello")

