from math import *
from random import *
from time import *
import sys

sys.set_int_max_str_digits(0)

def MultiplicaIngenuo(a, b):
    a = str(a)
    b = str(b)
    deslocamento = 1
    res = 0
    for i in range(len(b) - 1,-1, -1):
        resParcial = 0
        deslocInterno = 1
        carry = 0
        for j in range(len(a) - 1, -1, -1):
            prod = ((int(a[j]) * int(b[i])) + carry)
            esc = prod % 10
            carry = floor(prod / 10)
            resParcial += esc * deslocInterno
            deslocInterno *= 10
        res += (carry*deslocInterno+resParcial)*deslocamento
        deslocamento *= 10
    return res


def karatsuba (x, y):
    if x < 10 and y < 10:
        return x*y
    n = max(len(str(x)), len(str(y)))
    m = ceil(n/2) #Escolhe o maior valor caso n seja ímpar
    x1 = x // (10**m) #Arredonda divisão para baixo, selecionando só os m elementos mais significativos
    x0 = x % (10**m)
    y1 = y // (10**m)
    y0 = y % (10**m)
    z = karatsuba (x1+x0, y1+y0)
    x1y1 = karatsuba (x1, y1)
    x0y0 = karatsuba (x0, y0)
    xy = x1y1 * (10**(2*m)) + (z - x1y1 - x0y0)*(10**m) + x0y0
    return int(xy)

def bench_ingenuo(tamMax):
    ls = 10
    li = 99
    tam = 1
    qtd = 1
    while qtd <= tamMax:
        ts = time()
        a = randint(ls, li)
        b = randint(ls, li)
        qtd = floor(log10(a) + 1)
        MultiplicaIngenuo(str(a), str(b))
        print(str(qtd) + "," + str(time() - ts))
        tam *= 10
        ls *= tam
        li *= tam

def bench_karatsuba(tamMax):
    ls = 10
    li = 99
    tam = 1
    qtd = 1
    while qtd <= tamMax:
        ts = time()
        a = randint(ls, li)
        b = randint(ls, li)
        qtd = floor(log10(a) + 1)
        karatsuba(a, b)
        print(str(qtd) + "," + str(time() - ts))
        tam *= 10
        ls *= tam
        li *= tam


