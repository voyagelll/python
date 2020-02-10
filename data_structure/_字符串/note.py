"""
	字符串
	- 两个字符串匹配
		- 暴力匹配
		- KMP
		
	- 编辑距离
		* 从一个字符串修改到里另一个字符串是，其中编辑单个字符需要修改的最少次数

	- 最长回文字符串
		- 暴力求解
		- 马拉车算法

"""

# 暴力匹配
def brute_force_match(t, p):
	tlen = len(t)
	plen = len(p)
	for i in range(tlen):
		j = 0 
		while t[i+j] == p[j] and j < plen:
			j += 1 
			if j == plen:
				return i 
	return -1  

# print(brute_force_match('123456', '456'))



# kmp算法
def get_failure_array(pattern):
	failure = [0]
	i = 0 
	j = 1 
	while j < len(pattern):
		if pattern[i] == pattern[j]:
			i += 1 
		elif i > 0:
			i = failure[i-1]
			continue 
		j += 1 
		failure.append(i)
	return failure 

# print(get_failure_array('123123'))


def kmp(pattern, text):
	failure = get_failure_array(pattern)
	i = 0 
	j = 0 
	while i < len(text):
		if pattern[j] == text[i]:
			if j == (len(pattern) - 1):
				return True
			j += 1
		elif j > 0:
			j = failure[j - 1]
			continue 
		i += 1
	return False 


# print(kmp('123456', '123123456'))



# 编辑距离 
def levenshtein_distance(first_word, second_word):
	if len(first_word) < len(second_word):
		return levenshtein_distance(second_word, first_word)
	if len(second_word) == 0:
		return len(first_word)
	previous_row = range(len(second_word) + 1)
	print(previous_row)
	for i, c1 in enumerate(first_word):
		current_row = [i+1]
		for j, c2 in enumerate(second_word):
			# 计算增加，删除，修改次数
			insertions = previous_row[j+1] + 1 
			deletions = current_row[j] + 1 
			substitutions = previous_row[j] + (c1 != c2)
			# 得到最小值，添加到current_row 
			current_row.append(min(insertions, deletions, substitutions))
		# 存储previous_row 
		previous_row = current_row 
		print(current_row)
	print(previous_row)
	return previous_row[-1]

# print(levenshtein_distance('planet', 'planetary'))
# print(levenshtein_distance('', 'test'))
# print(levenshtein_distance('book', 'back'))
# print(levenshtein_distance('book', 'book'))
# print(levenshtein_distance('test', ''))
# print(levenshtein_distance('', ''))
# print(levenshtein_distance('orchestration', 'container'))


# 最长回文字符串（暴力求解）
def back_to_text_string(s):
	slen = len(s)
	res = []
	res_dict = {}
	for i in range(1, slen-1):
		j = 1 
		while i-j>=0 and i+j<slen and s[i-j] == s[i+j]:
			j += 1 

		if j > 1:
			print(i, j)
			res.append(s[i-(j-1):i+j])
	return res 


print(back_to_text_string('1232111111'))