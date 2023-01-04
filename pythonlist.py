if __name__ == '__main__':
    N = int(input())
    li = []
    for i in range(N):
        input_ = input().split()
        
        if input_[0] == "insert" :
            li.insert(int(input_[1]), int(input_[2]))
            
        elif input_[0] == "remove":
            li.remove(int(input_[1]))
        elif input_[0] == "append":
            li.append(int(input_[1]))
        elif input_[0] == "print":
            print(li)
        elif input_[0] == "sort":
            li.sort()
        elif input_[0] == "reverse":
            li.reverse()
        elif input_[0] == "pop":
            li.pop()
