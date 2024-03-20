# FOR, WHILE, (break,continue)
# for in -0 -- final

# 'in' no for devolve uma string e no 'if' devolve true or false
# for
for letra in "Ola mundo":
    print(letra)

prontuarios = ["SP01", "SP02", "SP03"]
               
for prontuario in prontuarios:
    print(prontuario)

# range(5) == 0, 1, 2, 3, 4
# range (start =0, stop, step=1) step é a quantidade de 'passos' dados
# list( range(10) )== 0,10, 2 --> 0, 2, 4 , 6 , 8 , 10

for i in range(5):
    print(i)

# 0 ate 1000
lista = list(range(1000))
print (lista)

# while

contador = 0
while contador < 5:
        print (contador)
        contador +=1

# break

comando = ''
while True
    if comando == 'sair':
        break
    if comando == '1':
        print('um')
    if comando == '2':
        print('dois')

# continue
numeros = [3, -1, 2, 0, -4, 5]
for numero in numeros:
    if numero <= 0:
        continue
    print(numero)

for numero in numeros:
    if numero > 0:
        print(numero)

# compreensao de listas

numeros = [1, 2, -3, 4, -5]


# expressao for item in lista
quadrados = [numero**2 for numero in numeros ]


# expressao for item in lista if condicao
positivos = [numero for numero in numeros if numero > 0]
elevad_quad = [numero** 2 for numero in numeros]