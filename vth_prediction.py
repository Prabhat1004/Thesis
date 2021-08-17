import numpy as np
import matplotlib.pyplot as plt

fhand = open(r"C:\Users\shatrunjay\Desktop\Thesis\ML Model\dataset1.csv", 'r')
data  = list()
count = 0
for line in fhand :
    if (count > 0) :
        temp = [float(item) for item in line.split(',')]
        data.append(temp)   
    count = count + 1

dataset_unscaled = np.array(data)

