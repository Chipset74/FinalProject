import random
import string

class Obfuscator():
    def __init__(self, InputString) -> str:
        if InputString != None:
            if callable(InputString):
                self.Output = self.override_native_methods(InputString)
            elif type(InputString) == str:
                Randomized = self.randomize_alphabet_string(InputString)
                self.Output = self.random_dictionary(Randomized)

    def randomize_alphabet_string(self, s: str):
        xx,finalstr = [],''
        [xx.append(x) for x in string.printable]
        for x in s:
            finalstr += str('a[{}][{}]+'.format(self.random_math_equation(random.randint(0,99), 30), self.random_math_equation(xx.index(x), 30)))
        return(finalstr[:-1])
    
    def override_native_methods(self, Method) -> str:
        if Method == print:
            RandomString = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
            return "{}=print\n".format(RandomString)

    def random_dictionary(self, s: str) -> list:
        Chars = s.split('+a')
        Dictionary,Call = {},''
        DictionaryVariable = '_0x' + str(random.randint(0000,99999999))
        #print(s)
        for Char in Chars:  
            CharIndex = self.random_math_equation(Chars.index(Char), 30)
            Dictionary[CharIndex] = ('a' + Char).replace('aa','a')
            Call+=DictionaryVariable + '[{}]+'.format(self.random_math_equation(Chars.index(Char), 30))
        StringifyedDictionary = DictionaryVariable + '=' + str(Dictionary).replace("'",'')
        #print(StringifyedDictionary + '\n')
        #print(Call[:-1])
        return [StringifyedDictionary, Call[:-1]]

    def random_math_equation(self, InputNum: int, LoopAmount: int) -> str:
        try:
            #print("Input Number: " + str(InputNum))
            Operaters = ['+','-','*','/']
            Looped = 0
            FoundEquation,RandomEquationFinal = False,''
            while FoundEquation==False:
                while LoopAmount != Looped:
                    RandomNumber = random.randint(1,20)
                    RandomEquationInput = random.choice(Operaters) + str(RandomNumber)
                    RandomEquation = str(InputNum) + RandomEquationInput
                    Evaled = eval(RandomEquation)
                    if type(Evaled) == int:
                        Looped+=1
                        RandomEquationFinal += RandomEquationInput
                EvaledEquation = eval(RandomEquationFinal[1:])
                if EvaledEquation < InputNum and EvaledEquation > InputNum-10: # Finds an equation that is within 10 numbers of the input (makes it looks more random) 
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
            return 'We messed up somewhere'

o = Obfuscator('s')