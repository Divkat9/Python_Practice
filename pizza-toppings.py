prompt = input("enter the topping you'd like on your pizza")
prompt += "\n(Enter 'quit' when finished)"
while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"I'd love to have {topping} on my pizza")