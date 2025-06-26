"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    numeros = []
    for char in lista[:]:
        if isinstance(char, int):
            numeros.append(char)
            lista.remove(char)

    lista.extend(numeros)

    return lista


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == [
    "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    letras = [char for char in lista if isinstance(char, str)]
    numeros = [char for char in lista if isinstance(char, (int, float))]

    return letras + numeros


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, 'a', 1, 'b', 10, 'j']) == [
    'a', 'b', 'j', 3, 1, 10]
# NO MODIFICAR - FIN


# ###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    return sorted(lista, key=lambda x: 1 if type(x) in [int, float] else 0)


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == [
    "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


# def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
#     """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
#     Referencia: https://docs.python.org/3/library/functions.html#filter
#     """
#     pass # Completar


# # NO MODIFICAR - INICIO
# if __name__ == "__main__":
#     assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# # NO MODIFICAR - FIN


###############################################################################


# def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
#     """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
#     pass # Completar


# # NO MODIFICAR - INICIO
# if __name__ == "__main__":
#     assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# # NO MODIFICAR - FIN
