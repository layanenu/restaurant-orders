from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    lasanha_presunto = Dish("lasanha presunto", 25.90)
    lasanha_beringela = Dish('lasanha beringela', 27.00)

    assert lasanha_presunto.name == 'lasanha presunto'
    assert lasanha_presunto.price == 25.90

    assert lasanha_presunto == lasanha_presunto
    assert str(lasanha_presunto) == "Dish('lasanha presunto', R$25.90)"

    assert hash(lasanha_presunto) == hash(lasanha_presunto)
    assert hash(lasanha_presunto) != hash(lasanha_beringela)

    ingredient = Ingredient('presunto')
    lasanha_presunto.add_ingredient_dependency(ingredient, 50)
    assert lasanha_presunto.get_ingredients() == {ingredient}
    assert lasanha_presunto.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED
    }

    ingredient2 = Ingredient('beringela')
    lasanha_beringela.add_ingredient_dependency(ingredient2, 20)
    assert lasanha_beringela.get_ingredients() == {ingredient2}
    assert lasanha_beringela.get_restrictions() == set()

    with pytest.raises(TypeError):
        Dish("dish", "price")
    with pytest.raises(ValueError):
        Dish('dish', 0)
