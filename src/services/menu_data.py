from models.ingredient import Ingredient
from models.dish import Dish
import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_menu_from_csv(source_path)

    def load_menu_from_csv(self, source_path: str):
        csv_data = pd.read_csv(source_path)
        dishes = {}

        for row in csv_data.itertuples(index=False):
            name, price, ingredient_name, amount = row

            dish = dishes.get(name)
            if not dish:
                dish = Dish(name, price)
                dishes[name] = dish
                self.dishes.add(dish)

            ingredient = Ingredient(ingredient_name)
            dish.add_ingredient_dependency(ingredient, amount)
