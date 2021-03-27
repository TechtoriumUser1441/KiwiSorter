import time
kiwiData = [1.57, 1.591, 1.604 ,1.61, 1.644, 1.652, 1.663, 1.67, 1.675, 1.679, 1.689, 1.68, 1.718, 1.758, 1.796, 1.809, 1.822,
1.824, 1.824, 1.825, 1.826, 1.831, 1.834, 1.836, 1.862, 1.878, 1.88, 1.882, 1.884, 1.886, 1.905, 1.916, 1.916, 1.921, 1.921,
1.923, 1.928, 1.93, 1.947, 1.948, 1.95, 1.951, 1.957, 1.959, 1.959, 1.96,1.965,1.97,1.971,1.979,1.984,1.987,1.996,1.999,2,
2.003,2.004,2.004,2.006, 2.008,2.009,2.009,2.01,2.011,2.014,2.014,2.016,2.017,2.018,2.021,2.022,2.026,2.028,2.029,2.033,2.033,2.041,2.044,2.044,2.045,2.049, 2.05,2.054,2.057,2.059,2.064,2.065,2.073,2.076,2.079,2.081,2.084,2.085,2.086,2.087,2.092,2.093,2.093,2.093,2.095,2.095,2.096,2.099, 2.101, 2.102,2.103,2.103,2.109,2.117,2.122,2.124,2.125,2.13,2.133,2.133,2.135]

def bSort(kiwiData): 
     x = len(kiwiData) 
     for i in range(x-1): 
         for j in range(0, x-i-1): 
             if kiwiData[j] > kiwiData[j+1] : 
                 kiwiData[j], kiwiData[j+1] = kiwiData[j+1], kiwiData[j] 
    
 bSort(kiwiData)

start_time = time.time()
for i in range(len(kiwiData)): 
     print (kiwiData[i])
print("Process took --- %s seconds ---" % (time.time() - start_time))

def sSort(kiwiData):
    x = len(kiwiData)
    for i in range(x):
        minimum = i
        for j in range(i+1, x):
            if (kiwiData[j] < kiwiData[minimum]):
                minimum = j

        temp = kiwiData[i]
        kiwiData[i] = kiwiData[minimum]
        kiwiData[minimum] = temp
    return kiwiData

start_time = time.time()
for i in range(len(kiwiData)): 
    print (kiwiData[i])
print("Process took --- %s seconds ---" % (time.time() - start_time))
