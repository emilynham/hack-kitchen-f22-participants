""" 
Given a list of ingredients with [ingredient, cost, minimum_required] and budget
Gordon needs this program to maximize the number of distinct ingredients that he can 
    purchase before purchasing more of a single ingredient, prioritizing ingredients that
    can have their minimum_required met (or closest to meeting) within the budget.
    - In cases where minimum_required cannot be met, minimize the amount of money used.
 
Return a shopping list of ingredients with the quantity that Gordon can buy. It should be in
    the form of [[ingredient, quantity], [ingredient, quantity], ...]. 
    - The list can be returned in any order.
    - If no ingredients can be purchased, return [] (an empty list)
Constraints: 
    - All prices are non-negative. 
    - Ingredient list will contain at least 1 ingredient.
    - This is only for a dessert service, so the ingredient list will be limited to 50 distinct ingredients.
    - Gordon is rich, so the budget is limited to a generous 500000
###############################################################################
Example 1
Ingredients:    [["flour", 3.59, 2],
                ["egg", 0.99, 6],
                ["baking soda", 3.49, 1]]
Budget: 13
Return: [["flour", 2], ["egg", 2], ["baking soda", 1]]
Explanation: 
    Prioritize one of each item first. Add 1 bag of flour, 1 egg, and 1 box of baking soda. 
    This totals 8.07. 
    Next, prioritize the other bag of flour since the minimum_requirement can be reached.
    This totals 8.07 + 3.59 = 11.66
    Finally, only the eggs are left to purchase. Purchase as many eggs as possible. In this case, only 1 
    more egg can be purchased to stay under budget.
    This totals 11.66 + 0.99 = 12.65 < 13
###############################################################################
Example 2
Ingredients:    [["flour", 3.59, 2],
                ["egg", 0.99, 6],
                ["baking soda", 3.49, 1]]
Budget: 7
Return: [["baking soda", 1], ["egg", 3]]
Explanation:
    Prioritize one of each item. Add 1 egg and 1 box of baking soda. 
    This totals 4.48
    Flour cannot be added to the shopping list because it would go over budget. (4.48 + 3.59 > 7)
    Since there is 7 - 4.48 = 2.52 left, purchase 2 more eggs. 
    This totals 6.46 < 7
"""

# Dessert service starts in 30 minutes, so complete the function asap and don't disappoint Gordon!
def get_ingredients(ingredients, budget):
    remainingBudget = budget
    output = {item[0]:0 for item in ingredients}
    
    # helper fx
    def sortByPrice(e):
        return e[1]

    def sortByPriceReq(e):
        return e[1] * e[2]

    # Sort ingredients by price first. Try to buy as many distinct ingredients
    ingredients.sort(key=sortByPrice)
    for item in ingredients:
        if item[1] < remainingBudget:
            remainingBudget -= item[1]
            item[2]-= 1
            output[item[0]] += 1
        else: 
            break
    print(output)
    print("---")

    # Sort ingredients by price * # req to try to meet minimum req
    ingredients.sort(key=sortByPriceReq)
    for item in ingredients:
        if sortByPriceReq(item) < remainingBudget:
            remainingBudget-=sortByPriceReq(item)
            output[item[0]] += item[2]
            item[2]=0
        else:
            break
    print(output)
    print("---")
    
    # Sort ingredients by price to buy remaining extra ingredients
    ingredients.sort(key=sortByPrice)

    for item in ingredients:
        while item[2] != 0 and remainingBudget > 0:
            if (remainingBudget - item[1] >= 0):
                remainingBudget-=item[1]
                output[item[0]] += 1
                item[2]-= 1
            else:
                break

    print(output)

    outputList = []
    for key in output:
        if (output[key] != 0):
            outputList += [[key, output[key]]]

    return outputList

if __name__ == '__main__':
    # Edit ingredients and budget to test your program
    ingredients = [["flour", 3.59, 2], ["egg", 0.99, 6], ["baking soda", 3.49, 1]]
    budget = 13
    print(get_ingredients(ingredients, budget))

    ingredients2 = [["flour", 3.59, 2], ["egg", 0.99, 6], ["baking soda", 3.49, 1]]
    budget2 = 7
    print(get_ingredients(ingredients2, budget2))