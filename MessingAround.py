testarray = ["test", "test2", "test3", "test4"]
y = [x for x in range(0,10)]
one,two,three,four,five,six,seven,eight,nine = y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8],y[9] #more spoofing
print(testarray[one])
if(0.1+0.2 == 0.30000000000000004): # floating point number
    print('passed') #passes
print(0.6+1.1) # more floating point
import string
import hashlib

a,xx = list(),[]
[xx.append(x) for x in string.printable]
[a.append(string.printable) for xy in xx] #append all characters for every item in list
print(a[nine*nine][54]+a[54][29]+a[92][27]+a[44][18]+a[73][23]+a[50][16]+a[38][77]+a[47][94]+a[22][17]+a[23][14]+a[32][21]+a[62][21]+a[65][24]+a[49][94]+a[64][32]+a[47][24]+a[8][27]+a[31][21]+a[2][13])

testingdict = {
    0+1+2-2: 't',
    5+5-5*2/2: 'e',
    6-6+6: 't',
    2*2*2/2/2: 's'
} #can run math in a dict
print(testingdict[5-4] + testingdict[10-5] + testingdict[5+1-4] + testingdict[2+4]) # prints 'test'

print(bool([])) # = false bool[1] = true
if(len('\\a\h\\t\\\m\\\\\\') == 12): # valid
    print('yes')
print(len('\/'))
a = '\\ \ \\ \ \\'
for x in a.split(' '):
    print(len(x)) # might use this for final packing, put in base64 then inverse then binary then this
def test():
    print('working :)')

_print = print # found https://stackoverflow.com/questions/49271750/is-it-possible-to-hack-pythons-print-function
def print(a):
    _print(a)
print('a')
test = 'test'
print(hashlib.md5(str.encode(test)).hexdigest()) #https://docs.python.org/3/library/hashlib.html

#########################################

_______ = [x for x in range(0,10)]
____,_____,______ = _______[1],_______[2],_______[3]
___________________,____________________________ = list(),[]
[____________________________.append(x) for x in eval('elbatnirp.gnirts'[::-1])]
[___________________.append(eval('elbatnirp.gnirts'[::-1])) for ______________ in ____________________________]
__=print
exec('def print(_):\n\tif(0.1+0.2 == 0.30000000000000004):\n\t\treturn(_)')
___ = [___________________[46][43],___________________[54][14], ___________________[29][34]]
_={
194*0+5-4:___[0],
5-______+_____-2:___[____],
______-4+4*2/_____:___[2]
}
def ________():
    return _[____]+_[_____]+_[______+____-____]
__(________()) 

#TODO
# - Start Main Project Files
# - 