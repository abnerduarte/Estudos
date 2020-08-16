   
'''def eh_primo():
    numero_natural = int(input('Digite um numero: '))
    count = 0 
    for i in range (1, numero_natural + 1): 
        if numero_natural % i == 0: 
            count += 1 
    if count == 2: 
        print ('True')
    else: 
        print ('False')

eh_primo()'''

'''def lista_de_primos(): 
    numero_natural = int(input('Digite um numero: '))
    lista = []
    for i in range (1, numero_natural):
        count = 0 
        for x in range (1, i + 1):
            if i % x == 0:  
                count += 1
        if count <= 2: 
            lista.append(i)
    print(lista)

lista_de_primos()'''


'''def eh_armstrong():
    numero = int(input('Digite um numero: '))
    numero_n = numero
    quant_digito = len(str(numero))
    soma_digitos = 0
    while numero > 0:
        ult_digito = (numero % 10) ** quant_digito
        soma_digitos += ult_digito
        numero = numero // 10
    if numero_n == soma_digitos:
        print('True')
    else:
        print('False')

eh_armstrong()'''

'''def lista_armstrong():
    numero = int(input('Digite um numero: '))
    lista_armstrong = []
    for i in range(1 ,numero + 1):
        soma_digitos = 0
        quant_digito = len(str(i))
        numero_n = i
        while numero_n > 0:
            digit = (numero_n % 10) ** quant_digito
            soma_digitos += digit
            numero_n //= 10
        if i == soma_digitos:
            lista_armstrong.append(i)
    print(lista_armstrong)

lista_armstrong()'''


'''def eh_perfeito():
    numero = (int(input('Digite um numero : ')))
    count = 0
    for i in range (1, numero): 
        if numero % i == 0:
            count += i 
    if count == numero:
        print('verdade')
    else:
        print('falso')
           
                
        
eh_perfeito()'''

def lista_de_perfeitos():
    numero = int(input('digite: '))
    lista = []
    for x in range(1, numero):
        count = 0 
        for i in range (1, x): 
            if x % i == 0: 
                count += i 
        if count == x:
            lista.append(x)
    print(lista)         

lista_de_perfeitos()      

   
    
