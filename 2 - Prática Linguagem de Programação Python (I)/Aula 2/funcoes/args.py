def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total

def resultado_final(**kwargs):
    status = 'aprovado' if kwargs['nota'] >=7 else 'reprovado'
    print(kwargs['nome'])
    print(kwargs['nota'])

    return f'{kwargs["nome"]} foi {status}'