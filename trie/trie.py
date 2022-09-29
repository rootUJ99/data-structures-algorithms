class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_endword = False 

class Trie:
    def __init__(self):
        self.root = TrieNode() 
       
    def _char_to_index(self, ch):
        return ord(ch)-ord("a")

    def _is_empty(self, children):
        for item in children:
            if item:
                return True
        return False

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

    def delete(self, key, node=None, depth=0):
        pass
        # ch = self._char_to_index(depth)
        # if depth ==0 and node == None: node=self.root
        
    

        # if depth == len(key)-1:
        #     pass
            

        # if depth != len(key) -1 and node.children[ch]:
        #     depth+=1
        #     self.delete(key, node.children[ch], depth)

        # if 

if __name__ == "__main__":
    t = Trie()

    arr = ["cat", "bat", "rat"]

    for i in arr:
        t.insert(i)
     
    print(t.search("bat"))