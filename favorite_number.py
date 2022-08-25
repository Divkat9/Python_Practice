key_words = {'if':'conditional', 'for':'used for repetetive needs', 'list':'collection of objects',}
print(f"this is used for {key_words['if']}")
print(f"for is used for {key_words['for']}")
print(f"list is used for {key_words['list']}")

fav_numbers = {'divya':'9', 'bryan':'3'}
for name, number in fav_numbers.items():
    print(f"{name}'s favorite number is {number}")