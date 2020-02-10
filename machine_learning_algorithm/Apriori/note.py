"""
	Apriori算法
	- 原理： 
		如果某个项集是频繁的，那么它的所有子集也是频繁的
		如果某各项集是非频繁的，那么它的所有超集也是非频繁的

	- 支持度： 该数据集中包含该项集的比例
	- 置信度： P(B|A) = P(AB) / P(A)
	
	- 伪代码
		对数据集中的每条交易记录 tran
		对每个候选项集 can
			检查 can 是否是 tran 的自己
			如果是，则增加 can 的计数值 
		对每个候选项集
		如果其支持度不低于最小值，则保留该项集
		返回所有频繁项集
"""

def loadDataSet():
	return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

# 候选项集列表
def createC1(dataSet):
	C1 = []
	for transaction in dataSet:
		for item in transaction:
			if not [item] in C1:
				C1.append([item])
	C1.sort()
	return list(map(frozenset, C1))

# 返回满足支持度的项集列表，及所有项集和支持度的字典
def scanD(D, Ck, minSupport):
	ssCnt = {}
	for tid in D:
		tid = set(tid)
		for can in Ck:
			if can.issubset(tid):
				if not ssCnt.get(can, 0):
					ssCnt[can] = 1
				else:
					ssCnt[can] += 1 
	numItems = float(len(D))
	retList = []
	supportData = {}
	for key in ssCnt:
		support = ssCnt[key] / numItems 
		if support >= minSupport:
			retList.insert(0, key)
		supportData[key] = support 
	return retList, supportData 


dataSet = loadDataSet()
C1 = createC1(dataSet)
# print(C1)
# retList, supportData = scanD(dataSet, C1, 0.5)
# print(retList)
# print(supportData)


# Apriori 算法 (找出频繁项集)
def aprioriGen(Lk, k):
	retList = [] 
	lenLk = len(Lk)
	for i in range(lenLk):
		for j in range(i+1, lenLk):
			L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
			L1.sort(); L2.sort()
			if L1 == L2:
				retList.append(Lk[i] | Lk[j])
	return retList

# print(aprioriGen([frozenset({2}), frozenset({3}), frozenset({5})], 2))


def apriori(dataSet, minSupport=0.5):
	C1 = createC1(dataSet)
	D = list(map(set, dataSet))
	L1, supportData = scanD(D, C1, minSupport)
	L = [L1]
	k = 2 
	while (len(L[k-2]) > 2):
		Ck = aprioriGen(L[k-2], k)
		Lk, supK = scanD(D, Ck, minSupport)
		supportData.update(supK)
		L.append(Lk)
		k += 1 
	return L, supportData


L, supportData = apriori(dataSet, minSupport=0.7)
# print(L)
# print(supportData)



# 从频繁项集中挖掘关联规则
def generateRules(L, supportData, minConf=0.7):
	bigRuleList = []
	for i in range(1, len(L)):
		print('i: ', i)
		for freqSet in L[i]:
			H1 = [frozenset([item]) for item in freqSet] 
			if (i > 1):
				rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
			else:
				calcConf(freqSet, H1, supportData, bigRuleList, minConf)
	return bigRuleList 


# 对规则进行评估
def calcConf(freqSet, H, supportData, brl, minConf=0.7):
	prunedH = [] 
	for conseq in H:
		conf = supportData[freqSet] / supportData[freqSet-conseq]
		if conf >= minConf:
			print(freqSet-conseq, '-->', conseq, 'conf:', conf)
			brl.append((freqSet-conseq, conseq, conf))
			prunedH.append(conseq)
	return prunedH 

# 生成候选规则集合
def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
	m = len(H[0])
	print('freqset: ', freqSet, H)
	if (len(freqSet) > (m+1)):
		Hmp1 = aprioriGen(H, m+1)
		Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
		if (len(Hmp1) > 1):
			rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)


# L, supportData = apriori(dataSet, minSupport=0.5)
# print(L)
# print(supportData)
# rules = generateRules(L, supportData, minConf=0.5)
# print(rules)




"""
	示例：毒蘑菇的相似特征
"""
mushDataSet = [line.split() for line in open('mushroom.dat').readlines()]
# print(mushDataSet[0])
L, supportData = apriori(mushDataSet, minSupport=0.3)
# print(L)
# 索索包含特征 2 的频繁项集
for item in L[1]:
	if item.intersection('2'):
		print(item)