class Trie:

    def __init__(self):
        self.children = {}
        return
        
    def __match(self, word: str) -> tuple['Trie', str]:
        if not word:
            return self, ''
            
        child = self.children.get(word[0])
        if child is None:
            return self, word
        return child.__match(word[1:])
    

    def insert(self, word: str) -> None:
        node, remaining = self.__match(word)
        
        while remaining:
            ch = remaining[0]
            child = Trie()
            node.children[ch] = child

            node = child
            remaining = remaining[1:]
        
        node.children['EOS'] = Trie()

    def search(self, word: str) -> bool:
        node, remaining = self.__match(word)
        if remaining:
            return False
        return 'EOS' in node.children

    def startsWith(self, prefix: str) -> bool:
        _, remaining = self.__match(prefix)
        return not remaining


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
        

def main(cmd, param):
    print(f'Input: cmd = {cmd}')
    print(f'Input: param = {param}')
    

    trie = Trie()
    for i in range(len(cmd)):
        if i == 0:
            continue
        c = cmd[i]
        print(f'cmd={cmd[i]}, param={param[i]}')
        match c:
            case 'insert':
                o = trie.insert(param[i])
                print(o)
            case 'search':
                o = trie.search(param[i])
                print(o)
            case 'startsWith':
                o = trie.startsWith(param[i])
                print(o)




if __name__ == "__main__":
    cmd = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    param = ['', "apple", "apple", "app", "app", "app", "app"]

    cmd = ["Trie","insert","search","search","startsWith","insert","search"]
    param = ['',"apple","apple","app","app","app","app"]

   
    main(cmd, param)