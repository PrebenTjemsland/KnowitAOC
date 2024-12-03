from logging import error

food_stock = {
    "rice": 100,
    "peas": 100,
    "carrots": 100,
    "raindeer": 100,
    "pretzel": 100
}

rice_refill = [0, 0, 1, 0, 0, 2]
peas_refill = [0, 3, 0, 0]
carrots_refill = [0, 1, 0, 0, 0, 8]
raindeer_refill = [100, 80, 40, 20, 10]

vegetables = ["rice", "peas", "carrots"]
idx = 1

def eat_food(food_dict, food, amount):
    actual_amount = min(amount, food_dict[food])
    food_dict[food] -= actual_amount

def get_amount(food):
    if food in vegetables:
        return 5
    elif food == "raindeer":
        return 2
    elif food == "pretzel":
        return 1
    else:
        error("wrong food")
        return 0

while food_stock["pretzel"] > 0:
    items = list(food_stock.items())
    first_item_with_stock = next(((i, item) for i, item in enumerate(items) if item[1] > 0), None)

    first_index, (first_food, _) = first_item_with_stock
    amount = get_amount(first_food)
    eat_food(food_stock, first_food, amount)

    second_index = (first_index + 1) % len(items)
    while food_stock[items[second_index][0]] <= 0 and second_index != first_index:
        second_index = (second_index + 1) % len(items)
    second_food = items[second_index][0]
    amount = min(get_amount(second_food), 3)
    eat_food(food_stock, second_food, amount)
    print("time: ", idx)
    print(food_stock)
    idx += 1