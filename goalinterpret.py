class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        resp = ""
        while i < len(command):
            if command[i]=="G":
                resp+="G"
                i+=1
            if i+3 < len(command) and command[i:i+4]=="(al)":
                resp+="al"
                i+=4
            if i+1 < len(command) and command [i:i+2]=="()":
                resp+= "o"
                i+=2
        return resp
