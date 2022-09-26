def hello_world():
    print("hello world")
    return "hello world"

def list_len(lista):
    return len(lista)

def dodawanie_lub_mnozenie(a,b):
    if a % 2 == 0:
        return a + b
    elif a % 3 == 0:
        return a / b
    else:
        return a * b

def dodawanie(a,b,c):
    return a+b+c

def wpisz_imie(self):
    
    imie = (input())

    return f'dzień dobry {imie}'

def pole_kola(r):
    return 3.14*r**2