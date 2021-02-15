import operator

def getMath(inp):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    return(ops[inp])