from collections import *
import pdb
import socket
import re, time
from threading import Thread
from random import randint
import os,re,socket,time,hashlib
from datetime import datetime
from collections import *

class Server(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        
        # relax(0)
        # print len(graph)
        # for i in graph:
        # d, p = bellman_ford(graph, i)
        # p = {} # Stands for predecessor
        # for i in graph:
        #     print i,':',
        #     for j in graph[i]:
        #         print j,
        #     print
        # # d = initialize(graph, source)
        port = 60000
        s = socket.socket()
        host = ""
        s.bind((host, port))
        s.listen(5)
        for i in range(1,N): #Run this until is converges
            # print "************************************i is", i
            # print 'Server listening....'
            for u in range(1,N+1):
                # print "u is " ,u
                # conn, addr = s.accept()
                # print "U IS AGAIN,", u
                #time.sleep(0.1)
                # print "lol"
                tosend=""
                for v in range(1,N+1): #For each neighbour of u
                    tosend = tosend + str(v) + ' ' + str(d[u][v]) + "\n"
                    # relax(u, v, graph, d, p) #Lets relax it
                forwd_table_u = tosend
                for v in graph[u]:
                    conn, addr = s.accept()
                    conn.send(forwd_table_u)
                    
                    
                    #time.sleep(0.1)
                    conn, addr = s.accept()
                    conn.send(str(v))

                    #time.sleep(0.1)
                    conn, addr = s.accept()
                    conn.send(str(u))
                # print "table sent"
                # #time.sleep(0.1)
                # print "data sent, now connection is closed"
                # conn.close()
        # print "out of lloop//////////////////////////////"
        #time.sleep(0.1)
        conn, addr = s.accept()
        conn.send("Bye")
        # print "after BYE sent////////////////////////////"
        # #time.sleep(1)
        conn.close()
        # for u in graph:
        #     for v in graph[u]:
        #         assert d[v] <= d[u] + graph[u][v]

        # def initialize(graph, source):
                    # p[node][Node] = None
            # d[source] = 0 # For the source we know how to reach
            # return d

        # def bellman_ford(graph, source):
        
            # return d, p


        # def test(graph):
class Receiver(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):

        # i=0
        # graph, i = defaultdict(dict), 0
        # with open('test') as f:
        #     lines = f.readlines()
        #     for i in range(1+int(lines[0])):
        #         gf = lines[i].split()
        #         if i != 0:
        #             k=1
        #             for l in range(int(gf[0])):
        #                 if int(gf[k]) not in graph[i]:
        #                     graph[i][int(gf[k])] = int(gf[k+1])
        #                 else:
        #                     graph[i][int(gf[k])] = min(graph[i][int(gf[k])], int(gf[k+1]))
        #                 k=k+2

        distance = defaultdict()

        # def relax(flag):
        # forwarding table
        # node + forwarding table of neighbour
        # d[neighbour] is the value of distance and this is called for all neighbours
        # recv(1024)
        ii=0
        while True:
            ii+=1
            s = socket.socket()
            host = ""
            port = 60000
            s.connect((host, port))
            # s.send("Hello server!")
            # print "relax called"
            # print "waiting to rec"
            # #time.sleep(0.1)
            data = s.recv(1024)
            if ii%3 == 1:
                dist = data
            elif ii%3 == 2: 
                node = int(data)
            else:
                sender = int(data)
                # print "Ok", sender, node,
                # print graph
                dist = dist.split('\n')
                for i in range(len(dist) - 1): 
                    dist[i] = dist[i].split()
                    dist[i][0], dist[i][1] = int(dist[i][0]), int(dist[i][1])
                    distance[dist[i][0]] = dist[i][1]
                for j in graph:
                    # print node, j, sender
                    if d[node][j] > distance[j] + graph[sender][node]:
                        d[node][j] = distance[j] + graph[sender][node]
            # #time.sleep(0.1)
            # print "data is", data
            if data == 'Bye': break
            
        s.close()
        # print 'koud'
        # if d[neighbour] > d[node] + graph[node][neighbour]:
        #     # update
        #     d[neighbour] = d[node] + graph[node][neighbour]
        #     p[neighbour] = node



if __name__ == '__main__': 

    graph, i = defaultdict(dict), 0
    N = 0
    with open('test2') as f:
        lines = f.readlines()
        N = int(lines[0])
        for i in range(1+int(lines[0])):
            gf = lines[i].split()
            if i != 0:
                k=1
                for l in range(int(gf[0])):
                    if int(gf[k]) not in graph[i]:
                        graph[int(gf[k])][i] = int(gf[k+1])
                    else:
                        graph[int(gf[k])][i] = min(graph[i][int(gf[k])], int(gf[k+1]))
                    k=k+2
                # if int(gf[0]) == 0: graph[i]={}

    # print "graph",graph
    d = defaultdict(dict) # Stands for destination
    for node in range(1,N+1):
        for Node in range(1,N+1):
            if node != Node:
                d[node][Node] = 10**123 # We start admiting that the rest of nodes are very very far
            else: d[node][Node] = 0
        
    # print d
    # print graph
    rec=Receiver()
    ser=Server()
    # myThreadOb1 = MyThread(4)
    # myThreadOb1.setName('Thread 1')

    # myThreadOb2 = MyThread(4)
    # myThreadOb2.setName('Thread 2')

    # Start running the threads!
    ser.start()
    time.sleep(0.3)
    rec.start()

    # Wait for the threads to finish...
    ser.join()
    rec.join()
    print N
    for i in range(1,N+1):
        print N - 1,
        for j in range(1,N+1):
            if i!=j:
                if d[i][j] == 10**123:
                    print j, 'inf', 
                else: print j,d[i][j],
        # print 
        print
