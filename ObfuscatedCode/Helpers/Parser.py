from ast import parse
from ast2json import ast2json
from Helpers.Obfuscator import Obfuscator
from threading import Thread
import json
import random
import string

class ParseFile():
    def __init__(self, file: str):
        State = list(random.getstate()[1])
        self.RandomState = State
        self.OriginalState = State
        print(self.RandomState)
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
            print(Method)
            if Method != None:
                if Method == "print":
                    MethodsObfuscated = Obfuscator(eval(str(Method)), x['col_offset'], self.RandomState) # Super unsafe and bad
                    self.RandomState = MethodsObfuscated.State
                    MethodsObfuscated = MethodsObfuscated.Output
                    print(MethodsObfuscated)
                    if(x['value']['args'][0]['_type'] == 'Constant'):
                        Obfuscated = Obfuscator(x['value']['args'][0]['value'], x['col_offset'], self.RandomState)
                        self.RandomState = Obfuscated.State
                        Obfuscated = Obfuscated.Output
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
                            Obfuscated = Obfuscator(Value, x['col_offset'], self.RandomState)
                            self.RandomState = Obfuscated.State
                            Obfuscated = Obfuscated.Output
                            RandomObfuscated = Obfuscator(''.join([random.choice(string.ascii_letters) for _ in range(15)]), x['col_offset'], self.RandomState)
                            self.RandomState = RandomObfuscated.State
                            RandomObfuscated = RandomObfuscated.Output
                            print('\nObfuscated\n------------------\nDictionary: {}\n\nCall: {}\n------------------\n'.format(Obfuscated[0], Obfuscated[1]))
                            RandomStateAIO = Obfuscator(0,  x['col_offset'], self.RandomState)
                            self.RandomState = RandomStateAIO.State
                            self.ReplaceItems.append([
                                Obfuscated[0] + RandomObfuscated[0], '[' + str(Obfuscated[1]) + ',{}][bool({})]'.format(RandomObfuscated[1], RandomStateAIO.Output), 
                                x['value']['lineno'], VarNames['id'], None, x['col_offset']])
                        elif type(Value) == bool:
                            Obfuscated = Obfuscator(Value, x['col_offset'], self.RandomState)
                            self.RandomState = Obfuscated.State
                            Obfuscated = Obfuscated.Output
                            print('\nObfuscated\n------------------\nObfuscated Bool: {}\n\nCall: {}\n------------------\n'.format(Obfuscated, VarNames['id']))
                            self.ReplaceItems.append([
                                Obfuscated, None, 
                                x['value']['lineno'], VarNames['id'], None, x['col_offset']])  

                        elif type(Value) == int:
                            Obfuscated = Obfuscator(Value, x['col_offset'], self.RandomState)
                            self.RandomState = Obfuscated.State
                            Obfuscated = Obfuscated.Output
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
                                ObfuscatedKey = Obfuscator(x['value']['keys'][Key]['value'], x['col_offset'], self.RandomState)
                                self.RandomState = ObfuscatedKey.State
                                ObfuscatedKey = ObfuscatedKey.Output
                                if(type(x['value']['values'][Key]['value']) == str):
                                        ObfuscatedValue = Obfuscator(x['value']['values'][Key]['value'], x['col_offset'], self.RandomState)
                                        self.RandomState = ObfuscatedValue.State
                                        ObfuscatedValue = ObfuscatedValue.Output
                                finalDict[ObfuscatedKey[1]] = ObfuscatedValue[1]
                                finalObfuscatedKey+=ObfuscatedKey[0]+ ObfuscatedValue[0]
                        self.ReplaceItems.append([
                            finalObfuscatedKey, str(finalDict).replace("'",''),
                            x['value']['lineno'], VarNames['id'], None, x['col_offset']])     
                        print(finalDict)
                    elif x['value']['_type'] == "List":
                        Items = x['value']['elts']
                        Obfuscated = Obfuscator(Items, x['col_offset'], self.RandomState)
                        self.RandomState = Obfuscated.State
                        Obfuscated = Obfuscated.Output
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
                        Obfuscated = Obfuscator(Value, self.RandomState)
                        self.RandomState = Obfuscated.State
                        Obfuscated = Obfuscated.Output
                        print('\nObfuscated\n------------------\nDictionary: {}\n\nCall: {}\n------------------\n'.format(Obfuscated[0], Obfuscated[1]))
        
        thingsToObfuscate = ['FunctionDef', 'If', 'For', 'While']

        if(x['_type'] in thingsToObfuscate): #Funcs
            Body = x["body"]
            for x in Body:
                self.doStringObfiuscation(x)
    def parse_AST(self,astdump: str) -> str:
        with open('a.json', 'w') as x:x.write(str(json.dumps(astdump, indent=4)))

        thingsToObfuscate = ['FunctionDef', 'If', 'For', 'While']
        for x in astdump:
            if(x['_type'] in thingsToObfuscate): #Funcs
                Body = x["body"]
                for x in Body:
                    self.doStringObfiuscation(x)

            self.doStringObfiuscation(x)
        self.replace_strings(self.ReplaceItems)
        print(self.RandomState)
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
        RndTemplate = """
state = {}
def rnd():
    for states in range(len(state)):
        if states == len(state)-1: break
        choice = random.randint(0,1)
        if choice == 1: state[states]=state[states]+random.randint(0,10)
        elif choice == 0: state[states]=state[states]-random.randint(0,10)
    random.setstate((3,tuple(state),None))
    return random.randint(0,10)
""".format(str(self.OriginalState))
        print(self.OriginalState)
        lines[0] = 'import string;a=[];[[a.append(string.printable)] for x in string.printable];import random\n{}\n'.format(RndTemplate) + lines[0] 
        with open('./Results/Output.py', 'w') as f:
            f.writelines(lines)

    def read_file(self, File: str) -> str:
        with open(File, 'r') as f:
            ReadFile = f.read()
        if ReadFile != None:
            return ReadFile
