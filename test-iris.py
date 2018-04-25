from sklearn import datasets
import matplotlib.pyplot as plt
iris = datasets.load_iris()

iris.data[:,1]
color = ('blue', 'green','pink')
data = iris.data

colort = []
for i in target:
    if i == 0:
        colort.append(color[0])
    if i == 1:
        colort.append(color[1])
    if i == 2:
        colort.append(color[2])

plt.scatter(data[:,0],data[:,1], marker='o', c = colort)
plt.scatter(data[:,2],data[:,3], marker='o', c = colort)