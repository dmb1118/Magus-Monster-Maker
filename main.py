import Ability
from monster import *
from Ability import *
import math
from tools import *


def print_monster_sheet():
    f = open(f"C:/Users/devon/" +
             f"Desktop/MagusMonsters/Lvl{monster.lvl}_{monster.mtype}_" + f"{monster.m_name}.txt", "w")
    f.write(
        "Name: " + monster.m_name +
        "\nLevel: " + str(monster.lvl) +
        "\nType: " + monster.mtype +
        "\nTier: " + monster.tier +
        "\n" + ("-" * 25) +
        "\nHealth: " + str(monster.hp) +
        "\nAura Rating: " + str(monster.aura) +
        "\nBase Speed: " + str(monster.speed) + "'" +
        "\nPD: " + str(monster.pd) +
        "\nMD: " + str(monster.md) +
        "\nMana: " + str(monster.mana) +
        "\nMelee Attack Bonus: " + str(monster.attack_bonus) +
        "\n" + ("-" * 25) +
        "\nStrength: " + str(monster.strength) +
        "\nDexterity: " + str(monster.dex) +
        "\nStamina: " + str(monster.sta) +
        "\n" + ("-" * 25) +
        "\nIntellect: " + str(monster.intellect) +
        "\nWillpower: " + str(monster.will) +
        "\nCharisma: " + str(monster.cha) +
        "\n" + ("-" * 25) +
        "\nFocus: " + str(monster.focus) +
        "\nTalent: " + str(monster.talent) +
        "\nSkill: " + str(monster.skill) +
        "\n" + ("-" * 25) +
        "\nAbilities: "
    )
    for y in monster.m_abilities:
        f.write("\n" + y.name + " : " + y.effect)
    f.close()


