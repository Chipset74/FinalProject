import random
import string

class Obfuscator():
    def __init__(self, InputString, ColOffset) -> str:
        if InputString != None:
            if callable(InputString):
                self.Output = self.override_native_methods(InputString, ColOffset)
            elif type(InputString) == str:
                self.Output = self.random_dictionary(InputString, ColOffset)
            elif type(InputString) == int:
                self.Output = self.random_math_equation(InputString, 10)
            elif type(InputString) == bool:
                self.Output = "bool({})".format(self.random_math_equation(True if InputString else False, 5))
            elif type(InputString) == list:
                finalList = []
                for element in InputString:
                    ObfuscatedElement = self.random_dictionary(element['value'], ColOffset)
                    finalList.append(ObfuscatedElement)
                self.Output = finalList

    def randomize_alphabet_string(self, s: str):
        xx,finalstr = [],''
        [xx.append(x) for x in string.printable]
        for x in s:
            finalstr += str('a[{}][{}]+'.format(self.random_math_equation(random.randint(0,99), 6), self.random_math_equation(xx.index(x), 6)))
        return(finalstr[:-1])
    
    def override_native_methods(self, Method,ColOffset) -> str:
        spacer = ''
        for _ in range(ColOffset):
            spacer+=' '
        if Method == print:
            RandomString = '_0x' + str(random.randint(00000,99999999))
            return [spacer + RandomString, "{}=print\n".format(RandomString)]

    def random_dictionary(self, s: str, ColOffset: int) -> list:
        DictionaryNames = []
        spacer = ''
        for _ in range(ColOffset):
            spacer+=' '
        StringifyedDictionary= ''
        for x in range(15):
            Chars = self.randomize_alphabet_string(s).split('+a')
            Dictionary,Call = {},''
            DictionaryVariable = spacer + '_0x' + str(random.randint(00000,99999999))
            DictionaryNames.append(DictionaryVariable)
            for Char in Chars:  
                CharIndex = self.random_math_equation(Chars.index(Char), 6)
                Dictionary[CharIndex] = ('a' + Char).replace('aa','a')
                Call+=random.choice(DictionaryNames) + '[{}]+'.format(self.random_math_equation(Chars.index(Char), 6))
            StringifyedDictionary += DictionaryVariable + '=' + str(Dictionary).replace("'",'') + '\n'
            
        return [StringifyedDictionary, Call[:-1].replace(spacer, '')]

    def random_math_equation(self, InputNum: int, LoopAmount: int) -> str:
        try:
            Operaters = ['+', '-', '*', '/']
            Looped = 0
            FoundEquation, RandomEquationFinal = False, ''
            while FoundEquation is False:
                while LoopAmount != Looped:
                    RandomNumber = random.randint(0,11)
                    if RandomNumber == 1: RandomNumber=True
                    elif RandomNumber == 0: RandomNumber = False
                    if(RandomNumber%2 == 0): f = '~'
                    else: f = '~~'

                    for x in range(RandomNumber): f+='~~'
                    RandomNumber =  f + str(RandomNumber)

                    RandomEquationInput = random.choice(Operaters) + str(RandomNumber)
                    RandomEquation = str(InputNum) + RandomEquationInput
                    Evaled = eval(RandomEquation)
                    if type(Evaled) == int:
                        Looped+=1
                        RandomEquationFinal += RandomEquationInput
                RandomEquationFinal = RandomEquationFinal
                EvaledEquation = eval(RandomEquationFinal[1:])
                if EvaledEquation < InputNum and EvaledEquation > InputNum-40: # Finds an equation that is within 10 numbers of the input (makes it looks more random) 
                    GetRemainder = eval(str(InputNum) + '-(' + RandomEquationFinal[1:] + ')') 
                    RandomEquationFinal = "(" + RandomEquationFinal[1:] + '+' + str(GetRemainder) + ")"
                    FoundEquation = True
                    return RandomEquationFinal
                else:
                    Looped = 0
                    RandomEquationFinal = ''
        except Exception as e:
            print("Something Messed Up")
            print(e)
            return None