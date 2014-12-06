'''
Created on 05/12/2014

@author: A. Carlos del Pozo Muela

Funciona con numeros de 0 a 3999 (mayores a ese rango tienen una barra superior las letras

v 2.0
''' 

def esNumeroRomanoValido(numero):
    letras = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    for caracter in numero: 
            if caracter not in letras:
                return False
    return True

def convierteRomanoArabigo(numero):
    
    numero = numero.upper() #para numeros romanos en minuscula
    valores = tuple(zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')))
    total =  i = 0
    try: #YA ES UN NUMERO ARABIGO
        numero =  int(numero)
        if(numero >= 4000):
            raise Exception()
        return numero
    except ValueError: #EFECTIVAMENTE SI ES UN NUMERO ROMANO A CONVERTIR
        if not esNumeroRomanoValido(numero):
            raise Exception() #CONTIENE CARACTERES NO VALIDOS
        for arabigo, romano in valores:
            while numero[i:i + len(romano)] == romano:
                total += arabigo
                i += len(romano)
        return total
    
    
def convierteArabigoaRomano(numero):
    if(isinstance(numero,int)): #ES UN NUMERO ARABIGO, OK
        if(numero > 3999): #numero demasiado grande
            raise Exception()
        
        valores = tuple(zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
            ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')))
        resultado = []
        for arabigo, romano in valores:
            contador = numero // arabigo
            resultado.append(romano * contador)
            numero -= arabigo * contador
        return ''.join(resultado)
    else: #NO ES UN NUMERO ARABIGO
        if(esNumeroRomanoValido(numero)): #si es numero romano valido lo devuelvo tal cual
            return numero
        else:
            raise Exception()

    
valores = ["900","MCMXCIX","XLILXII","XXXVIII","XLIX","","XMCXIZ","mmm"]
for i in range(0,len(valores)):
    try:
        print(convierteRomanoArabigo(valores[i]))
        print("---")
    except Exception:
        print("No se pudo calcular, tiene caracteres que no pertenecen al sistema numérico romano.")
        print("---")
        
print("==========================\n\n==========================")        
          
valores = [0,1,10,25,50,100,250,135, "XLM","XLZ",40000]
for i in range(0,len(valores)):
    try:
        print(convierteArabigoaRomano(valores[i]))
        print("---")
    except Exception:
        print("No se pudo calcular, es numero romano no valido o supera los 3999.")
        print("---")
    

            
    

            
            