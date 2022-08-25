def sandwich(first, last, **customer):
    customer['first_name'] = first
    customer['last_name'] = last
    return customer
    
make_sandwich = sandwich('divya', 'katakam', flavor='veg and cheese',
toppingone = 'diced fried potatoes',
toppingtwo ='sweet peppers',
toppingthree = 'mozerella cheese')
print(make_sandwich)