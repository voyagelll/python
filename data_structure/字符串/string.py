"""
    KMP算法
    * 算法原理
        将主串的第一个字符与模式串的第一字符进行匹配。如果相等，则一次比较主串和模式的下一个字符。
        如果不相等，则继续向后按之前方法匹配
"""
def string_match(s, p):
    for i in range(len(p)):
        print(s[i], p[i], s[i] != p[i], p)
        if s[i] != p[i]:
            return False
    return True


def kmp(s, p):
    for i,v in enumerate(s):
        if v == p[0]:
            res = string_match(s[i:], p)
            print(res)
            if res:
                return True
            else:
                continue
    return False


# print(kmp('123456456', '123456'))



"""
    编辑距离
"""
def levenshtein_distance(first_word, second_word):
    if len(first_word) < len(second_word):
        return levenshtein_distance(second_word, first_word)
    if len(second_word) == 0:
        return len(first_word)
    previous_row = range(len(second_word)+1)
    for i, c1 in enumerate(first_word):
        current_row = [i+1]
        for j, c2 in enumerate(second_word):
            insertions = previous_row[j+1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            print(insertions, deletions, substitutions)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


# levenshtein_distance('test', 'test')



"""
    最长回文字符串
"""

