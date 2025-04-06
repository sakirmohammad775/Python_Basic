actors=[
    {'name':'sabana','age':65},
    {'name':'sabia','age':34},
    {'name':'sibana','age':9},
    {'name':'habana','age':48},
]
juniors=filter(lambda actor:actor['age']<40,actors)
print(list(juniors))