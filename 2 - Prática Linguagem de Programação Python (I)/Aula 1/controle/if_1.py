nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado (y/n): ') == 'y' else False

if nota >= 9 and comportado:
    print('Parabens')
elif nota>=7:
    print('Aprovado')
elif nota>=5.5:
    print('Recuperacao')
elif nota>=3.5:
    print('Recuperacao + Trabalho')
else:
    print('Reprovado')


print(nota)