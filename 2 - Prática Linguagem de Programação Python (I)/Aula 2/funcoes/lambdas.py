from functools import reduce

alunos = {
	{'nome': 'Ana', 'nota': 7.2},
	{'nome': 'Davi', 'nota': 9.4},
	{'nome': 'Lucas', 'nota': 8.1},
}

aluno_aprovado = lambda aluno: aluno['nota'] >= 7
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a+b

alunos_aprovados = filter(aluno_aprovado, alunos) # filtrou alunos aprovados do dicionarios
notas_alunos_aprovados = map(obter_nota, aluno_aprovado)
total = reduce(somar, notas_alunos_aprovados, 0)


print(total / len(alunos_aprovados))
print(alunos_aprovados)