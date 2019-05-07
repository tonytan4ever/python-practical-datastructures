'''
Trie (prefix-tree) is a data structure supports word
search and word's prefix search by O(L) time, where L is the word's
length

Created on May 6, 2019

@author: tonytan4ever
'''


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word, cache_word=True):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        if cache_word:
            node.word = word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def is_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == '__main__':
    # (TODO): Add more tests here...
    pass
