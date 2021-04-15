from ast import parse
from ast2json import ast2json
from Helpers.Obfuscator import Obfuscator
from threading import Thread
import json
import random
import string

class ParseFile():
    def __init__(self, file: str):
        self.file = file
        self.ReplaceItems = []
        ReadFile = self.read_file(file)
        self.read_with_ASTJSON(ReadFile)

    def read_with_ASTJSON(self, file: str):
        ParsedASTJSON = ast2json(parse(file))
        self.parse_AST(ParsedASTJSON['body'])
    
    def doStringObfiuscation(self, x):
        if x['_type'] == 'Expr': #Methods
            Method = x['value']['func']['id']
            if Method != None:
                if Method == "print":
                    MethodsObfuscated = Obfuscator(eval(str(Method)), x['col_offset']).Output # Super unsafe and bad
                    print(MethodsObfuscated)
                    if(x['value']['args'][0]['_type'] == 'Constant'):
                        Obfuscated = Obfuscator(x['value']['args'][0]['value'], x['col_offset']).Output
                        Obfuscated[1] = '{}{}({})'.format(MethodsObfuscated[1], MethodsObfuscated[0], Obfuscated[1])
                        self.ReplaceItems.append([
                            Obfuscated[0], Obfuscated[1], 
                            x['value']['func']['lineno'], None,
                            None, x['col_offset']
                        ])
        if(x['_type'] == 'Assign'): #Strings
            if(x['targets'][0]['_type'] == 'Name'):
                for VarNames in x['targets']:
                    if(x['value']['_type'] == 'Constant'):
                        Value = x['value']['value']
                        print('Variable: {}, Value: {}, ValueType: {}, LineNumber: {}'.format(VarNames['id'], Value, type(Value), x['value']['lineno']))
                        if(type(Value) == str):
                            Obfuscated = Obfuscator(Value, x['col_offset']).Output
                            RandomObfuscated = Obfuscator(''.join([random.choice(string.ascii_letters) for _ in range(15)]), x['col_offset']).Output
                            print('\nObfuscated\n------------------\nDictionary: {}\n\nCall: {}\n------------------\n'.format(Obfuscated[0], Obfuscated[1]))
                            self.ReplaceItems.append([
                                Obfuscated[0] + RandomObfuscated[0], '[' + str(Obfuscated[1]) + ',{}][bool({})]'.format(RandomObfuscated[1], Obfuscator(0,  x['col_offset']).Output), 
                                x['value']['lineno'], VarNames['id'], None, x['col_offset']])
                        elif type(Value) == bool:
                            Obfuscated = Obfuscator(Value, x['col_offset']).Output
                            print('\nObfuscated\n------------------\nObfuscated Bool: {}\n\nCall: {}\n------------------\n'.format(Obfuscated, VarNames['id']))
                            self.ReplaceItems.append([
                                Obfuscated, None, 
                                x['value']['lineno'], VarNames['id'], None, x['col_offset']])  

                        elif type(Value) == int:
                            Obfuscated = Obfuscator(Value, x['col_offset']).Output
                            print('\nObfuscated\n------------------\nObfuscated Int: {}\n\nCall: {}\n------------------\n'.format(Obfuscated, VarNames['id']))
                            self.ReplaceItems.append([
                                Obfuscated, None, 
                                x['value']['lineno'], VarNames['id'], None, x['col_offset']])

                        else:
                            print(type(Value))
                    elif x['value']['_type'] == 'Dict':
                        finalDict = {}
                        finalObfuscatedKey = ''
                        for Key in range(len(x['value']['keys'])):
                            if(type(x['value']['keys'][Key]['value']) == str):
                                ObfuscatedKey = Obfuscator(x['value']['keys'][Key]['value'], x['col_offset']).Output
                                if(type(x['value']['values'][Key]['value']) == str):
                                        ObfuscatedValue = Obfuscator(x['value']['values'][Key]['value'], x['col_offset']).Output
                                finalDict[ObfuscatedKey[1]] = ObfuscatedValue[1]
                                finalObfuscatedKey+=ObfuscatedKey[0]+ ObfuscatedValue[0]
                        self.ReplaceItems.append([
                            finalObfuscatedKey, str(finalDict).replace("'",''),
                            x['value']['lineno'], VarNames['id'], None, x['col_offset']])     
                        print(finalDict)
                    elif x['value']['_type'] == "List":
                        Items = x['value']['elts']
                        Obfuscated = Obfuscator(Items, x['col_offset']).Output
                        replaceList = []
                        stringyes = ''
                        for Eleme in Obfuscated:
                            replaceList.append(Eleme[1])
                            stringyes+=Eleme[0]

                        replaceString = str(replaceList).replace("'", '')
                        self.ReplaceItems.append([
                            replaceString, None, 
                            x['value']['lineno'], VarNames['id'], stringyes, x['col_offset']])

            elif x['targets'][0]['_type'] == 'Tuple':
                a = 0
                for VarNames in (x['targets'][0]['elts']):
                    Value = x['value']['elts'][a]['value']
                    print('Tuple Variable: {}, Value: {}, ValueType: {}, LineNumber: {}'.format(VarNames['id'], Value, type(Value), x['value']['lineno']))
                    if(type(Value) == str):
                        Obfuscated = Obfuscator(Value).Output
                        print('\nObfuscated\n------------------\nDictionary: {}\n\nCall: {}\n------------------\n'.format(Obfuscated[0], Obfuscated[1]))

    def parse_AST(self,astdump: str) -> str:
        with open('a.json', 'w') as x:x.write(str(json.dumps(astdump, indent=4)))

        thingsToObfuscate = ['FunctionDef', 'If', 'For']

        for x in astdump:
            if(x['_type'] in thingsToObfuscate): #Funcs
                Body = x["body"]
                for x in Body:
                    self.doStringObfiuscation(x)

            self.doStringObfiuscation(x)
        self.replace_strings(self.ReplaceItems)

    def replace_strings(self, ReplaceItems: list):
        x = 1 
        with open(self.file, 'r') as f:
            lines = f.readlines()
        for VarArray in ReplaceItems:
            spacer = ''
            for _ in range(VarArray[5]):
                spacer+=' '
           # print(self.ReplaceItems[4])
            if VarArray[4] is not None:
                lines[VarArray[2]-x] = VarArray[4] + '\n' + spacer + VarArray[3] + ' = ' + VarArray[0] + '\n'
            else:
                if VarArray[3] is not None and VarArray[1] is not None:
                    lines[VarArray[2]-x] = VarArray[0] + '\n' + spacer + VarArray[3] + ' = ' + VarArray[1] + '\n'
                elif VarArray[1] is not None:
                    lines[VarArray[2]-x] = VarArray[0] + '\n' + spacer + VarArray[1] + '\n'
                else:
                    lines[VarArray[2]-x] = spacer + VarArray[3] + ' = ' + VarArray[0] + '\n'

        lines[0] = 'import string;a=[];[[a.append(string.printable)] for x in string.printable]\n' + lines[0] 
        with open('./Results/Output.py', 'w') as f:
            f.writelines(lines)

    def read_file(self, File: str) -> str:
        with open(File, 'r') as f:
            ReadFile = f.read()
        if ReadFile != None:
            return ReadFile