# shoping cart program 

foods=[]
prices=[]
total=0

while True:
    food= input("enter food to buy {q to quits}:")
    if food.lower()== "q":
        break
    else:
        price = float(input(f"enter the price of a {food}: Rs"))
        foods.append(food)
        prices.append(price)

print("---Shoping cart---")
for food in foods:
    print(food , end=" ")

for price in prices:
    total +=price
print()
print(f"your total is: Rs{total}")


