from src.models.ingredient import (Ingredient, Restriction)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_one = Ingredient("queijo provolone")
    ingredient_two = Ingredient("tomate")
    ingrediente_three = Ingredient("queijo provolone")

    assert ingredient_one.name == "queijo provolone"
    assert ingredient_two.name == "tomate"

    assert ingredient_one.__repr__() == "Ingredient('queijo provolone')"
    assert ingredient_two.__repr__() == "Ingredient('tomate')"

    assert ingredient_one == ingrediente_three
    assert ingredient_one != ingredient_two

    assert hash(ingredient_one) == hash("queijo provolone")
    assert hash(ingredient_two) == hash("tomate")
    assert hash(ingredient_one) != hash(ingredient_two)

    assert ingredient_one.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
