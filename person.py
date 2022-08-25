my_favorite_person = {'first_name':'bryan', 'last_name': 'almond', 'age': '43', 'city': 'lincoln',}
print(my_favorite_person['first_name'])
print(my_favorite_person['last_name'])
print(my_favorite_person['age'])
print(my_favorite_person['city'])
for person in my_favorite_person.values():
    print(person.title())
my_best_friend = {'first_name':'tulasi', 'last_name':'kandula','age':'33', 'city':'omaha'}
my_second_best_friend = {'first_name':'kavya', 'last_name':'sathyanarayana','age':'31', 'city':'omaha'}
best_friends = [my_best_friend, my_second_best_friend]
for best_friend in best_friends:
    print(best_friend)