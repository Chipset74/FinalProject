import json
from ast import parse
from ast2json import ast2json

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
                for VarNames in x['_type']['targets']:
                    print(VarNames['id'])

    def ReadFile(self,File):
        with open(File, 'r') as f:
            ReadFile = f.read()
        if(ReadFile != None):
            return ReadFile

p = ParseFile('output.py')