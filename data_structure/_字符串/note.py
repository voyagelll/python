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
        while t[i + j] == p[j] and j < plen:
            j += 1
            if j == plen:
                return i
    return -1


# print(brute_force_match('123456', '456'))


def brute_force_match_(t, p):
    tlen = len(t)
    plen = len(p)
    for i in range(tlen):
        j = 0
        while j < plen and i + j < tlen and t[i + j] == p[j]:
            # i += 1
            j += 1
            if j == plen:
                return i
    return False


# print(brute_force_match_('123456', '4568'))


def brute_force_match__(t, p):
    tl = len(t)
    pl = len(p)

    for i in range(tl):
        j = 0
        while i+j<tl and t[i+j]==p[j]:
            j += 1
            if j==pl:
                return i
    return False

# print(brute_force_match__('12321', '32'))


# kmp算法
def get_failure_array(pattern):
    failure = [0]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = failure[i - 1]
            continue
        j += 1
        failure.append(i)
    return failure

# print(get_failure_array('123451245'))

def get_failure_array_(pattern):
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

# print(get_failure_array_('123451245'))


def get_failure_array__(l):
    failure = [0]
    i = 0
    j = 1
    while j < len(l):
        if l[i]==l[j]:
            i += 1
        elif i > 0:
            i = failure[i-1]
            continue
        j += 1
        failure.append(i)
    return failure

print(get_failure_array__('12312333'))



def kmp(pattern, text):
    failure = get_failure_array(pattern)
    i = 0
    j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            if j == (len(pattern) - 1):
                return i - len(pattern) + 1
            j += 1
        elif j > 0:
            j = failure[j - 1]
            continue
        i += 1
    return False


print(kmp('123', '333123'))

def kmp_(pattern, text):
    failure = get_failure_array_(pattern)
    i = 0
    j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            if j == (len(pattern)-1):
                return i - len(pattern)+1
            j += 1
        elif j > 0:
            j = failure[j-1]
            continue
        i += 1
    return False

print(kmp_('123', '333123'))






# 编辑距离
def levenshtein_distance(first_word, second_word):
    if len(first_word) < len(second_word):
        return levenshtein_distance(second_word, first_word)
    if len(second_word) == 0:
        return len(first_word)
    previous_row = range(len(second_word) + 1)
    # print(previous_row)
    for i, c1 in enumerate(first_word):
        current_row = [i + 1]
        for j, c2 in enumerate(second_word):
            # 计算增加，删除，修改次数
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            # 得到最小值，添加到current_row
            current_row.append(min(insertions, deletions, substitutions))
        # 存储previous_row
        previous_row = current_row
        print(current_row)
    # print(previous_row)
    return previous_row[-1]


# print(levenshtein_distance('planet', 'planetary'))
# print(levenshtein_distance('', 'test'))
# print(levenshtein_distance('book', 'back'))
# print(levenshtein_distance('book', 'book'))
# print(levenshtein_distance('test', ''))
# print(levenshtein_distance('', ''))
# print(levenshtein_distance('orchestration', 'container'))


"""
    字符串匹配：
        马拉车
"""


def manacher(s):
    s = '#' + '#'.join(s) + '#'
    # print(s)

    RL = [0] * len(s)
    MaxRight = 0
    pos = 0
    MaxLen = 0
    for i in range(len(s)):
        if i < MaxRight:
            RL[i] = min(RL[2 * pos - i], MaxRight - i)
        else:
            RL[i] = 1
        while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
            RL[i] += 1
        if RL[i] + i - 1 > MaxRight:
            MaxRight = RL[i] + i - 1
            pos = i
        MaxLen = max(MaxLen, RL[i])
    return MaxLen - 1


# print(manacher('1232111'))


def back_to_text_string(s):
    if s is None:
        return
    s = '#' + '#'.join(s) + '#'
    print(s)

    max_recur = []
    slen = len(s)
    if slen == 1:
        return
    elif slen == 3:
        max_recur.append(s.replace('#', ''))
    else:
        for i in range(slen):
            j = 0
            while i - j > 0 and i + j < slen and s[i - j] == s[i + j]:
                j += 1
            if j >= 1:
                max_recur.append(s[i - j + 1:i + j].replace('#', ''))
    return max_recur


# print(back_to_text_string('11223333221121'))


def manacher_(s):
    if s is None:
        return
    s = '#' + '#'.join(s) + '#'
    print(s)

    if len(s) == 2:
        return
    else:
        rl = []
        for i in range(len(s)):
            j = 0
            while i-j>0 and i+j<len(s) and s[i-j]==s[i+j]:
                j += 1
            if j > 2:
                rl.append(s[i-j+1:i+j])
    return rl


# print(manacher_('111232111'))

