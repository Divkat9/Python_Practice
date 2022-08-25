def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('divya', 'katakam', favorite_food = 'biryani', state_of_mind = 'not great', reason = 'feel like shes not good enough')
print(user_profile)