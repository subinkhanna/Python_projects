import numpy as np

data = [1,2,3,4,5]

arr = np.array(data)

mean = np.mean(data)
print(mean)
std = np.std(data)
print(std)
z_score = [(x-mean)/std for x in data]

print(z_score)