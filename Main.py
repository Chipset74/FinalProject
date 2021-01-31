import ast
import codegen
import base64
import random
import string

class Obfuscator():
    def __init__(self):
        Randomized = self.RandomizeAlphabetString('hey')
        self.RandomDictionary(Randomized)
        self.RandomMathEquation(50, 10)
    def RandomizeAlphabetString(self, s):
        xx,finalstr = [],''
        [xx.append(x) for x in string.printable]
        for x in s:
            finalstr += 'a[' + str(random.randint(0,99)) + '][' + str(xx.index(x)) + ']+'
        return(finalstr[:-1])
    
    def RandomDictionary(self, s):
        Chars = s.split('+')
        Dictionary = {}
        for Char in Chars:
            print(Char)
            Dictionary[Chars.index(Char)] = Char
        print(Dictionary)

    def RandomMathEquation(self, InputNum, LoopAmount):
        print("Input Number: " + str(InputNum))
        Operaters = ['+','-','*','/']
        Looped = 0
        FoundEquation,RandomEquationFinal = False,''
        while(FoundEquation==False):
            while(LoopAmount != Looped):
                RandomNumber = random.randint(1,10)
                RandomEquationInput = random.choice(Operaters) + str(RandomNumber)
                RandomEquation = str(InputNum) + RandomEquationInput
                Evaled = eval(RandomEquation)
                if(type(Evaled) == int):
                    Looped+=1
                    RandomEquationFinal += RandomEquationInput
            EvaledEquation = eval(RandomEquationFinal[1:])
            if(EvaledEquation < 50 and EvaledEquation > 40):   
                GetRemainder = eval('50-(' + RandomEquationFinal[1:] + ')') 
                print('Found Equation:' + str(EvaledEquation), RandomEquationFinal[1:])
                print('Remainder:' + str(GetRemainder))
                RandomEquationFinal = RandomEquationFinal[1:] + '+' + str(GetRemainder)
                if(eval(RandomEquationFinal) == InputNum):
                    FoundEquation = True
                    print('Final Working Equation: ' + RandomEquationFinal)
            else:
                Looped = 0
                RandomEquationFinal = ''
                
def start():
    ob = Obfuscator()

start()