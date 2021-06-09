import random
population = {}
def offspring(parent1,parent2,identifier):
    child_start = random.choice([parent1,parent2])
    mutate = random.choice([1,1,1,1,1,1,1,1,1, 1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,6,6,6,7,7,8,8,9,10,0])
    if mutate == 0:
        child_trait = float(child_start)
    elif mutate == 1:
        child_trait = child_start+(random.random()/2)
    elif mutate == 2:
        child_trait = child_start+(random.random())
    elif mutate == 3:
        child_trait = child_start+(random.random()*1.25)
    elif mutate == 4:
        child_trait = child_start+(random.random()*1.5)
    elif mutate ==5:
        child_trait = child_start+(random.random()*1.75)
    elif mutate == 6:
        child_trait = child_start+(random.random()*2.00)
    elif mutate == 7:
        child_trait = child_start+(random.random()*2.5)
    elif mutate == 8:
        child_trait = child_start+(random.random()*3.5)
    elif mutate == 9:
        child_trait = child_start+(random.random()*4)
    elif mutate == 10:
        child_trait = child_start+(random.random()*6)
    population[f'{identifier}']=child_trait
def day():
    for i in range(0,int(list(population)[-1])+1):
        try:
            organism = population[str(i)]
            if round(organism) == 2:
                survive = random.choice([True,True,True,True,False])
            if round(organism) != 2:
                survive = random.choice([False, False, False,True, True])
            reproduce = random.choice([True,False,True,True,True])
            if survive != True:
                del population[str(i)]
            if len(population) > 1000:
                if random.choice([True,True,False]):
                    del population[str(i)]
            if organism >=7:
                del population[str(i)]
            if reproduce:
                offspring(organism,organism,int(list(population)[-1])+1)
            if len(population)< 50:
                offspring(organism, organism, int(list(population)[-1]+1))
                offspring(organism, organism, int(list(population)[-1]+1))
                offspring(organism, organism, int(list(population)[-1]+1))
                offspring(organism, organism, int(list(population)[-1]+1))
                offspring(organism, organism, int(list(population)[-1]+1))
                offspring(organism, organism, int(list(population)[-1]+1))
                offspring(organism, organism, int(list(population)[-1]+1))
                offspring(organism, organism, int(list(population)[-1]+1))
                offspring(organism, organism, int(list(population)[-1]+1))
                offspring(organism, organism, int(list(population)[-1]+1))
                offspring(organism, organism, int(list(population)[-1]+1))
                offspring(organism, organism, int(list(population)[-1]+1))
        except:
            continue
def restart():
    time=0
    for i in range(0,100):
        offspring(random.choice([0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,5,6,7,8,9,10,11,12,13,14,15,16]),random.choice([0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,5,6,7,8,9,10,11,12,13,14,15,16]),i)
    while len(population)>0:
        day()
        time+=1
    return time
def _max(_range):
    _max=0
    for i in range(0,_range):
        a = restart()
        if a>_max:
            _max=a
    return _max 