static_level = -2
static_random = 0
static_choice = ""
static_count = 1
static_seed = 0
running = True
while running:
    static_seed = str(rng(9)) + str(rng(9)) + str(rng(9)) + str(rng(9)) + str(rng(9))
    choice = str(input("Would you like to create new monsters? Y/N\n"))
    if choice == "y" or choice == "Y":
        repeat_num = int(input("How many monsters would you like to create?\n"))
        repeater = 0
        tier = ""
        mtype = ""
        for repeater in range(repeat_num):
            repeater += 1
            if static_choice == "":
                static_choice = str(input("Do you wish to randomize or submit information manually? Random/Manual\n"))
            if static_choice == "Manual":
                mlvl = int(input("What level monster do you wish to create?\n"))
                mtype = str(input("What type of monster would you like to create?\n"
                                  "Types: Animal, Celestial, Construct, Dragon, Fey, Fiend, Magical Beast, Spirit\n"))
                tier = str(input(f"What tier {mtype} do you wish to create?\n"
                                 "Tiers: Mob, Troop, Normal, Elite, Boss\n"))
            else:
                if static_level == -2:
                    choice = str(input("Do you wish to set the level for all of the monsters? Y/N\n"))
                    if choice == "y" or choice == "Y":
                        static_level = int(input("Please enter the desired monster level: \n"))
                    else:
                        static_level = -1  # Causes the loop not to ask each time during the current program run
                if static_level >= 0:
                    mlvl = static_level
                else:
                    mlvl = rng(10)

                ran_num = rng(8)
                if ran_num == 1:
                    mtype = "Animal"
                elif ran_num == 2:
                    mtype = "Celestial"
                elif ran_num == 3:
                    mtype = "Construct"
                elif ran_num == 4:
                    mtype = "Dragon"
                elif ran_num == 5:
                    mtype = "Fey"
                elif ran_num == 6:
                    mtype = "Fiend"
                elif ran_num == 7:
                    mtype = "Magical Beast"
                elif ran_num == 8:
                    mtype = "Spirit"

                ran_num = rng(5)
                if ran_num == 1:
                    tier = "Mob"
                elif ran_num == 2:
                    tier = "Troop"
                elif ran_num == 3:
                    tier = "Normal"
                elif ran_num == 4:
                    tier = "Elite"
                elif ran_num == 5:
                    tier = "Boss"

            attr_pts = 0
            mag_pts = 0
            hp_mod = 0
            ability_pts = 0
            hp = 0
            speed = 30
            fly_speed = 0
            aura = 0
            pd = 0
            md = 0
            mana = 0
            attack_bonus = 0

            if tier == "Mob":
                attr_pts = 2 + (2 * mlvl)
                mag_pts = 3 + (2 * mlvl)
                ability_pts = math.ceil(mlvl * .5)  # every odd num level
                hp_mod = 2
            elif tier == "Troop":
                attr_pts = 4 + (2 * mlvl)
                mag_pts = 6 + (2 * mlvl)
                ability_pts = 1 + math.ceil(mlvl * .5)
                hp_mod = 4
            elif tier == "Normal":
                attr_pts = 6 + (2 * mlvl)
                mag_pts = 9 + (2 * mlvl)
                ability_pts = 2 + math.ceil(mlvl * .5)
                hp_mod = 6
            elif tier == "Elite":
                attr_pts = 8 + (2 * mlvl)
                mag_pts = 9 + (2 * mlvl)
                ability_pts = 3 + math.ceil(mlvl * .5)
                hp_mod = 8
                mana += 10
            elif tier == "Boss":
                attr_pts = 10 + (2 * mlvl)
                mag_pts = 12 + (2 * mlvl)
                ability_pts = 4 + math.ceil(mlvl * .5)
                hp_mod = 10
                mana += 20

            phys_pts = math.ceil(attr_pts * .5)
            attr_pts -= phys_pts
            ment_pts = attr_pts
            strength = 1
            dex = 1
            sta = 1
            m_f_style = 0
            ran_value = rng(3)
            if ran_value == 1:  # 1 == Offensive fighting style
                temp = math.ceil(phys_pts * .5)
                strength += temp
                phys_pts -= temp

                temp = rng(phys_pts)
                if temp >= (phys_pts * .5):
                    temp = math.floor(phys_pts * .5)
                dex += temp
                phys_pts -= temp

                temp = phys_pts
                sta += temp
                phys_pts -= temp
            if ran_value == 2:  # 2 == Defensive fighting style
                temp = math.floor(phys_pts * .25)
                strength += temp
                phys_pts -= temp

                temp = rng(phys_pts)
                if temp >= (phys_pts * .5):
                    temp = math.floor(phys_pts * .5)
                dex += temp
                phys_pts -= temp

                temp = phys_pts
                sta += temp
                phys_pts -= temp
            if ran_value == 3:  # 3 == Balanced fighting style
                temp = math.floor(phys_pts * .33)
                strength += temp
                phys_pts -= temp

                temp = math.floor(phys_pts * .33)
                dex += temp
                phys_pts -= temp

                temp = phys_pts
                sta += temp
                phys_pts -= temp

            intellect = 1
            will = 1
            cha = 1
            if ran_value == 1:  # 1 == Offensive fighting style
                temp = math.ceil(ment_pts * .5)
                intellect += temp
                ment_pts -= temp

                temp = rng(ment_pts)
                if temp >= (ment_pts * .5):
                    temp = math.floor(ment_pts * .5)
                will += temp
                ment_pts -= temp

                temp = ment_pts
                cha += temp
                ment_pts -= temp
            if ran_value == 2:  # 2 == Defensive fighting style
                temp = math.floor(ment_pts * .25)
                intellect += temp
                ment_pts -= temp

                temp = rng(ment_pts)
                if temp >= (ment_pts * .5):
                    temp = math.floor(ment_pts * .5)
                will += temp
                ment_pts -= temp

                temp = ment_pts
                cha += temp
                ment_pts -= temp
            if ran_value == 3:  # 3 == Balanced fighting style
                temp = math.floor(ment_pts * .33)
                intellect += temp
                ment_pts -= temp

                temp = math.floor(ment_pts * .33)
                will += temp
                ment_pts -= temp

                temp = ment_pts
                cha += temp
                ment_pts -= temp

            focus = 1
            temp = rng(mag_pts)
            if temp >= (mag_pts * .5):
                temp = math.ceil(mag_pts * .5)
            focus += temp
            mag_pts -= temp

            talent = 1
            temp = rng(mag_pts)
            if temp >= (mag_pts * .5):
                temp = math.floor(mag_pts * .5)
            talent += temp
            mag_pts -= temp

            skill = 1
            temp = mag_pts
            skill += temp
            mag_pts -= temp

            m_abilities = []
            temp_ability_list = ability_objects.copy()

            if mtype == "Animal":
                focus = 0
                talent = 0
                skill = 0
                strength += 1
                dex += 1
                sta += 1

                no_magic_list = [x for x in temp_ability_list if x.magical != 1]
                temp_ability_list = no_magic_list.copy()

            if mtype == "Celestial" and ability_pts >= 1:
                var = first(x for x in temp_ability_list if x.name == "Flying")
                m_abilities.append(var)
                temp_ability_list.pop(temp_ability_list.index(var))
                ability_pts -= var.cost
                if ability_pts >= 2:
                    var = first(x for x in temp_ability_list if x.name == "Healing Touch")
                    m_abilities.append(var)
                    temp_ability_list.pop(temp_ability_list.index(var))
                    ability_pts -= var.cost
                if ability_pts >= 2:
                    var = first(x for x in temp_ability_list if x.name == "Invisibility")
                    m_abilities.append(var)
                    temp_ability_list.pop(temp_ability_list.index(var))
                    ability_pts -= var.cost
                if ability_pts >= 2:
                    var = first(x for x in temp_ability_list if x.name == "Smite")
                    m_abilities.append(var)
                    temp_ability_list.pop(temp_ability_list.index(var))
                    ability_pts -= var.cost
                if ability_pts >= 3:
                    var = first(x for x in temp_ability_list if x.name == "Teleport")
                    m_abilities.append(var)
                    temp_ability_list.pop(temp_ability_list.index(var))
                    ability_pts -= var.cost

            if mtype == "Construct":
                var = first(x for x in temp_ability_list if x.name == "Construct Body")
                m_abilities.append(var)
                temp_ability_list.pop(temp_ability_list.index(var))
                ability_pts -= var.cost

            if mtype == "Dragon":
                if ability_pts >= 1:
                    var = first(x for x in temp_ability_list if x.name == "Flying")
                    m_abilities.append(var)
                    temp_ability_list.pop(temp_ability_list.index(var))
                    ability_pts -= var.cost
                if ability_pts >= 3:
                    var = first(x for x in temp_ability_list if x.name == "Elemental Breath")
                    m_abilities.append(var)
                    temp_ability_list.pop(temp_ability_list.index(var))
                    ability_pts -= var.cost
                if ability_pts >= 3:
                    var = first(x for x in temp_ability_list if x.name == "Greater Natural Weapons")
                    m_abilities.append(var)
                    temp_ability_list.pop(temp_ability_list.index(var))
                    ability_pts -= var.cost
                    var = first(x for x in temp_ability_list if x.name == "Enhanced Natural Weapons")
                    temp_ability_list.pop(temp_ability_list.index(var))
                    var = first(x for x in temp_ability_list if x.name == "Natural Weapons")
                    temp_ability_list.pop(temp_ability_list.index(var))
                if ability_pts >= 2 and [x for x in temp_ability_list if x.name == "Enhanced Natural Weapons"]:
                    var = first(x for x in temp_ability_list if x.name == "Enhanced Natural Weapons")
                    m_abilities.append(var)
                    temp_ability_list.pop(temp_ability_list.index(var))
                    ability_pts -= var.cost
                    var = first(x for x in temp_ability_list if x.name == "Natural Weapons")
                    temp_ability_list.pop(temp_ability_list.index(var))
                if ability_pts >= 1 and [x for x in temp_ability_list if x.name == "Natural Weapons"]:
                    var = first(x for x in temp_ability_list if x.name == "Natural Weapons")
                    m_abilities.append(var)
                    temp_ability_list.pop(temp_ability_list.index(var))
                    ability_pts -= var.cost

            if mtype == "Fey" and ability_pts >= 0:
                var = first(x for x in temp_ability_list if x.name == "Iron Sensitivity")
                m_abilities.append(var)
                temp_ability_list.pop(temp_ability_list.index(var))
                ability_pts -= var.cost

            if mtype == "Fiend" and ability_pts >= 2:
                var = first(x for x in temp_ability_list if x.name == "Fiendish Blood")
                m_abilities.append(var)
                temp_ability_list.pop(temp_ability_list.index(var))
                ability_pts -= 2

            if mtype == "Magical Beast" and ability_pts >= 1:
                var = first(x for x in temp_ability_list if x.name == "Magical Body")
                m_abilities.append(var)
                temp_ability_list.pop(temp_ability_list.index(var))
                ability_pts -= var.cost

            if mtype == "Spirit":
                var = first(x for x in temp_ability_list if x.name == "Spirit Body")
                m_abilities.append(var)
                temp_ability_list.pop(temp_ability_list.index(var))

            if tier != "Mob":
                no_familiar = [x for x in temp_ability_list if x.name != "Ideal Familiar"]
                temp_ability_list = no_familiar.copy()

            while ability_pts > 0:
                if ability_pts >= 3:
                    ran_cost = rng(3)
                    temp_list = []
                    for obj in temp_ability_list:
                        if obj.cost == ran_cost:
                            temp_list.append(obj)
                    ran_ability = temp_list[rng(len(temp_list) - 1)]
                    m_abilities.append(ran_ability)
                    ability_pts -= ran_ability.cost
                    temp_ability_list.pop(temp_ability_list.index(ran_ability))
                if ability_pts >= 2:
                    ran_cost = rng(2)
                    temp_list = []
                    for obj in temp_ability_list:
                        if obj.cost == ran_cost:
                            temp_list.append(obj)
                    ran_ability = temp_list[rng(len(temp_list) - 1)]
                    m_abilities.append(ran_ability)
                    ability_pts -= ran_ability.cost
                    temp_ability_list.pop(temp_ability_list.index(ran_ability))
                if ability_pts >= 1:
                    ran_cost = 1
                    temp_list = []
                    for obj in temp_ability_list:
                        if obj.cost == ran_cost:
                            temp_list.append(obj)
                    ran_ability = temp_list[rng(len(temp_list) - 1)]
                    m_abilities.append(ran_ability)
                    ability_pts -= ran_ability.cost
                    temp_ability_list.pop(temp_ability_list.index(ran_ability))

            for obj in m_abilities:
                hp_mod += obj.hp_mod
                mana += obj.mana_mod
                attack_bonus += obj.attack_bonus
                pd += obj.pd_mod
                md += obj.md_mod

            md += 7 + will + cha
            mana += 7 + (2 * cha) + mlvl
            if mtype == "Spirit":
                aura += max(intellect, will, cha) + max(intellect, will, cha) + max(focus, talent, skill) + mlvl
                if mlvl >= 1:
                    hp += (hp_mod + will) * mlvl
                else:
                    hp += (hp_mod + cha) / 2
                pd += 7 + will + cha
                attack_bonus += intellect + mlvl
                strength = 0
                dex = 0
                sta = 0
            else:
                aura += max(strength, dex, sta) + max(intellect, will, cha) + max(focus, talent, skill) + mlvl
                if mlvl >= 1:
                    hp += (hp_mod + sta) * mlvl
                else:
                    hp += (hp_mod + sta) / 2
                pd += 7 + dex + sta
                attack_bonus += strength + mlvl
            for obj in m_abilities:
                if obj.name == "Gestalt Entity":
                    pd += will

            hp = int(math.ceil(hp))
            print("Name: " +
                  "\nLevel: " + str(mlvl) +
                  "\nType: " + mtype +
                  "\nTier: " + tier +
                  "\n" + ("-" * 25) +
                  "\nHealth: " + str(hp) +
                  "\nAura Rating: " + str(aura) +
                  "\nBase Speed: " + str(speed) + "'")
            if fly_speed > 0:
                print(f"\nFly Speed: {fly_speed}'")
            print("PD: " + str(pd) +
                  "\nMD: " + str(md) +
                  "\nMana: " + str(mana) +
                  "\nMelee Attack Bonus: " + str(attack_bonus) +
                  "\n" + ("-" * 25) +
                  "\nStrength: " + str(strength) +
                  "\nDexterity: " + str(dex) +
                  "\nStamina: " + str(sta) +
                  "\n" + ("-" * 25) +
                  "\nIntellect: " + str(intellect) +
                  "\nWillpower: " + str(will) +
                  "\nCharisma: " + str(cha) +
                  "\n" + ("-" * 25) +
                  "\nFocus: " + str(focus) +
                  "\nTalent: " + str(talent) +
                  "\nSkill: " + str(skill))
            print("Abilities")
            for x in m_abilities:
                print(x.name, ":", x.effect)

            static_count = repeater
            if static_choice == "Random":
                m_name = f"rng_{static_count}"
            else:
                m_name = str(input("Time to name your monster: "))
            monster = Monster(m_name, mlvl, m_abilities, mtype, strength, dex, sta, intellect, will, cha, focus,
                              talent, skill, hp, aura, pd, md, mana, attack_bonus, tier, speed)
            print_monster_sheet()
    else:
        update_csv()
        print("Exiting Program. Have a nice day!\n")
        print_abilities()
        running = False
