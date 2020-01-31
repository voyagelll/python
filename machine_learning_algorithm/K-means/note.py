"""
	K 均值
	* 工作流程
		首先随机确定 k 各初始点作为质心。然后将数据集中的每个点分配到离自己最近的质心。
		每个簇的质心，更新为该簇所有点的平均值
"""
from numpy import * 
import matplotlib.pyplot as plt 


def loadDataSet(fileName):
	dataMat = []
	fr = open(fileName)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fltLine = map(float, curLine)
		dataMat.append(list(fltLine))
	return mat(dataMat)


def distEclud(vecA, vecB):
	return sqrt(sum(power(vecA-vecB, 2)))


def randCent(dataSet, k):
	n = shape(dataSet)[1]
	centroids = mat(zeros((k, n)))
	for j in range(n):
		minJ = min(dataSet[:, j])
		rangeJ = float(max(dataSet[:, j]) - minJ)
		centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
	return centroids


dataMat = loadDataSet('testSet2.txt')
centroids = randCent(dataMat, 2)
# print(centroids)
# print(distEclud(dataMat[0], dataMat[1]))


def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
	m = shape(dataSet)[0]
	clusterAssment = mat(zeros((m, 2)))
	centroids = createCent(dataSet, k)
	clusterChanged = True
	while clusterChanged:
		clusterChanged = False 
		for i in range(m):
			minDist =  inf; minIndex = -1 
			for j in range(k):
				distJI = distMeas(centroids[j, :], dataSet[i, :])
				# print(distJI, minDist)
				if distJI < minDist:
					minDist = distJI; minIndex = j 
			# print(clusterAssment[i, :], minIndex)
			if clusterAssment[i, 0] != minIndex: 
				clusterChanged = True 
			clusterAssment[i, :] = minIndex, minDist**2 
		# print(centroids)
		for cent in range(k):
			# print(nonzero(clusterAssment[:,0]==cent)[0])
			ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A==cent)[0]]
			centroids[cent, :] = mean(ptsInClust, axis=0)
	return centroids, clusterAssment 


# print(dataMat[:,1].flatten().A[0])
# centroids, clusterAssment = kMeans(dataMat, 3)
# print(centroids)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(dataMat[:,0].flatten().A[0], dataMat[:,1].flatten().A[0])
# ax.scatter(centroids[:,0].flatten().A[0], centroids[:,1].flatten().A[0])
# plt.show()



"""
	二分 K 均值算法                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             v
	* 原理：
		将所有点作为一个簇，然后将该簇一分为二。
		之后选择其中一个簇继续划分，选择哪个簇进行划分取决于对其划分是否可以最大程度降低SSE
		上述基于SSE的过程不断重复，直到得到用户指定的簇数目为止
"""
def biKmeans(dataSet, k, distMeas=distEclud):
	m = shape(dataSet)[0]
	clusterAssment = mat(zeros((m,2)))
	centroid0 = mean(dataSet, axis=0).tolist()[0]
	centList = [centroid0]
	for j in range(m):
		clusterAssment[j, 1] = distMeas(mat(centroid0), dataSet[j,:])**2
	while (len(centList) < k):
		lowestSSE = inf 
		for i in range(len(centList)):
			ptsInCurrCluster = dataSet[nonzero(clusterAssment[:,0].A == i)[0], :]
			centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)
			sseSplit = sum(splitClustAss[:, 1])
			sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:, 0].A != i)[0], 1])
			print('sseSplit, and not split: ', sseSplit, sseNotSplit)
			if (sseSplit + sseNotSplit) < lowestSSE:
				bestCentToSplit = i 
				bestNewCents = centroidMat 
				bestClustAss = splitClustAss.copy()
				lowestSSE = sseSplit + sseNotSplit 
		bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(centList)
		bestClustAss[nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentToSplit 
		print('The bestCentToSplit is :', bestCentToSplit)
		print('The len of bestClustAss is :', len(bestClustAss))
		centList[bestCentToSplit] = bestNewCents[0, :]
		centList.append(bestNewCents[1, :])
		clusterAssment[nonzero(clusterAssment[:, 0].A == bestCentToSplit)[0], :] = bestClustAss
	return centList, clusterAssment 



# dataMat = loadDataSet('testSet2.txt')
centList, myNewAssment = biKmeans(dataMat, 3)
print(centList)
# print(centList[:,0])
cents = array([c.flatten().A[0] for c in centList])
# print(array(centList)[:, 0][:, 0])
print(cents)
# 画图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:,0].flatten().A[0], dataMat[:,1].flatten().A[0])
ax.scatter(cents[:,0], cents[:,1], marker='x', c='red', s=500)
plt.show()
