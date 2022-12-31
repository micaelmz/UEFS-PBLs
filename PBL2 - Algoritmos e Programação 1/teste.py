'''
888888888888  88888888888  ad88888ba  888888888888  88888888888  ad88888ba
     88       88          d8"     "8b      88       88          d8"     "8b
     88       88          Y8,              88       88          Y8,
     88       88aaaaa     `Y8aaaaa,        88       88aaaaa     `Y8aaaaa,
     88       88"""""       `"""""8b,      88       88"""""       `"""""8b,
     88       88                  `8b      88       88                  `8b
     88       88          Y8a     a8P      88       88          Y8a     a8P
     88       88888888888  "Y88888P"       88       88888888888  "Y88888P"
'''
import difficulty_select
'''
difficulty = "easy"
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = []
for lista in matriz1:
    lista_auxiliar = []
    for item in lista:
        lista_auxiliar.append(item)
    matriz2.append(lista_auxiliar.copy())
    lista_auxiliar.clear()

print(matriz1)
print(matriz2)
linha1 = matriz2[0]
linha1.pop()

print(matriz1)
print(matriz2)


pos_p1 = 'y1'
def history(type, value, add=""):  # NAO FUNFA

    history_xy = {'x1': '',
                  'x2': '',
                  'x3': '',
                  'x4': '',
                  'x5': '',
                  'y1': '',
                  'y2': '',
                  'y3': '',
                  'y4': '',
                  'y5': ''}

    if type == 'round':
        return "Msg teste"
    elif type == "add_xy":
        history_xy[value] + add

    elif type == "read_xy":
        return history_xy




history('add_xy', pos_p1, history('round'))

print(history('read_xy', 0))
'''
print(f'┌────────────────────────────────────────────────┐\n'
          f'│{f"Como navegar através das pastas":^48}│\n'
          f'├────────────────────────────────────────────────┤\n'
          f'│{f" .─────._________     a navegação através das  ":^48}│\n'
          f'│{f" |               |    pastas e arquivos ocorre ":^48}│\n'
          f'│{f" |    ───────────┴─── por meio da execução de   ":^48}│\n'
          f'│{f" |   /              / linhas de comandos simples":^48}│\n'
          f'│{f" |  /              /  que podem ser digitadas em":^48}│\n'
          f'│{f" | /              /   qualquer momento abaixo da":^48}│\n'
          f'│{f" |/______________/    janela de exibição do app ":^48}│\n'
          f'└────────────────────────────────────────────────┘\n')

