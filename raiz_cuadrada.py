def f(x,n):
    return x**2-n

entrada = int(input('Introduce el numero: '))
resultado = 0
lim_inf = 0
lim_sup = entrada
tolerancia = 0.000000000001

while abs(f(resultado,entrada)) > tolerancia:
    resultado = (lim_inf + lim_sup) / 2
    # print(resultado)
    if f(resultado,entrada) < 0:
        lim_inf = resultado
    else:
        lim_sup = resultado
    
print(f'La raiz cuadrada de {entrada} es : ',resultado)

     

