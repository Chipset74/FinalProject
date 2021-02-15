import random
import string

class Obfuscator():
    def __init__(self, InputString: str) -> str:
        Randomized = self.RandomizeAlphabetString(InputString)
        #print(Randomized)
        self.Output = self.RandomDictionary(Randomized)
    def RandomizeAlphabetString(self, s: str):
        xx,finalstr = [],''
        [xx.append(x) for x in string.printable]
        for x in s:
            finalstr += str('a[' + self.RandomMathEquation(random.randint(0,99), 30) + '][' + self.RandomMathEquation(xx.index(x), 30) + ']+')
        return(finalstr[:-1])
    
    def RandomDictionary(self, s: str) -> list:
        Chars = s.split('+a')
        Dictionary,Call = {},''
        DictionaryVariable = '_0x' + str(random.randint(0000,99999999))
        #print(s)
        for Char in Chars:  
            CharIndex = self.RandomMathEquation(Chars.index(Char), 30)
            Dictionary[CharIndex] = ('a' + Char).replace('aa','a')
            Call+=DictionaryVariable + '[{}]+'.format(self.RandomMathEquation(Chars.index(Char), 30))
        StringifyedDictionary = DictionaryVariable + '=' + str(Dictionary).replace("'",'')
        #print(StringifyedDictionary + '\n')
        #print(Call[:-1])
        return ([StringifyedDictionary, Call[:-1]])

    def RandomMathEquation(self, InputNum: int, LoopAmount: int) -> str:
        try:
            print("Input Number: " + str(InputNum))
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
                    print('Found Equation:' + str(EvaledEquation), RandomEquationFinal[1:])
                    print('Remainder:' + str(GetRemainder))
                    RandomEquationFinal = RandomEquationFinal[1:] + '+' + str(GetRemainder)
                    if eval(RandomEquationFinal) == InputNum:
                        FoundEquation = True
                        print('Final Working Equation: ' + RandomEquationFinal)
                        return RandomEquationFinal
                else:
                    Looped = 0
                    RandomEquationFinal = ''
        except:
            print("Something Messed Up")
            return 'We messed up somewhere'