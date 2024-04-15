for _ in range(int(input())):
    word=input()

    stack=[] 
    for w in word:
        if w=='(' or w=='[': 
            stack.append(w)
        elif w==')': 
            if len(stack)!=0 and stack[-1]=='(': 
                stack.pop()
            else: 
                stack.append(w)
        elif w==']':
            if len(stack)!=0 and stack[-1]=='[': 
                stack.pop()
            else:
                stack.append(w)

    if len(stack)==0:
        print('YES')
    else: 
        print('NO')