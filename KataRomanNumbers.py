'''
Created on 05/12/2014

@author: A. Carlos del Pozo Muela

Funciona con numeros de 0 a 3999 (mayores a ese rango tienen una barra superior las letras)

v 3
''' 

class OutOfRange(ValueError): pass
class NotValidArabicNumeral(ValueError): pass
class NotValidRomanNumeral(ValueError): pass

valores = tuple(zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')))

def isValidRoman(numero):
    letras = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    for caracter in numero: 
            if caracter not in letras:
                return False
    return True

def getInt(numero):
    numero = numero.upper() #para numeros romanos en minuscula
    total =  i = 0
    try: #YA ES UN NUMERO ARABIGO
        numero =  int(numero)
        raise NotValidRomanNumeral('Debe introducir un número romano, no arábigo.')
        return numero
    except ValueError: #EFECTIVAMENTE SI ES UN NUMERO ROMANO A CONVERTIR
        if not isValidRoman(numero):
            raise NotValidRomanNumeral('Número romano no válido.') #CONTIENE CARACTERES NO VALIDOS
        for arabigo, romano in valores:
            while numero[i:i + len(romano)] == romano:
                total += arabigo
                i += len(romano)
        return total
    
    
def getRoman(numero):
    if(isinstance(numero,int)): #ES UN NUMERO ARABIGO, OK
        if not (0 < numero < 4000): #numero demasiado grande
            raise OutOfRange('Número fuera de rango. El número debe estar entre 1 y 3999')
        resultado = []
        for arabigo, romano in valores:
            contador = numero // arabigo
            resultado.append(romano * contador)
            numero -= arabigo * contador
        return ''.join(resultado)
    else: #NO ES UN NUMERO ARABIGO
        if(isValidRoman(numero)): #si es numero romano valido lo devuelvo tal cual
            return numero
        else:
            raise NotValidArabicNumeral('Número arábigo no válido. Tampoco se detectó que ya fuese un número romano válido.') #CONTIENE CARACTERES NO VALIDOS
            
    

            
            