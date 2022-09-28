class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_endword = False 

class Trie:
    def __init__(self):
        self.root = TrieNode() 
       
    def _char_to_index(self, ch):
        return ord(ch)-ord("a")

    def insert(self, key):
        node = self.root
        for i in key:
            ch = self._char_to_index(i)
            if not ch in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_endword = True

    def search(self, key):
        node = self.root
        for i in key:
            ch = self._char_to_index(i)
            if not node.children:
                return False
            node = node.children[ch]
        return node.is_endword


if __name__ == "__main__":
    t = Trie()

    arr = ["cat", "bat", "rat"]

    for i in arr:
        t.insert(i)
     
    print(t.search("bat"))