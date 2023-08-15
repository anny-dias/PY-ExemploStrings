# LISTAS
# Estruturas de dados (sequencia de itens)
# delimitados por colchetes [ ]

lista = [3, 5, 7, 8]
print(lista)

# lista são heterogêneas (itens de tipos diferentes)
lista = [3, 2.66, 'abc', 4, 'Anny']
print(lista)

# listas são mutáveis (podem ser alteradas)
lista = [3, 5, 7, 8]
lista[0] = 100
print(lista)

# listas são acessadas pelos indices (começa sempre no indice zero)
print(lista[0])

# indices negativos começam sempre em -1 (a partir do último item)
lista = [3, 5, 7, 8]
print(lista[-1])

# len - retorna o tamanho da lista
print(len(lista))

# append - adiciona um item no final da lista
lista.append(300)
lista.append(400)
print(lista)

# insert(indice, item) - adiciona um item em uma posição específica da lista
lista.insert(3, 99)
print(lista)

# pop() - remove o ultimo elemento da lista
lista = [3, 7, 5, 10]
lista.pop()
print(lista)

# pop(indice) - remove o item do indice específico
lista.pop(1)
print(lista)

# remove - remove somente o primeiro valor igual ao passado como parâmetro
lista = [3, 7, 5, 10, 5, 5]
lista.remove(5)
print(lista)

# operador in (verificar se o valor existe ou nao na lista)
lista = [3, 7, 5, 10, 5, 5]
if 9 in lista:
    lista.remove(5)
print(lista)

# count - conta quantas vezes um item aparece na lista
lista = [3, 7, 5, 10, 5, 5]
print(lista.count(5))

# index - retorna o indice de um elemento
print(lista.index(5))

# sort - ordena uma lista
lista = [3, 7, 5, 10, 5, 5]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista = ['Maria', 'Ana', 'Paulo', 'Fernando']
lista.sort()
print(lista)

# max - retorna o maior elemento da lista
lista = [3, 5, 10, 1]
print(max(lista))

# min - retorna o menor elemento da lista
print(min(lista))

# som - retorna o somatótio da lista
print(sum(lista))

# media
media = sum(lista) / len(lista)
print(media)

# preencher lista com itens informados pelo usuário
lista = []
for i in range(5):
    n = int(input('Digite um número inteiro: '))
    lista.append(n)
print(lista)

lista = []
while True:
    n = int(input('Digite um número (-1 para sair): '))
    if n == -1:
        break
    lista.append(n)
print(lista)

# percorrer itens da lista
lista = [4, 6, 2, 3, 10]
cont = 0
for item in lista:  #for cada item na lista...
    if item % 2 == 0 :
        cont += 1
print(f'Quantidade de pares {cont}')

# percorrer indices da lista
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i]
print(lista)

# concatenação (juntar listas)
lista1 = [3, 5, 6]
lista2 = ['Anny', 'Lu', 'Cams']
lista3 = lista1 + lista2
print(lista3)

