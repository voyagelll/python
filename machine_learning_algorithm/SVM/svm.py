from numpy import * 
import seaborn as sns 
import matplotlib.pyplot as plt


# 读取数据
def loadDataSet(filename):
	dataMat = []
	labelMat = []
	fr = open(filename)
	for line in fr.readlines():
		lineArr = line.strip().split('\t')
		dataMat.append([float(lineArr[0]), float(lineArr[1])])
		labelMat.append(float(lineArr[2]))
	return dataMat, labelMat 


# 在 0-m 中随机选择一个不是 i 的数
def selectJrand(i, m):
	j = i 
	while (j==i):
		j = int(random.uniform(0, m))
	return j


# 保证 a 在L和H范围
def clipAlpha(aj, H, L):
	if aj > H:
		aj = H
	elif L > aj:
		aj = L
	return aj


# 和函数，输入参数：X， 支持向量的特征数：A， 某一行特征数据：kTup
def kernelTrans(X, A, kTup):
	m, n = shape(X)
	K = mat(zeros((m, 1)))
	if kTup[0] == 'lin':
		K = X * A.T
	elif KTup[0] == 'rbf':
		for j in range(m):
			deltaRow = X[j, :] - A
			K[j] = deltaRow * deltaRow.T
		K = exp(K/(-1*kTup[1]**2))
	else:
		raise NameError('Houston We Have a Problem -- That Kernel is not recognized')
	return K 


# 定义类，方便存储数据
class optStruct:
	def __init__(self, dataMatIn, classLabels, C, toler, kTup):
		self.X = dataMatIn                     # 数据
		self.labelMat = classLabels            # 数据类别
		self.C = C                             # 软家呢参数C， 参数越大，非线性拟合能力越强
		self.tol = toler                       # 停止阈值
		self.m = shape(dataMatIn)[0]           # 数据行数
		self.alphas = mat(zeros((self.m, 1)))  
		self.b = 0 	                           # 初始设为 0
		self.eCache = mat(zeros((self.m, 2)))  # 缓存
		self.K = mat(zeros((self.m, self.m)))  # 和函数计算结果
		for i in range(self.m):
			self.K[:, i] = kernelTrans(self.X, self.X[i, :], kTup)		


# 计算Ek
def calcEk(oS, k):
	fXk = float(multiply(oS.alphas,oS.labelMat).T*oS.K[:,k] + oS.b)
	Ek = fXk - float(oS.labelMat[k])
	return Ek 


# 随机选取 aj， 并返回其 E 值
def selectJ(i, oS, Ei):
	maxK = -1
	maxDeltaE = 0
	Ej = 0 
	oS.eCache[i] = [1, Ei]
	validEcacheList = nonzero(oS.eCache[:,0].A)[0]
	if (len(validEcacheList)) > 1:
		for k in validEcacheList:
			if k == i:
				continue
			Ek = calcEk(oS, k)
			deltaE = abs(Ei - Ek)
			if (deltaE > maxDeltaE):
				maxK = k 
				maxDeltaE = deltaE 
				Ej = Ek
		return maxK, Ej 
	else:
		j = selectJrand(i, oS.m)
		Ej = calcEk(oS, j)
	return j, Ej


# 更新 os 数据
def updateEk(oS, k):
	Ek = calcEk(oS, k)
	oS.eCache[k] = [1, Ek]


