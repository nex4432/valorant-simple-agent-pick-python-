agent = input("what agents are u gonna play? ")

if agent in (
    "Astra",
    "Breach",
    "Brimstone",
    "Chamber",
    "Clove",
    "Cypher",
    "Deadlock",
    "Fade",
    "Gekko",
    "Harbor",
    "Iso",
    "Jett",
    "KAY/O",
    "Killjoy",
    "Neon",
    "Omen",
    "Phoenix",
    "Raze",
    "Reyna",
    "Sage",
    "Skye",
    "Sova",
    "Tejo",
    "Veto",
    "Vyse",
    "Waylay",
    "Yoru"
):
    print(agent + " locked in")
else:
    print("error: agent doesn't exist ")

import random

agents = [
    "Astra",
    "Breach",
    "Brimstone",
    "Chamber",
    "Clove",
    "Cypher",
    "Deadlock",
    "Fade",
    "Gekko",
    "Harbor",
    "Iso",
    "Jett",
    "KAY/O",
    "Killjoy",
    "Neon",
    "Omen",
    "Phoenix",
    "Raze",
    "Reyna",
    "Sage",
    "Skye",
    "Sova",
    "Tejo",
    "Veto",
    "Vyse",
    "Waylay",
    "Yoru"
]

import time

time.sleep(5)

player2 = random.choice(agents)
agents.remove(player2)
player3 = random.choice(agents)
agents.remove(player3)
player4 = random.choice(agents)
agents.remove(player4)
player5 = random.choice(agents)
agents.remove(player5)

print("player2:", player2)
time.sleep(2)
print("player3:", player3)
time.sleep(3)
print("player4:", player4)
time.sleep(2)
print("player5:", player5)
time.sleep(1)


print("all players are ready")
print("game starts in 10 seconds")

time.sleep(1)


for i in range (10, 0, -1):
    print(i)
    time.sleep(1)

print("game started!!")