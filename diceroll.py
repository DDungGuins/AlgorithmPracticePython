from collections import Counter

dicelist = list(map(int, input().split()))
x = dicelist[0]
y = dicelist[1]
z = dicelist[2]

dicecounter = Counter(dicelist)

prize: int


def get_key(val):
    for key, value in dicecounter.items():
        if value == val:
            return key


if 3 in dicecounter.values():
    prize = 10000 + get_key(3) * 1000
elif 2 in dicecounter.values():
    prize = 1000 + get_key(2) * 100
else:
    prize = max(dicelist) * 100

print(prize)
