"""
    字典树（Trie树）
        - 是一种树形结构，是哈希树的变种
        - 典型应用是用于统计，排序和保存大量的字符串
          经常被搜索引擎用于文本词频统计
          优点：利用字符串的公共前缀来减少查询时间，
        - 性质
            * 根节点不包含字符，除根节点外每个节点都只包含一个字符
            * 从根节点到某一节点，路径上经过的字符链接起来，为该节点对应的字符串
            * 每个节点的所有子节点包含的字符不相同
"""
class TrieNode:
    def __init__(self):
        self.nodes = dict()
        self.is_leaf = False

    def insert(self, word:str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def insert_many(self, words:[str]):
        for word in words:
            self.isnert(word)

    def search(self, word:str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf


