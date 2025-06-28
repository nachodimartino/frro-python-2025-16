"""Magic Methods"""

from __future__ import annotations
from typing import List


# NO MODIFICAR - INICIO
class Article:
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Article):
            return NotImplemented
        return self.name == other.name

    def __repr__(self) -> str:
        return f'Article("{self.name}")'


class ShoppingCart:
    def __init__(self, articles: List[Article] = None) -> None:
        if articles is None:
            self.articles = []
        else:
            self.articles = articles

    def add(self, article: Article) -> ShoppingCart:
        self.articles.append(article)
        return self

    def remove(self, remove_article: Article) -> ShoppingCart:
        new_articles = []
        for article in self.articles:
            if article != remove_article:
                new_articles.append(article)
        self.articles = new_articles
        return self

    def __str__(self) -> str:
        return str([article.name for article in self.articles])

    def __repr__(self) -> str:
        return f"ShoppingCart([{', '.join(repr(article) for article in self.articles)}])"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        return sorted(self.articles, key=lambda a: a.name) == sorted(other.articles, key=lambda a: a.name)

    def __add__(self, other: ShoppingCart) -> ShoppingCart:
        return ShoppingCart(self.articles + other.articles)


# NO MODIFICAR - INICIO
manzana = Article("Manzana")
pera = Article("Pera")
tv = Article("Television")

# Test de conversión a String
assert str(ShoppingCart().add(manzana).add(pera)) == "['Manzana', 'Pera']"

# Test de reproducibilidad
carrito = ShoppingCart().add(manzana).add(pera)
assert carrito == eval(repr(carrito))

# Test de igualdad
assert ShoppingCart().add(manzana) == ShoppingCart().add(manzana)

# Test de remover objeto
assert ShoppingCart().add(tv).add(pera).remove(tv) == ShoppingCart().add(pera)

# Test de igualdad con distinto orden
assert ShoppingCart().add(tv).add(pera) == ShoppingCart().add(pera).add(tv)

# Test de suma
combinado = ShoppingCart().add(manzana) + ShoppingCart().add(pera)
assert combinado == ShoppingCart().add(manzana).add(pera)

# NO MODIFICAR - FIN
