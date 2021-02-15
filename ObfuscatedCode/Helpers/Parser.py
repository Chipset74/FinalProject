from ast import parse
from ast2json import ast2json
from Helpers.Obfuscator import Obfuscator

class ParseFile():
    def __init__(self, file: str):
        self.file = file
        ReadFile = self.read_file(file)
        self.read_with_ASTJSON(ReadFile)

    def read_with_ASTJSON(self, file: str):
        ParsedASTJSON = ast2json(parse(file))
        self.parse_AST(ParsedASTJSON['body'])

    def parse_AST(self,astdump: str) -> str:
        ReplaceItems = []
        #with open('a.json', 'w') as x:x.write(str(astdump))
        for x in astdump:
            if(x['_type'] == 'Assign'):
                if(x['targets'][0]['_type'] == 'Name'):
                    for VarNames in x['targets']:
                        #if(type(x['value']['_type']) == 'Constant'):
                        Value = x['value']['value']
                        print('Variable: {}, Value: {}, ValueType: {}, LineNumber: {}'.format(VarNames['id'], Value, type(Value), x['value']['lineno']))
                        if(type(Value) == str):
                            Obfuscated = Obfuscator(Value).Output
                            print('\nObfuscated\n------------------\nDictionary: {}\n\nCall: {}\n------------------\n'.format(Obfuscated[0], Obfuscated[1]))
                            ReplaceItems.append([
                                Obfuscated[0], Obfuscated[1], 
                                x['value']['lineno'], VarNames['id']])

                elif x['targets'][0]['_type'] == 'Tuple':
                    a = 0
                    for VarNames in (x['targets'][0]['elts']):
                        Value = x['value']['elts'][a]['value']
                        print('Tuple Variable: {}, Value: {}, ValueType: {}, LineNumber: {}'.format(VarNames['id'], Value, type(Value), x['value']['lineno']))
                        if(type(Value) == str):
                            Obfuscated = Obfuscator(Value).Output
                            print('\nObfuscated\n------------------\nDictionary: {}\n\nCall: {}\n------------------\n'.format(Obfuscated[0], Obfuscated[1]))

            elif x['_type'] == 'Expr': #Methods
                Method = x['value']['func']['id']
                if Method != None:
                    Obfuscated = Obfuscator(eval(str(Method))).Output # Super unsafe and bad
                    print(Obfuscated)

            elif(x['_type'] == 'FunctionDef'):
                pass
        self.replace_strings(ReplaceItems)

    def replace_strings(self, ReplaceItems: list):
        with open(self.file, 'r') as f:
            lines = f.readlines()
        for VarArray in ReplaceItems:
            lines[VarArray[2]-1] = VarArray[0] + '\n' + VarArray[3] + '=' + VarArray[1] + '\n'
        lines[0] = 'import string;a=[];[[a.append(string.printable)] for x in string.printable]\n' + lines[0] 
        with open('./Results/Output.py', 'w') as f:
            f.writelines(lines)

    def read_file(self, File: str) -> str:
        with open(File, 'r') as f:
            ReadFile = f.read()
        if ReadFile != None:
            return ReadFile