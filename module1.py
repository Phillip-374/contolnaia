#def uskorenie():
    #a=(u1-u0)/t
    #return a
#    print('+')



def rastoianie(uskorenie):
    def obertka(u0,u1,t):
        uskorenie(u0,u1,t)
        s=((u1-u0)/t*t*t)/2
        print('Путь',s)
    return obertka

@rastoianie
def uskorenie(u0,u1,t):
    a=(u1-u0)/t
    print('Ускорение',a)
uskorenie


try:
    uskorenie(0,4,2)
except TypeError:
    print('Данные не являются числами')
except ZeroDivisionError:
    print('Время не может быть нулём')

