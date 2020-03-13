from random import seed
from random import randint
from random import randrange

import time
import multiprocessing

print("Number of processors: ", multiprocessing.cpu_count())



def population_simulation(num_families):
    girls = 0
    boys = 0
    for _ in range(0,num_families):
        girl_found = False
        while girl_found == False:
            num = randrange(2)
            if num == 1:
                girls += 1
                girl_found = True
            else:
                boys += 1
    
    print(boys, girls, boys/girls)

# starttime = time()

# population_simulation(100000)
# print('Time taken = {} seconds'.format(time() - starttime))



starttime = time.time()
pool = multiprocessing.Pool()
pool.map(population_simulation, range(1,10))
pool.close()

print('Time taken = {} seconds'.format(time.time() - starttime))