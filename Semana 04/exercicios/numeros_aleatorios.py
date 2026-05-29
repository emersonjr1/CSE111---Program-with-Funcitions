import random

lista_aleatoria = ["laranja", "banana", 'Azul', "Python", "Brasil", "Mustang", "Relogio", "Celular"]

def main():
    lista = [12, 34, 1.99, 12.5, 594.9]
    print(lista)

    anexar_numeros_aleatorios(lista)
    print(lista)

    anexar_numeros_aleatorios(lista, 4)
    print(lista)

    lista2 = []
    print(lista2)

    anexar_palavras_aleatorias(lista2)
    print(lista2)

    anexar_palavras_aleatorias(lista2,3)
    print(lista2)


def anexar_numeros_aleatorios(lista_de_numeros, quantidade = 1):
    for x in range(quantidade):
        lista_de_numeros.append(round(random.uniform(1,100),2))
    

def anexar_palavras_aleatorias(lista_palavras, quantidade = 1):
    for y in range(quantidade):
        lista_palavras.append(random.choice(lista_aleatoria))



if __name__ == "__main__":
    main()