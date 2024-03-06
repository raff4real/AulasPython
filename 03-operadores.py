# Operadores aritméticos 
# +, -, /, *, %

nota1 = 10
nota2 = 2

media = (nota1 + nota2) / 2

# potencia

numero = 2 ** 3 # elevar ao cubo
numero = 5 ** 2 # elevar ao quadrado

# logicos 
# and, or, not 


# acesso liberado = nao bloqueado, idade => 18, horario entre 8 e 18

bloqueado = False
idade = 20
hora_atual = 12
horario_comercial = hora_atual >= 8 and hora_atual <=18
maior_idade >= 18 

if not bloqueado and maior_idade >= and horario_comercial:
    print('Liberado')
else:
    print ('nao liberado')

# operadores de comparacao
# >, <, >=, <=, ==, =!

numeros = [1, 2, 3]
numeros = [1, 2, 3]

print (numeros == numeros2) # true 


# operador "is"
print (numero is numeros2) # false (pois sao duas unidades de memorias diferentes no armazenamento)

numeros3 = [1, 2, 3]
numeros4 = numeros3

print (numeros3 is numeros4) # true
print (numeros3 is not numeros4) # false

# in (boolean)

print ('a' in 'python') # false

# sim, nao, talvez

opcao_selecionada = '' 

if opcao_selecionada == 'sim' or opcao_selecionada == 'nao' or opcao_selecionada == 'talvez'
    print ('opcao valida')
else 
    print ('opcao invalida')

# OU

opcoes = ('sim', 'nao', 'talvez')
    
if opcao_selecionada in opcoes
    print ('opcao valida')
else
    print ('opcao invalida')