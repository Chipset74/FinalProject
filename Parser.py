import json
from ast import parse
from ast2json import ast2json
from Obfuscator import Obfuscator

class ParseFile():
    def __init__(self, file):
        ReadFile = self.ReadFile(file)
        self.ReadWithASTJSON(ReadFile)

    def ReadWithASTJSON(self,file):
        ParsedASTJSON = ast2json(parse(file))
        self.ParseAST(ParsedASTJSON['body'])

    def ParseAST(self,astdump):
        for x in astdump:
            if(x['_type'] == 'Assign'):
                if(x['targets'][0]['_type'] == 'Name'):
                    for VarNames in x['targets']:
                        Value = x['value']['value']
                        print('Variable: {}, Value: {}, ValueType: {}, LineNumber: {}'.format(VarNames['id'], Value, type(Value), x['value']['lineno']))
                        if(type(Value) == str):
                            Obfuscated = Obfuscator(Value).Output
                            print('\nObfuscated\n------------------\nDictionary: {}\n\nCall: {}\n------------------\n'.format(Obfuscated[0], Obfuscated[1]))
                elif(x['targets'][0]['_type'] == 'Tuple'):
                    a = 0
                    for VarNames in (x['targets'][0]['elts']):
                        Value = x['value']['elts'][a]['value']
                        print('Tuple Variable: {}, Value: {}, ValueType: {}, LineNumber: {}'.format(VarNames['id'], Value, type(Value), x['value']['lineno']))
                        if(type(Value) == str):
                            Obfuscated = Obfuscator(Value).Output
                            print('\nObfuscated\n------------------\nDictionary: {}\n\nCall: {}\n------------------\n'.format(Obfuscated[0], Obfuscated[1]))
                        a+=1

    def ReadFile(self,File):
        with open(File, 'r') as f:
            ReadFile = f.read()
        if(ReadFile != None):
            return ReadFile

p = ParseFile('output.py')