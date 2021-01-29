
import ast
import codegen
import base64
import random
import string

class NodeVisitor(ast.NodeVisitor):
    def visit_Str(self, tree_node):
        #print('{}'.format(tree_node.s))
        ob = Obfuscator('str', tree_node.s)
        print(ast.dump(tree_node))
        return(ob,ast.dump(tree_node))
    def visit_Name(self, tree_node):
        #print('{}'.format(tree_node.id))
        ob = Obfuscator('func', tree_node.id)
        return(ob.output,ast.dump(tree_node))

class NodeTransformer(ast.NodeTransformer):
    def visit_Str(self, tree_node):
        return ast.Str(tree_node.s)
    def visit_Name(self, tree_node):
        return ast.Name(tree_node.id)

class Obfuscator():
    def __init__(self, typ, inpt):
        if(typ == 'str'):
            Output = self.RandomizeAlphabetString(inpt)
            self.RandomList(Output)
        elif(typ == 'func'):
            self.FunctionEncrypt(inpt)
        self.output = 'a'
    def StringEncrypt(self, s):
        #a = base64.encode(s, 'ascii')
        pass
    def FunctionEncrypt(self, f):
        name = '_0x' + str(random.randint(0000000,99999999))
        return name
    def JunkVarOverride(self):
        pass
    def JunkCode(self):
        pass
    def RandomList(self, s):
        DictofVars = {}
        Split_Data = s.split('+')
        for x in range(len(Split_Data)):
            DictofVars[x] = Split_Data[x]
            Split_Data[x] = s.replace(Split_Data[x], str(x))
        print(DictofVars)
        print(Split_Data)
        return DictofVars
    def RandomizeAlphabetString(self, s):
        xx = list()
        finalstr = ''
        for x in string.printable:
            xx.append(x)
        for x in s:
            print(xx.index(x))
            finalstr += 'a[' + str(random.randint(0,99)) + '][' + str(xx.index(x)) + ']+'
        return(finalstr[:-1])

class StartObfuscator():
    def __init__(self):
        with open('input.py', 'r') as f:
            expr = f.read()
        #print(expr)
        tree_node=ast.parse(expr)
        #print(ast.dump(tree_node))
        #tree_node.body[0].body= [ ast.parse("return 42").body[0] ]

        NodeTransformer().visit(tree_node)
        a = NodeVisitor().visit(tree_node)
        print(a)

        #print(codegen.to_source(tree_node))

Start = StartObfuscator()
