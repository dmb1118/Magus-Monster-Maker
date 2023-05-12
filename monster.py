class Monster:
    def __init__(self, m_name, lvl, m_abilities, mtype, strength, dex, sta, intellect, will, cha, focus, talent,
                 skill, hp, aura, pd, md, mana, melee_attack, ranged_attack, attack_bonus, tier, speed, fly_speed,
                 climb_speed, swim_speed):
        self.m_name = m_name
        self.lvl = lvl
        self.mtype = mtype
        self.tier = tier
        self.hp = hp
        self.aura = aura
        self.speed = speed
        self.pd = pd
        self.md = md
        self.mana = mana
        self.strength = strength
        self.dex = dex
        self.sta = sta
        self.intellect = intellect
        self.will = will
        self.cha = cha
        self.focus = focus
        self.talent = talent
        self.skill = skill
        self.m_abilities = m_abilities
        self.attack_bonus = attack_bonus
        self.melee_attack = melee_attack
        self.ranged_attack = ranged_attack
        self.fly_speed = fly_speed
        self.climb_speed = climb_speed
        self.swim_speed = swim_speed

    def print_abilities(self):
        print("Abilities\n")
        for x in self.m_abilities:
            print(x)