# 首先检验 ai 是否满足KKT条件，如果不满足，随机选择 aj 进行优化，更新ai，aj，b的值
def innerL(i, oS):        # 输入参数i 和所有参数数据
	Ei = calcEk(oS, i)    # 计算 E 值
	if ((oS.labelMat[i]*Ei < -oS.tol) and (oS.alphas[i] < oS.C)) \
		or ((oS.labelMat[i]*Ei > oS.tol) and (oS.alphas[i] > 0)):   # 检验这行数据是否符合KKT条件
		j, Ej = selectJ(i, oS, Ei)     # 随机选取 aj， 并返回其 E 值
		alphaIold = oS.alphas[i].copy()
		alphaJold = oS.alphas[j].copy()
		if (oS.labelMat[i] != oS.labelMat[j]):
			L = max(0, oS.alphas[j]-oS.alphas[i])
			H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
		else:
			L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
			H = min(oS.C, oS.alphas[j] + oS.alphas[i])
		if L == H:
			print("L == H")		
			return 0 
		eta = 2.0 * oS.K[i,j] - oS.K[i,i] - oS.K[j,j]
		if eta >= 0:
			print("eta >= 0")
			return 0 
		oS.alphas[j] -= oS.labelMat[j] * (Ei - Ej) / eta
		oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
		updateEk(oS, j)
		if (abs(oS.alphas[j] - alphaJold) < oS.tol):
			print("j not moving enough")
			return 0 
		oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] * (alphaJold - oS.alphas[j])
		updateEk(oS, i)
		b1 = oS.b - Ei - oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.K[i,i] - oS.labelMat[j]*(oS.alphas[j]-alphaJold)*oS.K[i,j]
		b2 = oS.b - Ej - oS.labelMat[i]*(oS.alphas[i]-alphaIold)*oS.K[i,j] - oS.labelMat[j]*(oS.alphas[j]-alphaJold)*oS.K[j,j]
		if (0 < oS.alphas[i] < oS.C):
			oS.b = b1
		elif (0 < oS.alphas[j] < oS.C):
			oS.b = b2 
		else:
			oS.b = (b1+b2) / 2.0
		return 1 
	else:
		return 0 


# SMO 函数，用于快速求解alpha
def smop(dataMatIn, classLabels, C, toler, maxIter, kTup=('lin', 0)):
	oS = optStruct(mat(dataMatIn), mat(classLabels).transpose(), C, toler, kTup)
	iter = 0 
	entireSet = True 
	alphaPairsChanged = 0 
	while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
		alphaPairsChanged = 0
		if entireSet:
			for i in range(oS.m):
				alphaPairsChanged += innerL(i, oS)
				print('fullSet, iter:%d, i:%d, pairs changed:%d' % (iter, i, alphaPairsChanged))
			iter += 1
		if entireSet:
			entireSe = False
		elif (alphaPairsChanged == 0):
			entireSet = True
		print('iteration number:%d' % iter)
	return oS.b, oS.alphas 


def testRbf(data_train, data_test):
	dataArr, labelArr = loadDataSet(data_train)
	b, alphas = smoP(dataArr, labelArr, 200, 0.0001, 10000, ('rbf', 1.3))
	dataMat = mat(dataArr)
	labelMat = mat(labelArr).transpose()
	svInd = nonzero(alphas)[0]
	sVs = dataMat[svInd]
	labelSV = labelMat[svInd]
	print("There are %d Suppoer vectors" % shape(sVs)[0])
	m, n = shape(dataMat)
	errorCount = 0 
	for i in range(m):
		kernelEval = kernelTrans(sVs, dataMat[i, :], ('rbf', 1.3))
		predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b 
		if sign(predict) != sign(labelArr[i]):
			errorCount += 1
	print("the training error rate is :%f" % (float(errorCount)/m))
	dataArr_test, labelArr_test = loadDataSet(data_test)
	errorCount_test = 0 
	datMat_test = mat(dataArr_test)
	labelMat = mat(labelArr_test).transpose()
	m, n = shape(dataMat_test)
	for i in range(m):
		kernelEval = kernelTrans(sVs, dataMat_test[i,:], ('rbf', 1.3))
		predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b 
		if sign(predict) != sign(labelArr_test[i]):
			errorCount_test += 1 
	print("the test error rate is: %f" % (float(errorCount_test) / m))


def main():
	filename = 'testSet.txt'
	dataMat, labelMat = loadDataSet(filename)
	b, alphas = smop(dataMat, labelMat, 200, 0.0001, 1000)
	# print(b)
	# print(alphas)
	x = []; y = []
	for i in range(len(alphas)):
		if alphas[i] > 0:
			x.append(dataMat[i][0])
			y.append(dataMat[i][1])
	print(x, y)
	# print([r[0] for r in dataMat])
	# print([r[1] for r in dataMat])
	# sns.scatterplot(dataMat)
	sns.scatterplot([r[0] for r in dataMat], [r[1] for r in dataMat])
	sns.scatterplot(x, y)
	plt.show()


if __name__ == '__main__':
	main()