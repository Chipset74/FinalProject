import ast
import codegen
import base64
import random
import string

class Obfuscator():
    def __init__(self):
        self.RandomizeAlphabetString('testing')
        self.RandomDictionary('aaa')
    def RandomizeAlphabetString(self, s):
        a,xx,finalstr = list(),[],''
        [xx.append(x) for x in string.printable]
        for x in s:
            finalstr += 'a[' + str(random.randint(0,99)) + '][' + str(xx.index(x)) + ']+'
        return(finalstr[:-1])
    
    def RandomDictionary(self, s):
        UnScrambledDict = {1:'test',2:'test2',3:'testing',4:'lasttest'}
        random.shuffle(UnScrambledDict.keys)
        print(UnScrambledDict)

ob = Obfuscator()