#!python3


def saudacao(nome = 'Pessoa', idade =20):
    print(f'Oi {nome} ! \nVocê nem parece ter {idade} anos')
    
# def saudacao():
# print(f'Boa tarde')

def soma_mult(a,b,x):
    return a + b * x

if __name__ == '__main__':
    saudacao('Ana', 20)

    b = soma_mult(1,2,3)
    print(b)
    