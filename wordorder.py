# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
words = []
for i in range(n):
    words.append(input())

count = []
i = 0
resp = ""

while i < len(words):
    c = words.count(words[i])
    count.append(c)
    resp+= str(c) +" "
    
    for j in range(c):
        words.remove(words[i])
        
print(len(count))
print(resp)
