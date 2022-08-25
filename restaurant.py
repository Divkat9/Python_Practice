class Restaurant:
    def __init__(self, restaurant_name, restaurant_cuisine, number_served):
        self.restaurant_name = restaurant_name
        self.restaurant_cuisine = restaurant_cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        print (f"{self.restaurant_name} has great reviews")
        print(f"{self.restaurant_cuisine} is so authentic")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!!")

    def set_number_served(self, members):
        self.number_served = members
    
    def increment_number_served(self, members):
        self.number_served += members

my_restaurant = Restaurant('Bawarchi', 'Indian', 0)
print(f"My restaurant's name is {my_restaurant.restaurant_name}") 
print(f"My restaurant is famous for {my_restaurant.restaurant_cuisine} cuisine")
print(f"my restaurant served {my_restaurant.number_served} customers")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(35)
print(f"my restaurant served {my_restaurant.number_served} customers")
my_restaurant.increment_number_served(100)
print(f"my restaurant served {my_restaurant.number_served} customers")