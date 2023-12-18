import random

for i in range(3):
    print(random.randint(10, 20))


members = ('abbas', 'mahmut', 'kadirov', 'shu')
leader = random.choice(members)
print(leader)

# roll a dice program
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)


dice = Dice()
print(dice.roll())

