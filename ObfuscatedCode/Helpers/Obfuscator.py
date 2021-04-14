import random
import string

class Obfuscator():
    def __init__(self, InputString, ColOffset) -> str:
        if InputString != None:
            if callable(InputString):
                self.Output = self.override_native_methods(InputString)
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
    
    def override_native_methods(self, Method) -> str:
        if Method == print:
            RandomString = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
            return [RandomString, "{}=print\n".format(RandomString)]

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
            #print(s)
            for Char in Chars:  
                CharIndex = self.random_math_equation(Chars.index(Char), 6)
                Dictionary[CharIndex] = ('a' + Char).replace('aa','a')
                Call+=random.choice(DictionaryNames) + '[{}]+'.format(self.random_math_equation(Chars.index(Char), 6))
            StringifyedDictionary += DictionaryVariable + '=' + str(Dictionary).replace("'",'') + '\n'
            #print(StringifyedDictionary + '\n')
            #print(Call[:-1])
        return [StringifyedDictionary, Call[:-1]]

    def random_math_equation(self, InputNum: int, LoopAmount: int) -> str:
        try:
            #print("Input Number: " + str(InputNum))
            Operaters = ['+', '-', '*', '/']
            Looped = 0
            FoundEquation, RandomEquationFinal = False, ''
            while FoundEquation is False:
                while LoopAmount != Looped:
                    RandomNumber = random.randint(1,11)
                    if(RandomNumber == 1):
                        RandomNumber=True
                    RandomEquationInput = random.choice(Operaters) + str(RandomNumber)
                    RandomEquation = str(InputNum) + RandomEquationInput
                    Evaled = eval(RandomEquation)
                    if type(Evaled) == int:
                        Looped+=1
                        RandomEquationFinal += RandomEquationInput
                EvaledEquation = eval(RandomEquationFinal[1:])
                if EvaledEquation < InputNum and EvaledEquation > InputNum-20: # Finds an equation that is within 10 numbers of the input (makes it looks more random) 
                    GetRemainder = eval(str(InputNum) + '-(' + RandomEquationFinal[1:] + ')') 
                    #print('Found Equation:' + str(EvaledEquation), RandomEquationFinal[1:])
                    #print('Remainder:' + str(GetRemainder))
                    RandomEquationFinal = RandomEquationFinal[1:] + '+' + str(GetRemainder)
                    if eval(RandomEquationFinal) == InputNum:
                        FoundEquation = True
                        #print('Final Working Equation: ' + RandomEquationFinal)
                        return RandomEquationFinal
                else:
                    Looped = 0
                    RandomEquationFinal = ''
        except:
            print("Something Messed Up")
            return None