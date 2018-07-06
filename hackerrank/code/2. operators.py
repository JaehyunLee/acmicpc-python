def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    return round(meal_cost + tip + tax)


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    total = solve(meal_cost, tip_percent, tax_percent)

    print('The total meal cost is {0} dollars.'.format(total))
