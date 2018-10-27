
import random

import scipy
import numpy as np
import random


from matplotlib import pyplot as plt

xG1 = []
yG1 = []
xG2 = []
yG2 = []


def euclidian(tup1, tup2, tup3=None):
    x = tup2[0] - tup1[0]
    y = tup2[1] - tup1[1]
    try:
        z = tup3[3] - tup3[3]
    except:
        z = 0
    return np.sqrt(x*x+y*y+z*z)

def getCentroid(subgroup, centroid):
    x = 0
    y = 0
    try:
        a = centroid[0]
        b = centroid[1]
        subgroup.append((a,b))
        for tup in subgroup:
            x += tup[0]
            y += tup[1]
        n = len(subgroup)
        meanx = x/n
        meany = y/n
        subgroup.remove((a,b))
        return (meanx, meany)
    except:
        for tup in subgroup:
            x += tup[0]
            y += tup[1]
        n = len(subgroup)
        meanx = x/n
        meany = y/n
        return (meanx, meany)



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

def getCart(tupleList):
    x = []
    y = []
    for tup in tupleList:
        x.append(tup[0])
        y.append(tup[1])
    return x,y

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


#  ranPoints = [(1.0, 1.0), (1.5, 2.0), (3.0, 4.0), (5.0, 7.0), (3.5, 5.0), (4.5, 5.0), (3.5, 4.5)]
ranPoints = genRandomPoints(100)

(x,y) = getCart(ranPoints)

(disArray, disArrayIndex) = getFarthestPoints()




print(max(disArray))
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




for tup in group1:
        xG1.append(tup[0])
        yG1.append(tup[1])

for tup in group2:
    xG2.append(tup[0])
    yG2.append(tup[1])



plt.plot(x,y, 'o')
plt.plot((centroid1[0], centroid2[0]),(centroid1[1], centroid2[1]), 'xr')
plt.hold
plt.pause(2)

plt.plot(xG1, yG1, 'or')
plt.plot(xG2, yG2, 'om')

plt.show()


