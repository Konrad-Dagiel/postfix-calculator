def postfix(s):
    sList=s.split(" ")
    stack=[]
    operators={'+':True, '-':True, '*':True, '/':True}
    for i in sList:
        if i not in operators:
            stack.append(int(i))
        else:
            try:
                operand_2=stack.pop()
                operand_1=stack.pop()
            except IndexError:
                return 'Invalid sequence'
            
            if i == '+':
                stack.append(operand_1+operand_2)
            elif i == '-':
                stack.append(operand_1-operand_2)
            elif i == '*':
                stack.append(operand_1*operand_2)
            elif i == '/':
                stack.append(operand_1/operand_2)
            else:
                return 'Invalid operand'
    return stack.pop()
        


if __name__=="__main__":
    s=input('Input postfix expression:')
    print(postfix(s))