import math
import numpy as np

def test_fun(x,y):
    return (2*x*x*x)-(y*y*y)+(12*x*x)+27*y

def zloty2d(f,a,b,d,y):
    licznik = 0
    k = ( math.sqrt(5) -1 ) / 2
    xl = xb - k*(xb-xa)
    fxl=f(xl,y)
    xr = xa + k*(xb-xa)
    fxr=f(xr,y)
    while( (xb-xa)>d ):
        licznik = licznik + 1
        print("xl=",xl," fxl=",fxl,"; xr=",xr," fxr=",fxr)
        if( fxl > fxr):
            xb = xr
            xr = xl
            fxr = fxl
            xl = xb - k*(xb-xa)
            fxl = f(xl,y)
        else:
            xa = xl
            xl = xr
            fxl = fxr
            xr = xa + k*(xb-xa)
            fxr = f(xr,y)

    x1 = (xa +xb)/2
    y1 = f(x1,y)
    return ( x1, y1, licznik)   

def zloty1d(f,xa,xb,d,y):
    licznik = 0
    k = ( math.sqrt(5) -1 ) / 2
    xl = xb - k*(xb-xa)
    fxl=f(xl,y)
    xr = xa + k*(xb-xa)
    fxr=f(xr,y)
    while( (xb-xa)>d ):
        licznik = licznik + 1
        print("xl=",xl," fxl=",fxl,"; xr=",xr," fxr=",fxr)
        if( fxl > fxr):
            xb = xr
            xr = xl
            fxr = fxl
            xl = xb - k*(xb-xa)
            fxl = f(xl,y)
        else:
            xa = xl
            xl = xr
            fxl = fxr
            xr = xa + k*(xb-xa)
            fxr = f(xr,y)

    x1 = (xa +xb)/2
    y1 = f(x1,y)
    return ( x1, y1, licznik)     

def drukuj_wynik(wynik):
    print("wynik minimum dla x=",wynik[0],"y=",wynik[1],"ilość wywołań funkcji",wynik[2]);


dokladnosc=0.0001
x1 = -5
x2 = 0

print("złoty podział")
drukuj_wynik(zloty1d(test_fun,x1,x2,dokladnosc,3.0))

