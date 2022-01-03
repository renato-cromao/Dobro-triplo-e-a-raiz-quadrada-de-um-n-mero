titulo = ('EXERCÍCIO 006')
print('*'*40)
print('{:^40}'.format(titulo))
print('*'*40)
print('')
print('''Informe um número e veja qual será o dobro, o triplo
e a raiz quadrada dele.''')
print('')
n1 = int(input('Digite um número: '))

print('''
O número informado foi: {}
O dobro desse número é: {}
O triplo desse número é: {}
A raiz quadrada desse número é:{:.2f}
'''.format(n1, n1*2, n1*3, n1**(1/2)))

print('Tenha bons estudos!!!')