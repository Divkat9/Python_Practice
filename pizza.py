pizzas = ['pepperoni', 'jalapeno-pineapple', 'cheese']
print (pizzas)
for pizza in pizzas:
    print ("i like" + " "+ pizza.title())
print ("I really do love pizza")
friend_pizzas = pizzas
print (friend_pizzas)
pizzas.append('bacon')
print (pizzas)
friend_pizzas.append('hawaiian')
print (friend_pizzas)
