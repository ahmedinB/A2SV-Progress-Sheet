class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        resp = ""
        while i < len(command):
            if command[i]=="G":
                resp+="G"
                i+=1
            elif i+3 < len(command) and command[i:i+4]=="(al)":
                resp+="al"
                i+=4
            elif i+1 < len(command) and command [i:i+2]=="()":
                resp+= "o"
                i+=2
            print(resp, i+4 < len(command))
        return resp


S = Solution()
print(S.interpret("G()(al)"))
print(S.interpret("G()()()()(al)"))
print(S.interpret("(al)G(al)()()G"))
print(S.interpret("GG()"))
