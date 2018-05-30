# -*- coding: utf-8 -*-

rpn = "1 3 + 9 2 - *"  # (1 + 3) * (9 - 2)


def RPN(states):
    
    operator = {
        "+": (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: float(x) / y)
    }

    stack = []
    print("RPN: %s" % states)

    _states = states.replace(" ", "")
    
    for index, z in enumerate(_states):
        if index > 0:
            print(stack)
        if z not in operator.keys():
            stack.append(int(z))
            continue

        y = stack.pop()
        x = stack.pop()
        stack.append(operator[z](x, y))
        print("%s %s %s = " % (x, z, y))

    print(stack[0])
    return stack[0]

RPN(rpn)



