import pandas as pd

sheet_name = "Magus_Monster_Abilities"
sheet_id = "1lsZiqF8mArcqDkMm8LongnaP9jS1vZKd0zmiDkDB-KA"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
ability_list = []


class Ability:
    def __init__(self, name, magical, effect, cost, hp_mod, mana_mod, attack_bonus, pd_mod, md_mod, speed_mod, requirements):
        self.name = name
        self.magical = magical
        self.effect = effect
        self.cost = cost
        self.hp_mod = hp_mod
        self.mana_mod = mana_mod
        self.attack_bonus = attack_bonus
        self.pd_mod = pd_mod
        self.md_mod = md_mod
        self.speed_mod = speed_mod
        self.requirements = requirements


def update_csv():
    df = pd.read_csv(url, usecols=["Ability Name", "Cost", "Description", "Magical", "hp_mod", "mana_mod", "attack_mod", "pd_mod", "md_mod", "speed_mod", "Requirements"])
    print(df.to_string())
    for ind in df.index:
        ability_list.append(Ability(df["Ability Name"][ind], df["Magical"][ind], df["Description"][ind],
                                    df["Cost"][ind], df["hp_mod"][ind], df["mana_mod"][ind],
                                    df["attack_mod"][ind], df["pd_mod"][ind], df["md_mod"][ind], df["speed_mod"][ind],
                                    df["Requirements"][ind]))


def print_abilities():
    for abil in ability_list:
        print(f"{'' + abil.name:<25} |  Cost: {abil.cost:<3} |  Effect: {abil.effect}")
