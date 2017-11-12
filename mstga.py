import networkx as nx
import prufer
import random
import genal

def listFit(s):
    fitness_list = [prufer.fitness(prufer.decode(x,G)) for x in s]
    return fitness_list

def execute(population, population_fit, epoch, pm):
    mutation_number = int(pm*len(population)*len(population[0]))
    for x in range(epoch):
        offspring = [genal.cx_uniform(population[x],population[x+1]) for x in range(0,len(population)-1,2)]
        off = []
        for x in range(len(offspring)):
            off.append(offspring[x][0])
            off.append(offspring[x][1])

        off = genal.mut_randP(off, mutation_number)

        res = [prufer.decode(x,G) for x in off]
        eligible = [x for x in res if x != False]
        eligible_fit = [prufer.fitness(x) for x in eligible]
        eligible = [prufer.encode(x) for x in eligible]

        parentoff = population + eligible
        parentoff_fit = population_fit + eligible_fit
        rank = sorted(zip(parentoff,parentoff_fit), key = lambda x: x[1])
        population = [x for x,v in rank[:4]]
        population_fit = [v for x,v in rank[:4]]
    return population[0], population_fit[0]

def draw(G):
    prufer.draw(G)

G=nx.Graph()

G.add_edge('1','2',weight=2)
G.add_edge('1','8',weight=3)
G.add_edge('1','6',weight=5)
G.add_edge('2','8',weight=6)
G.add_edge('2','3',weight=4)
G.add_edge('3','9',weight=2)
G.add_edge('3','4',weight=2)
G.add_edge('4','9',weight=8)
G.add_edge('4','5',weight=1)
G.add_edge('5','7',weight=2)
G.add_edge('5','6',weight=6)
G.add_edge('6','7',weight=7)
G.add_edge('7','8', weight=1)
G.add_edge('7','9', weight=4)
G.add_edge('8','9', weight=3)

#T = prufer.decode(['1','1','8','7','5','4','3'], G)
epoch = 1000
sample = [['2','2','8','4','9','7','9'],['9','4','9','1','2', '8', '7'], ['2','8','4','5', '4', '9','7'],['8', '3', '4', '9', '7', '7', '7']]
sample += [['6','8','4','4','9','7','9'],['2','3','9','4','9','7','9'],['1','6','4','5','6','7','9'],['8','8','9','9','7','7','8']]
sample_fit = listFit(sample)

print execute(sample, sample_fit, epoch, 0.1)
