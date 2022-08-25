age = 32
if age<2:
    human = "baby"
elif age>=2 and age<=4:
    human = "toddler"
elif age>=4 and age<=13:
    human = "kid"
elif age>=13 and age<=20:
    human = "teenager"
elif age>=20 and age<=65:
    human = "adult"
else:
    human = "elder"
print(f"the person is {human}")
