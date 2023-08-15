# STRINGS
# SEQUENCIA DE CARACTERES

texto = 'Exemplo de texto'
a = texto[0]
print(a)
a = texto[-1]   # -1 ultima letra
print(a)

for c in texto:
    print(c)


# tamanho da string
print(len(texto))

# opeador in (busca)
if 'x' in texto:
    print('x existe na string')

if 'texto' in texto:
    print('texto existe na string')

# upper (converte para maiusculo)
print(texto.upper())

# lower (converte para minusculo)
print(texto.lower())

# title (iniciais de cada palavra em maiuscula)
print(texto.title())

#capitalize (coloca a inicial em maiuscula)
print(texto.capitalize())

# strip (remove os espaços em branco do inicio e do final)
texto = '    exemplo de texto    '
print(texto.strip())
print(texto.lstrip())   #remove espaço do começo
print(texto.lstrip())   #remove espaço do final

# count (conta a quantidade de vezes que um caracater aparece na string)
texto = 'exemplo de texto'
print(texto.count('e'))
print(texto.count('texto'))

# replace (substitui uma substring por outra)
texto = 'banana, laranja, maça'
texto = texto.replace('laranja', 'melancia')
print(texto)

# split (divide uma string de acordo com o separador) - retorna uma lista
texto = 'banana, laranja, maça'
frutas = texto.split(', ')   #retorna lista
print(frutas)


