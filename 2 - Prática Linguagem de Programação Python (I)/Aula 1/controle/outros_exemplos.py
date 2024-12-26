pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']

for p in pessoas:
    for a in adjs:
        print(f'{p} é {a}!')


for i in [1, 2, 3]:
    pass # definir laço vazio

for i in range(1, 11):
    if i % 2:
        continue
    print(i) # vai sempre mostrar os valores pares


for i in range(1, 11):
    if i == 5:
        break  # sai do laço
