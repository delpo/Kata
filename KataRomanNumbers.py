'''
Created on 05/12/2014

@author: A. Carlos del Pozo Muela

Funciona con numeros de 0 a 3999 (mayores a ese rango tienen una barra superior las letras)

v 4
''' 

class OutOfRange(ValueError): pass
class NotValidArabicNumeral(ValueError): pass
class NotValidRomanNumeral(ValueError): pass

valores = tuple(zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')))

def isValidRoman(numero):
    for caracter in numero:
        ok = False
        for tupla in valores:
            if(caracter==tupla[1]): ok = True
        if not ok: return False
    return True

def getInt(numero):
    if not isinstance(numero, str):
        raise NotValidRomanNumeral('Debe introducir una cadena con un número romano')
    if not numero:
        raise NotValidRomanNumeral('Debe introducir un número romano, usted no pasó ningún valor')
    if not isValidRoman(numero):
        raise NotValidRomanNumeral('Número romano no válido.') #CONTIENE CARACTERES NO VALIDOS
    numero = numero.upper() #para numeros romanos en minuscula
    total =  i = 0
    for arabigo, romano in valores:
        while numero[i:i + len(romano)] == romano:
            total, i = total+arabigo, i+len(romano)
    return total
    
def getRoman(numero):
    if int(numero) != numero:
        NotValidArabicNumeral('Número arábigo no válido.')
    if not (0 < numero < 4000): #numero demasiado grande
        raise OutOfRange('Número fuera de rango. El número debe estar entre 1 y 3999')
    resultado = []
    for arabigo, romano in valores:
        contador = numero // arabigo
        resultado.append(romano * contador)
        numero -= arabigo * contador
    return ''.join(resultado)
            