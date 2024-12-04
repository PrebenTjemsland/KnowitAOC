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

current_refill = {
    "rice": 0,
    "peas": 0,
    "carrots": 0,
    "raindeer": 0
}

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

def refill(idx, currentTime=None):
    food_stock["rice"] += rice_refill[current_refill["rice"]]
    food_stock["peas"] += peas_refill[current_refill["peas"]]
    if idx > 30:
        food_stock["carrots"] += carrots_refill[current_refill["carrots"]]
        if current_refill["carrots"] < len(carrots_refill) - 1:
            current_refill["carrots"] += 1
        else:
            current_refill["carrots"] = 0
    if current_refill["rice"] < len(rice_refill) - 1:
        current_refill["rice"] += 1
    else:
        current_refill["rice"] = 0
    if current_refill["peas"] < len(peas_refill) - 1:
        current_refill["peas"] += 1
    else:
        current_refill["peas"] = 0
    if food_stock["raindeer"] == 0:
        if not currentTime:
            currentTime = idx
            return
        if currentTime == 50:
            if current_refill["raindeer"] < len(raindeer_refill) - 1:
                food_stock["raindeer"] += raindeer_refill[current_refill["raindeer"]]
                current_refill["raindeer"] += 1
                currentTime = None


while food_stock["pretzel"] > 0:
    items = list(food_stock.items())
    first_item_with_stock = next(((i, item) for i, item in enumerate(items) if item[1] > 0), None)
    first_index, (first_food, _) = first_item_with_stock
    second_index = (first_index + 1) % len(items)
    while food_stock[items[second_index][0]] <= 0 and second_index != first_index:
        second_index = (second_index + 1) % len(items)
    second_food = items[second_index][0]
    amount = get_amount(first_food)
    eat_food(food_stock, first_food, amount)
    amount = min(get_amount(second_food), 3)
    excluded_foods = ("raindeer", "pretzel")
    if first_food not in excluded_foods and second_food not in excluded_foods:
        eat_food(food_stock, second_food, amount)
    print("time: ", idx)
    print(food_stock)
    refill(idx)
    idx += 1