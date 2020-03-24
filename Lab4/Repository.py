from importlib.resources import path
from _pickle import load
from pathlib import Path
from GA import GA
class repo:
    def __init__(self,filename,par):
        self.filename=filename
        self.all=[]
        self.n=None
        if par=="1":
            self.load()
        else:
            self.load_tests()
        
    def NN(self):
        res=[]
        for i in range(self.n):
            start=i
            route=[p for p in range(self.n)]
            path=[]
            path.append(start)
            route.remove(start)
            while len(route)>0:
                min=self.all[start][route[0]]
                poz=route[0]
                for j in route:
                    if self.all[start][j]<min:
                        min=self.all[start][j]
                        poz=j
                path.append(poz)
                route.remove(poz)
            res.append(path)
        return res
            

            

    
    def minims(self):
        li=[]
        for i in range(self.n):
            mini=self.all[i][0]
            po=0
            
            for j in range(1,self.n):
                if self.all[i][j]<mini:
                    mini=self.all[i][j]
                    po=j
            li.append(po)
        return li
            

        
    def fitness(self,comunities):
        sum=0
        for i in range(1,len(comunities)):
            sum=sum+self.all[comunities[i-1]][comunities[i]]
        sum=sum+self.all[comunities[0]][comunities[-1]]
        return sum


    def load_tests(self):

        dataf=Path("/TSP")
        self.filename=dataf /self.filename
        f=open(self.filename,"r")
        self.n=int(f.readline())
        next=f.readline()
        nr=0
        while nr<self.n:
            lista=next.split()
            self.all.append(list(map(int,lista)))
            next=f.readline()
            nr+=1 
    def load(self):
        ''' 
        citeste datele in formatul cerut
        '''
        dataf=Path("/Users/Georgia/Desktop/TSP")
        self.filename=dataf /self.filename
        f=open(self.filename,"r")
        self.n=int(f.readline())
        next=f.readline()
        nr=0
        while nr<self.n:
            lista=next.split(",")
            self.all.append(list(map(int,lista)))
            next=f.readline()
            nr+=1 