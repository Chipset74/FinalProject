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
print(testingdict)
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
"""
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
"""
#TODO
# - Start Main Project Files
# - 

a,xx = list(),[]
[xx.append(x) for x in string.printable]
[a.append(string.printable) for xy in xx] 
yes={14-1*7+8%4*5*8+8%14-20+5: a[18%16-18+18-1%11%6-18+1+16+5][9+3-15+8*20-16*4+17%4%17+2], 2%1-19+12-12%17*5%16+6*2+8: a[19+13-4+14+5*11-10%15-2+5+3][15+18%3+6%13+20%6%8%12*18+3], 11-15%5*3-2*1%20-6-6-3+8: a[10-12+17-9*12-9+5*16+4*17+9][17%9*8-17-12%17-15%2*14-5+8], 9%15%11*3%5*5*17%6+14-20+7: a[19%12%10*10+13%16%5%5+12+10+3][4*11%20+8+15%19%18+9*6%6+3], 11%18*12%15*1*12*12%5*17%1+4: a[3%13%16*9-20%12*14%6%4*3+6][5%16+18+3*20-4+12-2%19%9+5], 20-5-17-4*19%16*10%4*6+3+4: a[19%19%12+10+20%15*11-14%16%2+3][15*1*19%11%19-15%6+18+10%10+5], 20%19-4*8%7-16-2*8%8+20+5: a[8*4+1-1+18%7*16-5+1-10+4][6+15%12-11+17-14*9%3%20+7+1], 4+8+5*6-15-17-18+12%15%13+3: a[12-5*2-20-10-2+12-20+18*6+2][14+18-15%13+2+6*2-6-15-16+6], 4-20-16*4*15%4+10*1-2+14+2: a[12%20%7%1-1%5%7*4-12%1+8][7-14-10%4+1-4-19-12+7*8+1], 7%17-13%17-18*13*15%9+11+3+1: a[17+1*1*12%12%6+16-19+5%8+9][11%4-8+9+2%6%2+10+11%13+2], 17-19-2*3*14*16%3*15%14+8+4: a[4%18*8*4%13+10%7*20%10+1+2][20-15%14+2%10+18-5+7+1-18+4], 20+5+4+2-7%2%5%13*8-13+1: a[5%11-8-1%1%8-9+3*14+9+4][13*18%13*9-15+5*2%14*5-13+7], 1-17*18%3*8%1-2-19%6+10+4: a[16-3*7%20%13+20%5*18*3+11+9][3*20%8+12+13%4-3+3%3-7+3], 8%11-2*18%4*3*19%18-7+11+1: a[20-6%19+11*2+14+11%5+10%9+5][8%1*9+20%19%8*9-19%14+18+1], 12-13+7+17%12%10-16+7%15+8+4: a[3+3+8+18+17*16*18%5*5%2+1][8-13%3+1%4-15+16+13%6-1+4], 12%7-1*11*3+3%17*19-3-16+5: a[14%5+17+5%10*20%17%3*1+8+4][1*14*20-7-18%1*9%12-10*18+1], 17%6+2%6+1*10-13%3%19-7+7: a[18-4-12-11-20%14*15%6*1+20+9][6+4-15+7-10+18+18%2-19+17+3], 6+18-7%20+14-5-13%7-20%14+3: a[7+10-3+7+15+8-10+20+11+8+9][6%15-4-1%18+10+6-7%4%18+4], 3%9*3-7+10-13+2%10*5+5+4: a[9%15%3+1+18*2+20-8-16-14+3][12%18-19+7%1+20+9%19-17+12+6], 12+6%10-2-16+15+16%7-15+13+4: a[9+19+19%8%1-8%11-4-6*1+1][14%2*12-7+17%15*10%16+20-15+8], 17+2+13*8%14%7+5-12%13%19+2: a[16+16+15%1+13*15%15%4-2*9+5][13%17%13-10%19*12%15+12-5+14+6], 11%1*7-19%8+1*15+17%18%6+4: a[14-2%15*14%3%18+16+9%12*4+9][14+13-6+12%17*18%6*15+5+3+5], 19*11%5%7+14+4+7*3%1-5+5: a[20*2-7+15%12-18%13+1*18-1+1][6+14%2*4%2+16*9-9*9+20+5], 20+18+7*15*7%12-7-13-15+16+1: a[3+6+18-7+19*18%16*9+12%8+7][20+15-9-4-5+8%2%5-7+9+9], 7+17-19%13*2+17-13%19+4%17+4: a[12-3+4*18+20+13%3%15*6-13+1][16-2*3*10%15%20-9+13%20%5+4], 8-17%6*14%7%14%12*5*7+12+5: a[3-1+3%7%16*5+6+17+15+18+4][8*20%8*18*7%15*17%13-13+18+5], 18%11-6+9+9*8*1%5+8%19+6: a[16+18%10*19*8*20%7%17-3-7+2][1*19-18%2-1-10+16-3%3*12+3], 18-18*16*11%13+2%14*17*16%19+6: a[11*3-13%12%20%6%18*1-20%16+3][1+9-5-16%3-11%11*14%16%11+8], 3+7%7%16*11+13%5+5%16+11+6: a[12*4+15*20*20%13+8%9%8-15+1][12-13+7%12-8+14%18-16+17-5+9], 6+2%4-8*12%4+19+10+4-15+3: a[15%10-5+10%3%8*6+6*11+10+6][7-7*6-3%20*13+11*12+15+15+6], 1+1+16-5+4%10%3+15-20%17+4: a[9+8%11-7*1+17+7-19%6*16+1][14+18-9%16+12-7+1-17%8-8+7], 7-17*15%1%18%3%13*1+13+9+2: a[17+8-12-12+7+4*13-19%12*5+2][11%20*3-20%16-20+5*18*1%4+3], 11*9+20%2*6+13-2-7%11*12+6: a[10+5%5-18-13-7+12%3+15+17+3][19%1*18*11*7*11*18%9+13-8+5], 13+15%7*12%14%18-2+6+17%4+3: a[6*18-15+17-15-1-1+14%15-14+5][14%2*8%13-7%11*19%2+16+3+3], 19+11%15*20%12+4+20-7-4-7+5: a[12+16+8-11*3*6%3+13+4+4+7][10%2%10*14*19+8*18*2%12+16+5], 18+8+4*10+17%12-16%14%14*20+4: a[16%10*10+18-14+19+10%9+14-10+6][13+5+10+2+11-11-10+4+5-2+7], 11+7+5-2+14+14%18%1-19%13+7: a[14+1%8+12+2%15+17%13%9-11+2][17%17+12%3%20+12+5*16+2-2+2], 8%12+7+12*5*16%16*12+18-1+5: a[4%5%18-11+10+3*2*15%12*13+3][17%12+17%9+10+17%18%17-11%11+9], 3%20*6*16%17*2-10*1%10%17+6: a[4*11+2+2-4%16%5-20-17+1+7][9-5%1%3-7%5*2+16%17-10+3], 4-8+4%20+4%14-9+14%16*3+2: a[2+8%1-15-12*10+9%3+11*18+8][10*7%12%16%14%9-13*5%20+19+6], 14+1%3*12+6+1%11-1%1%17+7: a[5+4*16-11-12%14+10+17-3+15+7][7+15-5+9-3+3+14-7-7*3+9], 10-5+12+15-15+15+17%16*4-4+9: a[10+2%16%8%20%2%18+15%5*18+9][10+9+16-6+11+12+4-19%18%8+7]}

