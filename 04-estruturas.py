# if, if/elif/else, ternario, match

# a estrutura do if: 

#condição do if
#   codigo do if
#   codigo do if
#resto do codigo

# if/else

if idade >=18
    print ('maior')
else
    print ('menor')

# elif (ignora o resto do codigo assim q acha a condicao)
# melhor do que por varios if em sequencia

if idade <= 12:
    print ('kid')
elif idade <= 17:
    print ('chato')
elif idade <= 59:
    print ('veio') 

#operador ternario

if idade >= 18:
    status = 'maior'
else:
    status = 'menor'

status = 'maior' if idade >= 18 else 'menor'

#usuario passa o dia (int)
#devolve string nome 
# 1 - domingo, 2 - segunda... 7 - sabado

dia = 4

# dicionario (util para nao ficar repetindo if's)
dias ={
    1 :'Domingo',
    2 :'segunda',
    3 :'terça',
    4 :'quarta',
    5 :'quinta',
    6 :'sexta',
    7 :'sábado',
}


if dia in dias:
    print(dias(dia))

dia = 2
match dia:
    case 1: 
        print('Domingo')
    case 2: 
        print('segunda')
    case 3: 
        print('terça')
    case 4: 
        print('quarta')
    case 5: 
        print('quinta')
    case 6: 
        print('sexta')
    case 7: 
        print('sábado')
    case _: 
        print('inválido')

match dia:
    case 1 | 7:
        print('Fim de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('dia util')
    case _:
        print('inválido')