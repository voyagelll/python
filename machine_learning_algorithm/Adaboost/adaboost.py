"""
    bagging （基于数据随机重抽样的分类器构建方法）
    * 是从源数据集选择 S 次后得到 S 个新数据集的一种技术。新数据集和源数据的大小相等。
    * 分类器权重相等

    boosting
    * 通过集中关注被已有分类器错分的哪些数据来获得新的分类器
    * 分类器权重不相等，每个权重代表的是其对应分类器在上一轮迭代中的成功度

    Adaboost 运行过程
        * 悬链数据中每个样本，并赋予权重，这些权重构成向量 D。
        * 开始是权重初始化为相等值。
        * 首先在训练数据上训练出一个弱分类器并计算该分类器的错误率，然后在同一数据集上再次训练弱分类器
        * 在分类器第二次训练中，将会调整每个样本的权重。其中对第一次分对的样本的权重将会降低，第一次分错的样本权重将会提高。

        为了从所有弱分类器中得到最终的分类结果，AdaBoost 为每个分类器分配了一个权重值 alpha，这些alpha是基于每个弱分类器的错误率进行的

        错误率 = 未正确分类的样本数据 / 所有样本的数目
        alpha =  (1/2)*ln((1-e)/e))

        计算出alpha 值之后，就可以对权重向量 D 进行更新。使得哪些正确分类样本的权重降低，错误分类的样本权重提高
            正确分类 D = (D*e^-alpha) / sum(D)
            错误分类 D = (D*e^alpha) / sum(D)
"""


"""
    基于单层决策树构建弱分类器
    * 伪代码
        将最小错误率minError设为 正无穷
        对数据集中的每一个特征（第一层循环）
            对每个补偿（第二层循环）
                对每个不等号（第三层循环）
                    建立一棵单层决策树并利用加权数据集对它进行测试
                    如果错误率低于minError， 则将当前单层决策树设为最佳单层决策树
        返回最佳单层决策树
"""
from numpy import *
import seaborn as sns
import matplotlib.pyplot as plt

def loadSimpleData():
    dataMat = mat([[1, 2.1],[2, 1.1],[1.3, 1.],[1, 1],[2, 1]])
    classLabels = [1, 1, -1, -1, 1]
    return dataMat, classLabels

# 单层决策树生成函数
def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    retArray = ones((shape(dataMatrix)[0], 1))
    if threshIneq == 'lt':
        retArray[dataMatrix[:, dimen] <= threshVal] = -1
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = -1
    return retArray


def buildStump(dataArr, classLabels, D):
    dataMatrix = mat(dataArr); labelMat = mat(classLabels).T
    m, n = shape(dataMatrix)
    numSteps = 10.0; bestStump={}; bestClasEst=mat(zeros((m,1)))
    minError = inf
    for i in range(n):
        rangeMin = dataMatrix[:,i].min();  rangeMax = dataMatrix[:,i].max()
        stepSize = (rangeMax - rangeMin) / numSteps
        for j in range(-1, int(numSteps)+1):
            for inequal in ['lt', 'gt']:
                threshVal = (rangeMin + float(j)*stepSize)
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)
                errArr = mat(ones((m, 1)))
                errArr[predictedVals == labelMat] = 0
                weightedError = D.T * errArr
                # print(i, threshVal, inequal, weightedError)
                # print('split: dim:%d, thresh:%.2f, inequal:%s, the weight error is:%.3f' % (i, threshVal, inequal, weightedError))
                if weightedError < minError:
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClasEst


# if __name__ == '__main__':
#     dataMat, labelMat = loadSimpleData()
#     D = mat(ones((5,1))/5)
#     bestStump, minError, bestClasEst = buildStump(dataMat, labelMat, D)
#     print(bestStump)
#     print(minError)
#     print(bestClasEst)

    # print(dataMat[:, 1].flatten().A[0])
    # sns.scatterplot(dataMat[:,0].flatten().A[0], dataMat[:,1].flatten().A[0])
    # plt.show()




"""
    完整Adaboost算法实现
    * 伪代码
        利用bulidStump 函数找到最佳的单层决策树
        将最佳单层决策树加入到单层决策树组
        计算 alpha
        计算新的权重向量 D
        更新累计类别估计值
        如果错误率等于0， 则退出循环
"""
def adaBoostTrainDS(dataArr, classLabels, numIt=40):
    weakClassArr = []
    m = shape(dataArr)[0]
    D = mat(ones((m,1))/m)
    aggClassEst = mat(zeros((m,1)))
    for i in range(numIt):
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)
        alpha = float(0.5 * log((1.0 - error) / max(error, 1e-16)))
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
        D = multiply(D, exp(expon))
        D = D / D.sum()
        aggClassEst += alpha * classEst
        print("aggClassEst: ", aggClassEst.T)
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggErrors.sum() / m
        print("total error:", errorRate)
        if errorRate == 0:
            break
    return weakClassArr, aggClassEst


if __name__ == '__main__':
    dataMat, classLabels = loadSimpleData()
    adaBoostTrainDS(dataMat, classLabels, 9)

