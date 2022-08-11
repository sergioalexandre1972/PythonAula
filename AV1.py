'''Faça um programa que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
 Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O programa deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

'''nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))

media = (nota1 + nota2)/2

    

if media >= 9 and  media <= 10: 
    print ('Media A')
    print ('A media é:{}' .format(media))
    print ('Aprovado')            
    
elif media >= 7.5 and  media < 9: 
    print ('Media B')
    print ('A media é: {}' .format(media))
    print ('Aprovado')

elif media >= 6 and  media < 7.5: 
    print ('Media C')
    print ('A media é: {}' .format(media))
    print ('Aprovado')             
elif media >= 4 and  media < 6: 
    print ('Media D')
    print ('A media é: {}' .format(media))
    print ('Reprovado')   
   
elif media >= 4 and  media < 6: 
    print ('Media E')
    print ('A media é:{}' .format(media))
    print ('Reprovado') '''
    
#Desenvolva um programa que leia um array de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.


'''listaChar = []
cons = 0
print ('Informe as Letras')
for i in range(10):
 	listaChar.append((input('Letra  '+ str(i+1) + ':\n')))
 	char = listaChar[i]
 	if(char not in ('a','e','i','o','u')):
 		cons += 1
    
print(cons)'''
lista = [[], []]
for i in range(1, 5):
    aux = str(input(f'Digite a {i}º Letra: '))
    
    aux = lista[i]
    if (aux not in ('a','e','i','o','u')):

        lista[0].append(aux)
    else:
        lista[1].append(aux)
lista[0].sort()
lista[1].sort()
print(f'''cons {lista[0]}
Vgal {lista[1]}''')




#Desenvolva um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.



'''def soma(a, b, c):
    sm = a + b + c
    return sm



n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

print('Soma entre os tres numeros é = ', soma(n1, n2, n3))'''
