from collections import *
import pdb
import socket
import re
def initialize(graph, source):
    d = defaultdict(dict) # Stands for destination
    # p = {} # Stands for predecessor
    for node in graph:
        for Node in graph:
            if node != Node:
                d[node][Node] = float('Inf') # We start admiting that the rest of nodes are very very far
            else: d[node][Node] = 0
            # p[node][Node] = None
    # d[source] = 0 # For the source we know how to reach
    return d

def relax():
    # forwarding table
    # node + forwarding table of neighbour
    # d[neighbour] is the value of distance and this is called for all neighbours
    # recv(1024)
    print "relax called";
    s = socket.socket()
    host = ""
    port = 60000

    s.connect((host, port))
    data = s.recv(1024)
    print data;

    # if d[neighbour] > d[node] + graph[node][neighbour]:
    #     # update
    #     d[neighbour] = d[node] + graph[node][neighbour]
    #     p[neighbour] = node

def bellman_ford(graph, source):
    d = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            relax()
            port = 60000
            s = socket.socket()
            host = ""
            s.bind((host, port))
            s.listen(5)
            print 'Server listening....'
            time.sleep(1);
            conn, addr = s.accept()
            print "lol"
            for v in graph: #For each neighbour of u
                tosend = tosend + str(v) + ' ' + str(d[u][v]) + "\n";
                # relax(u, v, graph, d, p) #Lets relax it
            forwd_table_u = str(u) + ' ' + tosend
            conn.send(forwd_table_u)

    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p


def test(graph):
    print len(graph)
    # for i in graph:
    d, p = bellman_ford(graph, i)


if __name__ == '__main__': 
    graph, i = defaultdict(dict), 0
    with open('test') as f:
        lines = f.readlines()
        for i in range(1+int(lines[0])):
            gf = lines[i].split()
            if i != 0:
                k=1
                for l in range(int(gf[0])):
                    graph[i][int(gf[k])] = int(gf[k+1])
                    k=k+2

    # print graph
    test(graph)