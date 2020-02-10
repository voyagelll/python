"""
	Adaboost（Adaptive boosting）

	- 运行过程
		* 一开始权重初始化为相同的值，在训练数据上训练一个弱分类器的错误率，然后在同一数据集上再次训练弱分类器。在
		  分类器第二次训练当中，将会重新调整权重，其中第一次分队的样本权重将会降低，第一次分错的样本权重将会提高。
		* 训练数据中每个样本，并赋予权重 alpha，这些权重构成了向量D。 
			- alpha 由错误率(epsilon) = 未正确分类的样本数 / 所有样本数
			  alpha = (1/2)ln((1-e)/e)

			- 更新权向量
				正确分类 D = (D*e(-alpha))/ sum(D)
				错误分类 D = (D*e(alpha)) / sum(D)


	- 集成算法
		- bagging(bootstrap aggregating) 自举汇聚法
			- 通过原始数据集构建 S 各数据集，对 S 个数据集应用分类算法。
			  选择 S个分类器结果中类别多的作为结果

		- boosting
			- 每个新分类器都根据已训练的分类器的性能来进行训练。
			  集中关注错分的数据来获得新的分类器


	- 分类性能指标
		- 精确率 TP/(TP+FP)：预测为正例的样本中真正正例的比例 
		- 召回率 TP/(TP+FN)：预测为正例的真实正例占所有正例的比例 
	
"""



"""	
	- 单层决策树伪代码
		* 将最小错误率 minError 设为 +inf
		* 对数据集中的每一个特征
			* 对每个步长
				* 对每个不等号
					* 建立一棵单层决策树并利用加权数据集对它进行测试
					* 如果错误率低于 minError, 则将当前单层决策树设为最佳单层决策树
		* 返回最佳单层决策树
"""
from numpy import * 
import seaborn as sns
import matplotlib.pyplot as plt 


def loadSimpleData():
    dataMat = mat([[1, 2.1],[2, 1.1],[1.3, 1.],[1, 1],[2, 1]])
    classLabels = [1, 1, -1, -1, 1]
    return dataMat, classLabels


# 基于单层决策树构建弱分类器
def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
	retArray = ones((shape(dataMatrix)[0], 1))
	if threshIneq == 'lt':
		retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
	else:
		retArray[dataMatrix[:, dimen] > threshVal] = -1.0 
	return retArray 


def buildStump(dataArr, classLabels, D):
	dataMatrix = mat(dataArr); labelMat = mat(classLabels).T 
	m, n = shape(dataMatrix)
	numSteps = 10.0; bestStump = {}; bestClasEst = mat(zeros((m,1)))
	minError = inf 
	for i in range(n):
		rangeMin = dataMatrix[:,i].min(); rangeMax = dataMatrix[:,i].max()
		stepSize = (rangeMax - rangeMin) / numSteps 
		for j in range(-1, int(numSteps)+1):
			for inequal in ['lt', 'gt']:
				threshVal = (rangeMin + float(j)*stepSize)
				predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)
				errArr = mat(ones((m, 1)))
				errArr[predictedVals == labelMat] = 0 
				weightedError = D.T * errArr 
				# print('split: dim:%d, thresh:%.2f, inequal:%s, the weight error is:%.3f' % (i, threshVal, inequal, weightedError))
				if weightedError < minError:
					minError = weightedError 
					bestClasEst = predictedVals.copy()
					bestStump['dim'] = i 
					bestStump['thresh'] = threshVal 
					bestStump['ineq'] = inequal
	return bestStump, minError, bestClasEst 


dataMat, labelMat = loadSimpleData()
D = mat(ones((5, 1)) / 5)
# bestStump, minError, bestClasEst = buildStump(dataMat, labelMat, D)
# print('bestStump: ', bestStump)
# print('minError: ', minError)
# print('bestClasEst: ', bestClasEst)



"""
	完整 Adaboost 算法实现
	- 对每次迭代
		利用 buildStump 函数找到最佳的单层决策树
		将最佳单层决策树加入到单层决策树数组中
		计算 alpha 
		计算新的权重向量
		更新累计类别估计值
		如果错误率等于 0，则推出循环
"""
def adaBoostTrainDS(dataArr, classLabels, numIt=40):
	weakClassArr = []
	m = shape(dataArr)[0] 
	D = mat(ones((m, 1)) / m)
	aggClassEst = mat(zeros((m, 1)))
	for i in range(numIt):
		bestStump, error, classEst = buildStump(dataArr, classLabels, D)
		alpha = float(0.5 * log((1.0-error)/max(error,1e-16)))
		bestStump['alpha'] = alpha 
		weakClassArr.append(bestStump)
		expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
		D = multiply(D, exp(expon))
		D = D / D.sum()
		aggClassEst += alpha * classEst 
		print('aggClassEst: ', aggClassEst.T)
		aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m,1)))
		errorRate = aggErrors.sum() / m 
		print('total error: ', errorRate)
		if errorRate == 0:
			break
	return weakClassArr 


adaBoostTrainDS(dataMat, labelMat, 9)
