import math
import numpy as np

def test_fun(x):
    return 10*(1+(x-math.pi/5)**2/3-math.cos(3*math.pi*(x-math.pi/5)))

# 1. Sposób naiwny
    
def find_min_naive(f,a,b,d): # f - funkcja, a - początek przedziału, b - koniec przedziału, d - średnica podziału
    x=np.linspace(a,b,int((b-a)//d))
    y=np.vectorize(f)(x)
    return min(y)

    # 1.1. Sposób naiwny para
    
def find_min_naive_para(f,a,b,d): # f - funkcja, a - początek przedziału, b - koniec przedziału, d - średnica podziału
    x=np.linspace(a,b,int((b-a)//d))
    xm = a
    ym = f(a)
    for i in range( 1, len(x) ):
        y = f(x[i])
        if ( y < ym ):
            ym = y
            xm = x[i]
    return ( xm, ym, len(x)  )

    # 2. Podział zwykły
    
def podzial(f,a,b,d):
    licznik = 0
    wsp = 0.1
    while ( (b-a) > d):
        licznik = licznik + 2           
        x1 = a + wsp*(b-a)
        x2 = b - wsp*(b-a)
        if ( f(x1) < f(x2)):
            b = x2
        else:
            a = x1

    x1 = (a +b)/2
    y1 = f(x1)
    return ( x1, y1, licznik)

    # 3. Podział złoty

def zloty(f,a,b,d):
    licznik = 0
    k = ( math.sqrt(5) -1 ) / 2
    xl = b - k*(b-a)
    xr = a + k*(b-a)

    while( (b-a)>d ):
        licznik = licznik + 2
        if( f(xl)< f(xr)):
            b = xr
            xr = xl
            xl = b - k*(b-a)
        else:
            a = xl
            xl = xr
            xr = a + k*(b-a)

    x1 = (a +b)/2
    y1 = f(x1)
    return ( x1, y1, licznik)             

def zloty1(f,a,b,d):
    licznik = 0
    k = ( math.sqrt(5) -1 ) / 2
    xl = b - k*(b-a)
    fxl=f(xl)
    xr = a + k*(b-a)
    fxr=f(xr)
    while( (b-a)>d ):
        licznik = licznik + 2
        print("xl=",xl," fxl=",fxl,"; xr=",xr," fxr=",fxr)
        if( fxl< fxr):
            b = xr
            xr = xl
            fxr = fxl
            xl = b - k*(b-a)
            fxl = f(xl)
        else:
            a = xl
            xl = xr
            fxl = fxr
            xr = a + k*(b-a)
            fxr = f(xr)

    x1 = (a +b)/2
    y1 = f(x1)
    return ( x1, y1, licznik)     

def drukuj_wynik(wynik):
    print("wynik minimum dla x=",wynik[0],"y=",wynik[1],"ilość wywołań funkcji",wynik[2]);


dokladnosc=0.001
a = -10
b = 10

print("sposób naiwny")
print(find_min_naive(test_fun,a,b,dokladnosc))
print("sposób naiwny para")
drukuj_wynik(find_min_naive_para(test_fun,a,b,dokladnosc))
print("podział zwykły")
drukuj_wynik(podzial(test_fun,a,b,dokladnosc))
print("złoty podział")
drukuj_wynik(zloty(test_fun,a,b,dokladnosc))
print("złoty podział 1")
drukuj_wynik(zloty1(test_fun,a,b,dokladnosc))

