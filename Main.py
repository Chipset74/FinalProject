import ast
import codegen
import base64
import random
import string

class Obfuscator():
    def __init__(self, InputString):
        Randomized = self.RandomizeAlphabetString(InputString)
        #print(Randomized)
        self.Output = self.RandomDictionary(Randomized)
    def RandomizeAlphabetString(self, s):
        xx,finalstr = [],''
        [xx.append(x) for x in string.printable]
        for x in s:
            finalstr += str('a[' + self.RandomMathEquation(random.randint(0,99), 10) + '][' + self.RandomMathEquation(xx.index(x), 10) + ']+')
        return(finalstr[:-1])
    
    def RandomDictionary(self, s):
        Chars = s.split('+a')
        Dictionary = {}
        DictionaryVariable = ''
        Call = ''
        #print(s)
        for Char in Chars:
            CharIndex = self.RandomMathEquation(Chars.index(Char), 10)
            Dictionary[CharIndex] = ('a' + Char).replace('aa','a')
            Call+=DictionaryVariable + '[{}]+'.format(self.RandomMathEquation(Chars.index(Char), 10))
        StringifyedDictionary = DictionaryVariable + '=' + str(Dictionary).replace("'",'')
        print(StringifyedDictionary + '\n')
        print(Call[:-1])
        return (Call[:-1])

    def RandomMathEquation(self, InputNum, LoopAmount):
        #print("Input Number: " + str(InputNum))
        Operaters = ['+','-','*','/', '%']
        Looped = 0
        FoundEquation,RandomEquationFinal = False,''
        while(FoundEquation==False):
            while(LoopAmount != Looped):
                RandomNumber = random.randint(1,20)
                RandomEquationInput = random.choice(Operaters) + str(RandomNumber)
                RandomEquation = str(InputNum) + RandomEquationInput
                Evaled = eval(RandomEquation)
                if(type(Evaled) == int):
                    Looped+=1
                    RandomEquationFinal += RandomEquationInput
            EvaledEquation = eval(RandomEquationFinal[1:])
            if(EvaledEquation < InputNum and EvaledEquation > InputNum-10):   
                GetRemainder = eval(str(InputNum) + '-(' + RandomEquationFinal[1:] + ')') 
                #print('Found Equation:' + str(EvaledEquation), RandomEquationFinal[1:])
                #print('Remainder:' + str(GetRemainder))
                RandomEquationFinal = RandomEquationFinal[1:] + '+' + str(GetRemainder)
                if(eval(RandomEquationFinal) == InputNum):
                    FoundEquation = True
                    #print('Final Working Equation: ' + RandomEquationFinal)
                    return RandomEquationFinal
            else:
                Looped = 0
                RandomEquationFinal = ''
                
def start():
    with open('input.py', 'r') as f:
        expr = f.read()
        #print(expr)

    ob = Obfuscator("Hey, My name is billy bob joe")

start()