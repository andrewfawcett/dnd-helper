from random import random

def main():
    roll = roll_d(10)
    damage(
        base=10,
        rage=True,
        flank=True,
        gwm=True, 
        crit=True
    )
    while (True):
        print("(Q)uit")
        value = input("Enter value: ")
        if (value.lower() == "q"): break



def damage(base, rage=False, flank=False, gwm=False, crit=False):

    MOD_DMG = 4
    RAGE_DMG= 2
    FLANK_DMG = 1
    GWM_DMG = 10
    CRIT_DMG = 10

    dmg = [base, MOD_DMG]
    if (rage): dmg.append(RAGE_DMG)
    if (flank): dmg.append(FLANK_DMG)
    if (gwm): dmg.append(GWM_DMG)
    if (crit): dmg.append(CRIT_DMG)

    total = 0
    for i in range(0, len(dmg)):
        total += dmg[i]
        print(dmg[i], end = "")
        if (i < len(dmg) - 1):
            print(" + ", end = "")
    print(f" = {total}")


def roll_d(d=6):
    return int(random() * 10 + 1)

if __name__ == "__main__":
    main()
