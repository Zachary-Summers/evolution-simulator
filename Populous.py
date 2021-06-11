import random, decimal, sys
import matplotlib.pyplot as plt
population = {}
length = []
def offspring(parent1,parent2,identifier):
    child_start = random.choice([parent1,parent2])
    mutate = random.choice([1,1,1,1,1,1,1,1,1, 1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,6,6,6,7,7,8,8,9,10,0])
    if mutate == 0:
        child_trait = float(child_start)
    elif mutate == 1:
        child_trait = (child_start+(random.random()/2))/2+1
    elif mutate == 2:
        child_trait = (child_start+(random.random()))/2+1
    elif mutate == 3:
        child_trait = (child_start+(random.random()*1.25))/2+1
    elif mutate == 4:
        child_trait = (child_start+(random.random()*1.5))/2+1
    elif mutate ==5:
        child_trait = (child_start+(random.random()*1.75))/2
    elif mutate == 6:
        child_trait = (child_start+(random.random()*2.00))/2
    elif mutate == 7:
        child_trait = (child_start+(random.random()*2.5))/2
    elif mutate == 8:
        child_trait = (child_start+(random.random()*3.5))/2
    elif mutate == 9:
        child_trait = (child_start+(random.random()*4))/2
    elif mutate == 10:
        child_trait = (child_start+(random.random()*6))/2
    population[f'{identifier}']=child_trait
dead=0
def day():
    global dead
    for i in range(0,int(list(population)[-1])+1):
        try:
            organism = population[str(i)]
            if len(population)>50:
                if round(organism) == 2:
                    survive = random.choice([True,True,True,True,False,False,False])
                if round(organism) != 2:
                    survive = random.choice([False, False, False,False,True, True])
                reproduce = random.choice([1,0])
                if survive != True:
                    del population[str(i)]
                    dead+=1
                if len(population) > 1000:
                    if random.choice([True,True,True,True,True,True,False,False]):
                        del population[str(i)]
                        dead+=1
                if len(population) > 500 and round(organism) != (2 or 3 or 1):
                    if random.choice([True,True,False,False,False,False,False,False,False,False,False]):
                        del population[str(i)]
                        dead+=1
                if organism >=7:
                    del population[str(i)]
                    dead+=1
                if reproduce:
                    offspring(organism,organism,int(list(population)[-1])+1)
            else:
                if not random.choice([1,1,1,1,1,1,1,0]):
                    del population[str(i)]
                    dead+=1
                offspring(organism,organism,int(list(population)[-1])+1)
        except:
            continue
def restart(population):
     for i in range(0,population):
        offspring(random.choice([0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,5,6,7,8,9,10,11,12,13,14,15,16]),random.choice([0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,5,6,7,8,9,10,11,12,13,14,15,16]),i)
def trial():
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
        a = trial()
        if a>_max:
            _max=a
    return _max
def go(_range,pop):
    offspring(random.choice([0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,5,6,7,8,9,10,11,12,13,14,15,16]),random.choice([0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,5,6,7,8,9,10,11,12,13,14,15,16]),-1)
    restart(pop)
    for i in range(0,_range):
        length.append(int(len(population)))
        day()
        quotient = decimal.Decimal(len(length)/_range)
        percent = quotient*100
        print(str(round(percent,2))+"%")
    length.reverse()
    y=length
    y.reverse()
    x = []
    a=0
    plt.title('Population Of Species Over Time')
    plt.xlabel("Time")
    plt.ylabel("Population")
    for i in length:
        a+=1
        x.append(a)
    plt.plot(x,y)
    plt.show()
    length.clear()
    population.clear()
    print(str(dead)+" organisms died")
