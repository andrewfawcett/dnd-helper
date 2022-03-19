from random import random


def main():
  crit = to_hit()
  damage(crit)

def to_hit():
  crit = False
  rolls = []
  for i in range(0, 2):
    rolls.append(int(random() * 20 + 1))

  max = rolls[0]
  for i in range(1, len(rolls)):
    if (rolls[i] > max):
      max = rolls[i]

  modifier = 8 - 3
  result = max + modifier

  print(rolls, end='')
  print(f" + {modifier} = {result}")
  if (max >= 19):
    print("CRITICAL HIT!")
    crit = True
  return crit

def damage(critical=False):
  dmg =  roll_dmg()
  
  modifier = 4
  rage= 2
  flank = 1
  gwm = 10
  crit = 10

  if (critical == True):
    dmg2 = roll_dmg()
    result = dmg + dmg2 + modifier + rage + flank + gwm + crit
    print(f"{dmg} + {dmg2} + {modifier} + {rage} + {flank} + {gwm} + {crit} = {result}")
  else:
    result = dmg + modifier + rage + flank + gwm
    print(f"{dmg} + {modifier} + {rage} + {flank} + {gwm} = {result}")

def roll_dmg():
  roll = int(random() * 10 + 1)
  if (roll == 1):
    print("Re-rolling 1 damage!")
    roll =  roll_dmg()
  return roll

# print(f"{dmg} damage!")

if __name__ == "__main__":
  main()