print(yes[13+13+5%12-18+9%3-6%8-13+6]+yes[9%12+2-6%14-7-1*10+3+3+7]+yes[10+17%1+1%16-5+13-18-5%12+6]+yes[19+11%5-16-1-9-4*8%20+12+9]+yes[4%15-15%11%12%19%13+18%16%3+2]+yes[8-7+18*2*1%9*4*5*10*16+4]+yes[19*4%4-1-5%1*16*1*7-2+9]+yes[8-3-15-13+19%19+10-16%4+14+6]+yes[4-19%8+3+20%10*5*4%8%17+4]+yes[6%9+4-11*10%2+6-14%3-12+7]+yes[20%7+9%12%16%6-8%18%1*6+1]+yes[6-13-9-3%20%13-4+9+4*6+1]+yes[18%15+5-17-3+11-5+10-14+20+2]+yes[14+4%17*12*18%19+5%2-11-2+2]+yes[16+16%14*15%3%5*5-5+2%5+1]+yes[16*1*4*4%14-16*14%6+15%10+8]+yes[6+19%16-2%19%12*1+13%17-13+9]+yes[5%18+11%17%7*1%19*4*10%7+6]+yes[7-6*3-13%13%6+6*4-8+11+2]+yes[14*18%10-2%15-16+8+2%18+17+8]+yes[18%15*6%8-6+19%15%8%15+17+3]+yes[5%2*14-11+12+9*9*11%1*10+6]+yes[1-9+10*1+1*11+13-2-2-3+3]+yes[19*1-11%1*6-3%12-8*2%2+7]+yes[8*11%5*2+6%15%20%16+11%4+9]+yes[13%17+12+1+19%6-11*16*19%13+1]+yes[1-9%17%3*2*3%11%12*9+18+7]+yes[14+12-11%11%9%19+12%6%12*15+1]+yes[5+1-13%3*2+16-1+7-12+12+2]+yes[2*17-1-11*2*11%11+13-9*2+1]+yes[13+20-3+16%19%3+2-18%11%12+4]+yes[13-6+8*20%6-5+16+19-9*2+8]+yes[2%6+18+13+12-19+11%6%8%1+6]+yes[6%5*10+18-3+11%14-17+3+10+1]+yes[8%5+14+18*14%6+16%5*9%13+8]+yes[11-12+12+19-13+12-6+10-14%8+8]+yes[18+4%15*8%14+13+16-13+4-7+1]+yes[10*6*17*15*10%15%16+3+18+15+1]+yes[5*6+6+18%17+2*10*4%20%20+1]+yes[15+20*17%14-6*4%15%13+9*3+2]+yes[17%1+20%6*9-15+12+2+8+13+2]+yes[7%6*7-7-17%4-11+18+20+11+4])