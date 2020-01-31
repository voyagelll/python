from numpy import * 
import matplotlib.pyplot as plt 

# 加载数据
def loadDataSet(fileName):
	numFeat = len(open(fileName).readline().split('\t')) - 1
	dataMat = []; labelMat = []
	fr = open(fileName)
	for line in fr.readlines():
		lineArr = []
		curLine = line.strip().split('\t')
		for i in range(numFeat):
			lineArr.append(float(curLine[i]))
		dataMat.append(lineArr)
		labelMat.append(float(curLine[-1]))
	return dataMat, labelMat 


# 计算最佳拟合直线
def standRegress(xArr, yArr):
	xMat = mat(xArr); yMat = mat(yArr).T
	xTx = xMat.T * xMat 
	if linalg.det(xTx) == 0:
		print('The matrix is singular, cannot do inverse')
		return 
	ws = xTx.I * (xMat.T * yMat)
	return ws 


# xArr, yArr = loadDataSet('ex0.txt')
# w = standRegress(xArr, yArr)
# print(w)

# 画图
# xMat = mat(xArr)
# yMat = mat(yArr)
# yHat = xMat * w
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])

# xCopy = xMat.copy()
# xCopy.sort(0)
# print(xCopy)
# print(w)
# yHat = xCopy * w 
# ax.plot(xCopy[:,1], yHat)
# plt.show()


# 判断模型的好坏
# model_rate = corrcoef((xMat*w).T, yMat)
# print('model rate:', model_rate)




"""
	局部加权线性回归（Locally Weighted Linear Regression) LWLR
	* 在算法中给待预测点附近的每个点赋予一定的权重
		w = (X.T * W * X).I * X.T * y
"""

# 局部加权线性回归
def lwlr(testPoint, xArr, yArr, k=1.0):
	xMat = mat(xArr); yMat = mat(yArr).T 
	m = shape(xMat)[0]
	weights = mat(eye((m)))
	for j in range(m):
		diffMat = testPoint - xMat[j, :]
		weights[j, j] = exp(diffMat*diffMat.T / (-2*k**2))    # 高斯核 
	xTx = xMat.T * (weights*xMat)
	if linalg.det(xTx) == 0:
		print('The matrix is singular, cannot do inverse')
		return 
	ws = xTx.I * (xMat.T * (weights * yMat))
	return testPoint * ws 


def lwlrTest(testArr, xArr, yArr, k=1.0):
	m = shape(testArr)[0]
	yHat = zeros(m)
	for i in range(m):
		yHat[i] = lwlr(testArr[i], xArr, yArr, k)
	return yHat 


# xArr, yArr = loadDataSet('ex0.txt')
# res = lwlr(xArr[0], xArr, yArr, 1.0)
# print('Raw data:%s,  prediction:%s' % (yArr[0], res))

# # 画图
# xMat = mat(xArr)
# yHat = lwlrTest(xArr, xArr, yArr, 0.03)
# srtInd = xMat[:,1].argsort(0)
# xSort = xMat[srtInd][:, 0, :]
# # print(xSort)
# # print(yHat)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(xSort[:,1], yHat[srtInd])
# ax.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0], s=2, c='red')
# plt.show()



"""
	岭回归
	w = (X.T*X + lambda*I).I * X.T * y 
"""
def ridgeRegres(xMat, yMat, lam=0.2):
	xTx = xMat.T*xMat 
	# print(xTx.shape)
	denom = xTx + eye(shape(xMat)[1])*lam 
	if linalg.det(denom) == 0:
		print('The matrix is singular, cannot do inverse')
		return 
	ws = denom.I * (xMat.T*yMat)
	return ws 


def ridgeTest(xArr, yArr):
	xMat=mat(xArr); yMat=mat(yArr).T 
	yMean = mean(yMat, 0)
	yMat = yMat - yMean 
	xMeans = mean(xMat, 0)
	xVar = var(xMat, 0)
	xMat = (xMat - xMeans) / xVar 
	numTestPts = 30
	wMat = zeros((numTestPts, shape(xMat)[1]))
	for i in range(numTestPts):
		# print(xMat.shape)
		ws = ridgeRegres(xMat, yMat, exp(i-10))
		wMat[i, :] = ws.T 
	return wMat 


# xArr, yArr = loadDataSet('abalone.txt')
# wMat = ridgeTest(xArr, yArr)
# print(wMat)

# # 画图
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(wMat)
# plt.show()



"""
	前向逐步回归
"""
def stageWise(xArr, yArr, eps=0.01, numIt=100):
	xMat = mat(xArr); yMat=mat(yArr).T 
	yMean = mean(yMat, 0)
	yMat = yMat - yMean 
	xMeans = mean(xMat, 0)
	xVar = var(xMat, 0)
	xMat = (xMat - xMeans) / xVar
	m, n = shape(xMat)
	returnMat = zeros((numIt, n))
	ws = zeros((n,1)); wsTest = ws.copy(); wsMax = ws.copy()
	for i in range(numIt):
		print(ws.T)
		lowestError = inf
		for j in range(n):
			for sign in [-1, 1]:
				wsTest = ws.copy()
				wsTest[j] += eps * sign 
				yTest = xMat * wsTest 
				rssE = rssError(yMat.A, yTest.A)
				if rssE < lowestError:
					lowestError = rssE 
					wsMax = wsTest 
		ws = wsMax.copy()
		returnMat[i, :] = ws.T 
	return returnMat 


def rssError(yArr, yHatArr):
	return ((yArr - yHatArr) ** 2).sum()


xArr, yArr = loadDataSet('abalone.txt')
res = stageWise(xArr, yArr, 0.01, 200)
print('Res: ', res)




