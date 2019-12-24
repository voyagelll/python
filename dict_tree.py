"""
    字典树
    是哈希树的变种，主要用于统计，排序和保存大量的字符串（不仅限于字符串）。
    经常用于所有引擎系统文本词频统计。

    优点：利用字符串的公共前缀减少查询时间，最大限度减少无谓的字符串比较，查询效率比哈希树高

    性质：
        1、根节点不包含字符，除根节点外每一个节点都只包含一个字符
        2、从根节点到某一节点，路径上经过的字符连接起来，为改节点对应的字符串
        3、每个节点的所有子节点包含的字符都不相同
"""


class TrieNode:
    def __init__(self):
        self.nodes = dict()
        self.is_leaf = False

    def insert(self, word: str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def insert_many(self, words: [str]):
        for word in words:
            self.insert(word)

    def search(self, word: str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf


if __name__ == '__main__':
    t = TrieNode()
    print(t.is_leaf)

    # t.insert
