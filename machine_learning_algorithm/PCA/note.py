"""
	PCA(Principal Component Analysis) 主成分分析
	* 原理
		第一个坐标轴选择的是原始数据中方差最大的方向，
		第二个坐标轴选择的是和第一个坐标轴正交且具有最大方差的方向
		该做成一直重复，重复次数为特征数
		(大部分方差都包含在前面几个新坐标中)

	* 伪代码
		- 去除平均值
		- 计算协方差军阵
		- 计算协方差矩阵的特征值和特征向量
		- 将特征值从大到小排序
		- 保留最上面的 N 个特征向量
		- 将数据转换到上述 N 各特征向量构建新的空间中
"""
from numpy import * 
import matplotlib.pyplot as plt 



def loadDataSet(fileName, delim='\t'):
	fr = open(fileName)
	stringArr = [line.strip().split(delim) for line in fr.readlines()]
	dataArr = [list(map(float, line)) for line in stringArr]
	return mat(dataArr)


def pca(dataMat, topNfeat=9999):
	meanVals = mean(dataMat, axis=0)
	meanRemoved = dataMat - meanVals 
	covMat = cov(meanRemoved, rowvar=0)
	# print(covMat)
	eigVals, eigVects = linalg.eig(mat(covMat))
	print(eigVals)
	# print(eigVects)
	eigValInd = argsort(eigVals)
	print(eigValInd)
	eigValInd = eigValInd[: -(topNfeat+1): -1]
	print(eigValInd)
	redEigVects = eigVects[:, eigValInd]
	print(redEigVects)
	lowDDataMat = meanRemoved * redEigVects 
	# print(lowDDataMat)
	reconMat = (lowDDataMat * redEigVects.T) + meanVals 
	return lowDDataMat, reconMat 


dataMat = loadDataSet('testSet.txt')
lowDMat, reconMat = pca(dataMat, 1)
# print('lowDMat: ', lowDMat)
# print('reconMat: ', reconMat)
# 画图
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(dataMat[:, 0].flatten().A[0], dataMat[:, 1].flatten().A[0], marker='^', s=90)
# ax.scatter(reconMat[:, 0].flatten().A[0], reconMat[:, 1].flatten().A[0], marker='o', s=90)
# plt.show()


