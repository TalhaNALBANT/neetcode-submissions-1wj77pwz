class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        myHash = { "}" : "{", "]" : "[", ")" : "("}

        for c in s:
            if c in myHash:
                if myStack and myStack[-1] == myHash[c]:
                    myStack.pop()
                else:
                    return False
            else:        
                 myStack.append(c)    
        return True if not myStack else False