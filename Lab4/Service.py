

from GA import GA
class Service:

    def __init__(self,repo):
        self.repo=repo
    


    def solve(self,pop,ngen):
        self.gaParam = {"popSize": pop, "noGen" : ngen, "pc" : 0.8, "pm" : 0.1}

        self.problParamL={'function' : self.repo.fitness, 'noNodes' :self.repo.n, 'mat' :self.repo.all}
        self.problParamNN={'function' : self.repo.fitness, 'noNodes' :self.repo.n, 'minims':self.repo.minims() }
        self.problParam_NN={'function' : self.repo.fitness, 'noNodes' :self.repo.n, 'nns':self.repo.NN() }
        ga = GA(self.gaParam, self.problParam_NN)

        ga.initialisation()
        ga.evaluation()
        stop = False
        g = -1
        sol=[]
        while (not stop and g < ngen):
            g += 1
            ga.oneGenerationElitism()
            #self.repo.ga.oneGenerationElitism()
            #ga.oneGenerationSteadyState()
            bestChromo = ga.bestChromosome()
            sol.append(bestChromo)
  
            print('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(bestChromo.fitness))
        
        #self.writer(sol)
        return bestChromo
    
    
