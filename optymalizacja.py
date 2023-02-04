import numpy as np


def fun1d(x):
    y = 2*np.sin(x)-((x*x)/10)
    return y

def zloty(fun, x1,x2, n_iter, es):
    r = (np.sqrt(5.0)-1.0)/2.0
    xl = x1
    xu = x2
    d = r * ( xu - xl )
    x1 = xl + d
    x2 = xu - d
    f1 = fun( x1 )
    f2 = fun( x2 )
    if ( f1 > f2 ):
        xopt = x1
        fx = f1
    else:
        xopt = x2
        fx = f2
    for i in range( n_iter):
        d = r * d
        if ( f1 > f2 ):
            xl = x2
            x2 = x1
            x1 = xl + d
            f2 = f1
            f1 = fun(x1)
            xopt = x1
            fx = f1
        else:
            xu = x1
            x1 = x2
            x2 = xu - d
            f1 = f2
            f2 = fun(x2)
            xopt = x2
            fx = f2
        if ( xopt != 0):
            ea = ( 1 - r )*np.abs( (xu - xl) / xopt )
        if ( ea < es):
            break
    return [i, xopt, fx]

def kwadrat(fun, x0,x1,x2, n_iter, es):
    f0 = fun( x0 )
    f1 = fun( x1 )
    f2 = fun( x2)

    for i in range (n_iter):
        x3 = ((f0*((x1*x1)-(x2*x2)))+(f1*((x2*x2)-(x0*x0)))+f2*((x0*x0)-(x1*x1)))
        x3 = x3 / ((2.0*f0*(x1-x2))+(2.0*f1*(x2-x0))+(2.0*f2*(x0-x1)))
        f3 = fun( x3 )
        print('iter:%d x0 = %f, x1 = %f, x2 = %f, -> x3 = %f' % ( i, x0, x1, x2, x3 ))
        print('iter:%d f0 = %f, f1 = %f, f2 = %f, -> f3 = %f' % ( i, f0, f1, f2, f3 ))
        if ( x3 < x1 ):
            x2 = x1
            x1 = x3
            f2 = f1
            f1 = f3
        else:
            x0 = x1
            x1 = x3
            f0 = f1
            f1 = f3
        

kwadrat( fun1d, 0, 1, 4, 6, 0.001)
iter, x, f = zloty( fun1d, 0, 4, 20, 0.001)
print('zloty podzial: iter=%d, x=%f, f(x)=%f' % ( iter, x, f )  )