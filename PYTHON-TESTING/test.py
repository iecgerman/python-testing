# Curso de Unit Testing en Python

# Clase 2 - ¿Qué es el Testing en Software?


#  Código que va a ir a producción:
def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"] *product["discount"]
    return total

# Pruebas
def test_calculate_total_with_empty_list():
    # print("prueba")
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook",
            "price": 5,
            "discount": 0.9
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 4.5

def test_calculate_total_with_multiple_products():
    products = [
        {
            "name": "Book",
            "price": 10,
            "discount": 0.9
        },
        {
            "name": "Pen",
            "price": 2,
            "discount": 0.9
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 10.8


if __name__ == "__main__":
    # test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_products()
    


# https://ellibrodepython.com/assert-python 

"""
assert() en testing

La función assert() puede ser también muy útil para realizar testing de nuestro código, especialmente para test unitarios o unit tests. Imagínate que tenemos una función calcula_media() que como su nombre indica calcula la media de un conjunto de números.

def calcula_media(lista):
    return sum(lista)/len(lista)

En el mundo de la programación es muy importante probar o testear el software, para asegurarse de que está libre de errores. Gracias al uso de assert() podemos realizar estas comprobaciones de manera automática.

assert(calcula_media([5, 10, 7.5]) == 7.5)
assert(calcula_media([4, 8]) == 6)

Por lo que si hacemos que estas comprobaciones sean parte de nuestro código, podríamos proteger nuestra función, asegurándonos de que nadie la “rompa”.


"""
