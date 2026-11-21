class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.rootNode = Node()

    def addWord(self, word: str) -> None:
        current = self.rootNode

        for char in word:
            if char not in current.children:
                current.children[char] = Node()

            current = current.children[char]

        current.is_end = True

    def search(self, word: str) -> bool:

        def dfs(node, index):

            if index == len(word):
                return node.is_end

            char = word[index]

            if char == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False

            if char not in node.children:
                return False

            return dfs(node.children[char], index + 1)

        return dfs(self.rootNode, 0)