# Final drilling modulo 3: Filtrando Datos

# nombres en listas

magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking"]
otros = ["Messi", "Einstein", "Pele", "Juanes"]

# funcion hace grandioso

def hacer_grandioso(lista):
    grandiosos = []
    for x in range(len(lista)):
        grandiosos.append('El gran '+lista[x])
    return(grandiosos)

# funcion que imprime las listas
        
def imprimir_nombres(lista):
    for x in lista:
        print(x)

# imprime todos los nombres

imprimir_nombres(magos)
imprimir_nombres(cientificos)
imprimir_nombres(otros)

# imprime los nombres grandiosos

imprimir_nombres(hacer_grandioso(magos))
imprimir_nombres(hacer_grandioso(cientificos))
imprimir_nombres(hacer_grandioso(otros))