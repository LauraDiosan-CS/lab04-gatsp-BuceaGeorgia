
from Repository import repo
from Service import Service
class ui:
    def __init__(self):
        pass


    def main(self):
        while 1==1:
            files=input("Fisier:" )
            ngen=int(input("Generations:"))
            popsize=int(input("Popsize:"))
            r=repo(files,"1")m
            s=Service(r)
            print(str(s.solve(popsize,ngen)))


u=ui()
u.main()
