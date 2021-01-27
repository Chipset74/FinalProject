
import ast
import codegen

class NodeVisitor(ast.NodeVisitor):
    def visit_Str(self, tree_node):
        print('{}'.format(tree_node.s))

class NodeTransformer(ast.NodeTransformer):
    def visit_Str(self, tree_node):
        return ast.Str('String: ' + tree_node.s)

class Obfuscator():
    def __init__(self):
        pass
    def StringEncrypt(self):
        pass
    def FunctionEncrypt(self):
        pass

class StartObfuscator():
    def __init__(self):
        expr="""
        def foo():
        print("hello world")
        """

        tree_node=ast.parse(expr)
        #tree_node.body[0].body= [ ast.parse("return 42").body[0] ]

        NodeTransformer().visit(tree_node)
        NodeVisitor().visit(tree_node)

        #print(codegen.to_source(tree_node))
print(....__class__().__str__())
