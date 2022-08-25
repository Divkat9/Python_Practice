sandwich_orders = ['cheese', 'ham', 'chicken', 'tofu', 'pastrami', 'pastrami', 'pastrami']
print (sandwich_orders)
finished_sandwiches = []
available_sandwich_orders = []
for sandwich in sandwich_orders:
    print (f"I made your {sandwich} sandwich")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
        continue
while sandwich_orders:
    finished_orders = sandwich_orders.pop()
    print(f"the completed orders are {sandwich_orders}")
    finished_sandwiches.append(finished_orders)
    print(f"the finished sandwiches are {finished_sandwiches}")