import random

import scipy
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D

from matplotlib import pyplot as plt

xG1 = []
yG1 = []
xG2 = []
yG2 = []
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def euclidian(tup1, tup2):
    x = tup2[0] - tup1[0]
    y = tup2[1] - tup1[1]
    z = tup2[2] - tup1[2]
    return np.sqrt(x*x+y*y+z*z)


def getCentroid(subgroup, centroid):
    x = 0
    y = 0
    z = 0
    try:
        a = centroid[0]
        b = centroid[1]
        c = centroid[2]
        subgroup.append((a, b, c))
        for tup in subgroup:
            x += tup[0]
            y += tup[1]
            z += tup[2]
        n = len(subgroup)
        meanx = x/n
        meany = y/n
        meanz = z/n
        subgroup.remove((a,b,c))
        return (meanx, meany, meanz)
    except:
        for tup in subgroup:
            x += tup[0]
            y += tup[1]
            z += tup[2]
        n = len(subgroup)
        meanx = x/n
        meany = y/n
        meanz = z/n
        return (meanx, meany, meanz)


def genRandomPoints(n):
    ranPoints = []

    width1 = random.randint(50,200)
    width2 = random.randint(50, 200)
    rx1 = random.randint(0,1000)
    rx2 = random.randint(0,1000)
    ry1 = random.randint(0, 1000)
    ry2 = random.randint(0, 1000)
    for i in range(random.randint(40,100)):
        ranPoints.append((random.randint(rx1-width1,rx1+width1),random.randint(ry1-width1, ry1+width1)))

    for i in range(random.randint(40,100)):
        ranPoints.append((random.randint(rx2-width2,rx2+width2),random.randint(ry2-width2, ry2+width2)))
    for i in range(random.randint(1,15)):
        ranPoints.append((random.randint(0,1000),random.randint(0, 1000)))

    print('ranPoints = ', ranPoints)
    return ranPoints


def genRandomPoints3D(n):
    ranPoints = []

    width1 = random.randint(5, 15)
    width2 = random.randint(5, 15)
    rx1 = random.randint(0, 100)
    rx2 = random.randint(0, 100)
    ry1 = random.randint(0, 100)
    ry2 = random.randint(0, 100)
    rz1 = random.randint(0, 100)
    rz2 = random.randint(0, 100)
    for i in range(0, int(n/2)):
        ranPoints.append((random.randint(rx1,rx1+width1),random.randint(ry1, ry1+width1), random.randint(rz1, rz1+width1)))

    for i in range(0, int(n/2)):
        ranPoints.append((random.randint(rx2,rx2+width2),random.randint(ry2, ry2+width2), random.randint(rz2, rz2+width2)))
    #for i in range(0, 4):
    #    ranPoints.append((random.randint(0,100), random.randint(0,100), random.randint(0,100)))

    return ranPoints



def getCart(tupleList):
    x = []
    y = []
    z = []
    for tup in tupleList:
        x.append(tup[0])
        y.append(tup[1])
        z.append(tup[2])
    return x, y, z


def getFarthestPoints():
    distanceArray = []
    disArrayIndex = []
    for i in ranPoints:
        for j in ranPoints:
            if i == j:
                continue
            else:
                distanceArray.append(int(euclidian(i,j)))
                disArrayIndex.append((i,j))
    return (distanceArray, disArrayIndex)


#ranPoints = [(1.0, 1.0, 0), (1.5, 2.0, 3), (3.0, 4.0, 5), (5.0, 7.0,2), (3.5, 5.0, 8), (4.5, 5.0, 9), (3.5, 4.5, 2)]

ranPoints = genRandomPoints3D(12)

(x,y,z) = getCart(ranPoints)
(disArray, disArrayIndex) = getFarthestPoints()
(centroid1, centroid2) = disArrayIndex[disArray.index(max(disArray))]

group1 = []
group2 = []

print(centroid1)
print(centroid2)

# select group for point n1
# move centroid for chosen group
# select group for point n2
# move centroid for chosen group

for tup in ranPoints:
    g1comp = euclidian(centroid1, tup)
    g2comp = euclidian(centroid2, tup)
    if g1comp < g2comp:
        group1.append(tup)
        centroid1 = getCentroid(group1, centroid1)
        print("new centroid1: ", centroid1)
    else:
        group2.append(tup)
        centroid2 = getCentroid(group2, centroid2)
        print("new centroid2: ", centroid2)

# reallocation of groups 1 and 2
print("group 1: ", group1)
print("group 2: ", group2)


for tup in ranPoints:
    g1comp = euclidian(centroid1, tup)
    g2comp = euclidian(centroid2, tup)
    if (g1comp < g2comp) and (tup in group2):
        group1.append(tup)
        group2.remove(tup)
    elif (g2comp < g1comp) and (tup in group1):
        group2.append(tup)
        group1.remove(tup)


centroid1 = getCentroid(group1, None)
centroid2 = getCentroid(group2, None)



print(x)
print(y)
print(z)

#for i in range(0, len(x)-1):
#    ax.scatter(x[i], y[i], z[i])
ax.scatter(x[0], y[0], z[0], marker='o')
ax.scatter(x[1], y[1], z[1], marker='o')
ax.scatter(x[2], y[2], z[2], marker='o')
ax.scatter(x[3], y[3], z[3], marker='o')
ax.scatter(x[4], y[4], z[4], marker='o')
ax.scatter(x[5], y[5], z[5], marker='o')
ax.scatter(x[6], y[6], z[6], marker='o')
ax.scatter(x[7], y[7], z[7], marker='o')

ax.scatter(x[8], y[8], z[8], marker='o')
ax.scatter(x[9], y[9], z[9], marker='o')
ax.scatter(x[10], y[10], z[10], marker='o')
ax.scatter(x[11], y[11], z[11], marker='o')

ax.scatter(centroid1[0], centroid1[1], centroid1[2], marker='^')
ax.scatter(centroid2[0], centroid2[1], centroid2[2], marker='^')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()


