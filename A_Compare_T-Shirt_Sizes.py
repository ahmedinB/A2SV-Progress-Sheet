n = int(input())
for n_ in range(n):
    tshirtsize = input().split()
    if tshirtsize[0][-1] == "M" and tshirtsize[1][-1] == "S":
        print(">")
    elif tshirtsize[0][-1] == "S" and tshirtsize[1][-1] == "M":
        print("<")
    elif tshirtsize[0][-1] == "M" and tshirtsize[1][-1] == "L":
        print("<")
    elif tshirtsize[0][-1] == "L" and tshirtsize[1][-1] == "M":
        print(">")
    elif tshirtsize[0][-1] == "L" and tshirtsize[1][-1] == "S":
        print(">")
    elif tshirtsize[0][-1] == "S" and tshirtsize[1][-1] == "L":
        print("<")

    elif tshirtsize[0][-1] == "S" and tshirtsize[1][-1] == "S":
        if len(tshirtsize[0]) > len(tshirtsize[1]):
            print("<")
        elif len(tshirtsize[0]) < len(tshirtsize[1]):
            print(">")
        else:
            print("=")

    elif tshirtsize[0][-1] == "L" and tshirtsize[1][-1] == "L":
        if len(tshirtsize[0]) > len(tshirtsize[1]):
            print(">")
        elif len(tshirtsize[0]) < len(tshirtsize[1]):
            print("<")
        else:
            print("=")
    elif  tshirtsize[0][-1] == "M" and tshirtsize[1][-1] == "M":
        print("=")