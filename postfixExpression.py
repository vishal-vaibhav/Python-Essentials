"""
Program to show postfix expression
Stack works on LIFO
Algo:
1) Evaluate for each character in postfix expression
2) if Operand is encountered , Push into the Stack
3) if Operator is encountered, POP 2 characters from the stack which were already filled in the stack
    first =  top element from stack
    second = second element from the stack
4) check for operator & push into stack after operation
    second operator first
5) retrun top element from stack

"""


def eval_expression(arr):
    stack=[]
    operator=["+","-","*","/","%"]

    for item in arr:
        if item not in operator:
            stack.append((item))#push into stack
        else:
            first = int(stack.pop())#pop/pull from stack
            sec = int(stack.pop())

            if (item == "+"):
                stack.append(sec + first)

            if (item == "-"):
                stack.append(sec - first)

            if (item == "*"):
                stack.append(sec * first)

            if (item == "/"):
                stack.append(sec / first)

            if (item == "+"):
                stack.append(sec % first)
    return stack[-1]

a = ["2","1","+","3","*"] # expression to be evaluted

print(eval_expression(a)) # print output 9

