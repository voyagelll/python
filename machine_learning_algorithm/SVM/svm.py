"""
	简版 svm(smo)实现
"""
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


# 在0-m中随机选择一个不是i的整数
def selectJrand(i, m):
    j = i
    while (j==i):
        j = int(random.uniform(0, m))
    return j


# 保证a在L和H范围内（L <= a <= H)
def clipAlpha(aj, H, L):
    if aj>H:
        aj = H
    if L>aj:
        aj=L
    return aj


# 简化版SMO算法
def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn); labelMat = mat(classLabels).transpose()
    b = 0
    m, n = shape(dataMatrix)
    alphas = mat(zeros((m, 1)))
    iter = 0
    while (iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas, labelMat).T * (dataMatrix*dataMatrix[i, :].T)) + b
            Ei = fXi - float(labelMat[i])
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):
                j = selectJrand(i, m)
                fXj = float(multiply(alphas, labelMat).T * (dataMatrix*dataMatrix[j, :].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                # 保证alpha 在 0-C之间
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    print("L == H")
                    continue
                eta = 2.0 * dataMatrix[i,:] * dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0:
                    print("eta >= 0")
                    continue
                # 对i进行修改，对j进行修改但方向相反
                alphas[j] -= labelMat[j] * (Ei - Ej) / eta
                alphas[j] = clipAlpha(alphas[j], H, L)
                if (abs(alphas[j] - alphaJold) < 0.00001):
                    print("J is not moving enough")
                    continue
                alphas[i] += labelMat[j] * labelMat[i] * (alphaJold - alphas[j])
                b1 = b - Ei - labelMat[i] * (alphas[i]-alphaIold) * dataMatrix[i,:] * dataMatrix[i,:].T -\
                    labelMat[j]*(alphas[j]-alphaJold) * dataMatrix[i,:] * dataMatrix[j, :].T
                b2 = b - Ej - labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T -\
                    labelMat[j] * (alphas[j]-alphaJold) * dataMatrix[j,:] * dataMatrix[j,:].T
                if (0 < alphas[i]) and (C > alphas[i]):
                    b = b1
                elif (0 < alphas[j]) and (C > alphas[j]):
                    b = b2
                else:
                    b = (b1+b2) / 2
                alphaPairsChanged += 1
                print("iter: %d,   i:%d,  pairs changed %d" % (iter, i , alphaPairsChanged))
        if (alphaPairsChanged == 0):
            iter += 1
        else:
            iter = 0
        print("iteration number : %d" % iter)
    return b, alphas


# if __name__ == "__main__":

#     dataArr, labelArr = loadDataSet('testSet.txt')
#     print(mat(dataArr)[:, 0].flatten().A[0])

#     b, alphas = smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
#     print(b)
#     # print(alphas[alphas>0])
#     x = []; y= []
#     for i in range(100):
#         if alphas[i]>0:
#             print(dataArr[i], labelArr[i])
#             x.append(dataArr[i][0])
#             y.append(dataArr[i][1])

#     sns.scatterplot(mat(dataArr)[:, 0].flatten().A[0], mat(dataArr)[:, 1].flatten().A[0])
#     sns.scatterplot(x, y, markers='+')
#     plt.show()






"""
	完整版
"""
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
	elif kTup[0] == 'rbf':
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


def testRbf(data_train, data_test, k=1.3):
	dataArr, labelArr = loadDataSet(data_train)
	b, alphas = smop(dataArr, labelArr, 200, 0.0001, 100, ('rbf', k))
	dataMat = mat(dataArr)
	labelMat = mat(labelArr).transpose()
	svInd = nonzero(alphas)[0]
	sVs = dataMat[svInd]
	labelSV = labelMat[svInd]
	print("There are %d Suppoer vectors" % shape(sVs)[0])
	m, n = shape(dataMat)
	errorCount = 0 
	for i in range(m):
		kernelEval = kernelTrans(sVs, dataMat[i, :], ('rbf', k))
		predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b 
		if sign(predict) != sign(labelArr[i]):
			errorCount += 1
	print("the training error rate is :%f" % (float(errorCount)/m))
	dataArr_test, labelArr_test = loadDataSet(data_test)
	errorCount_test = 0 
	dataMat_test = mat(dataArr_test)
	labelMat = mat(labelArr_test).transpose()
	m, n = shape(dataMat_test)
	for i in range(m):
		kernelEval = kernelTrans(sVs, dataMat_test[i,:], ('rbf', k))
		predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b 
		if sign(predict) != sign(labelArr_test[i]):
			errorCount_test += 1 
	print("the test error rate is: %f" % (float(errorCount_test) / m))



def calcWs(alphas, dataArr, classLabels):
	X = mat(dataArr); labelMat = mat(classLabels).transpose()
	m, n = shape(X)
	w = zeros((n,1))
	for i in range(m):
		w += multiply(alphas[i] * labelMat[i], X[i,:].T)
	return w 


def main():
	filename = 'testSetRBF.txt'
	dataMat, labelMat = loadDataSet(filename)
	b, alphas = smop(dataMat, labelMat, 200, 0.0001, 110, ('rbf', 1.3))
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
	# testRbf('testSetRBF.txt', 'testSetRBF2.txt')