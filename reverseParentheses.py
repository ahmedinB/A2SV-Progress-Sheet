def reverseParentheses(s):
    opened = []
    pair = {}
    for i, c in enumerate(s):
        if c == '(':
            opened.append(i)
        if c == ')':
            j = opened.pop()
            pair[i], pair[j] = j, i
    print(pair)
    res = []
    i, d = 0, 1
    while i < len(s):
        if s[i] in '()':
            i = pair[i]
            d = -d
        else:
            res.append(s[i])
        i += d
    return ''.join(res)
print(reverseParentheses("(ed(et(oc))el)"))
print(reverseParentheses("a(bcdefghijkl(mno)p)q"))
# leetcode
# apmnolkjihgfedcbq