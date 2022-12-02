def isValid(s):
    op = "{[("
    clo = "}])"
    brackets = {')':'(','}':'{',']':'['}
    stack= []
    for char in s:
        if char in op:
            stack.append(char)
        elif char in clo:
            if len(stack)==0:
                return False
            if stack[-1]==brackets[char]:
                stack.pop()
            else:
                return False
    return len(stack)==0
s = input()
print(isValid(s))