class Ability:
    def __init__(self, name, magical, effect, cost, hp_mod, mana_mod, attack_bonus, pd_mod, md_mod):
        self.name = name
        self.magical = magical
        self.effect = effect
        self.cost = cost
        self.hp_mod = hp_mod
        self.mana_mod = mana_mod
        self.attack_bonus = attack_bonus
        self.pd_mod = pd_mod
        self.md_mod = md_mod


ability_objects = [
    Ability("Water Dependant", 0, "-2 on all checks made while outside of water. You can only survive outside of " +
            "water for a number of minutes equal to Stamina score", -2, 0, 0, 0, 0, 0),
    Ability("Cold-Blooded", 0, "-2 on all checks made while in a cold environment", -2, 0, 0, 0, 0, 0),
    Ability("Iron Sensitivity", 1, "All of your magical abilities are disabled while you are in direct contact "
                                   "with iron", -2, 0, 0, 0, 0, 0),
    Ability("Invisibility", 1, "Turn Invisible as a Move action for 1 mana, Duration 1 Minute", 2, 0, 0, 0, 0, 0),
    Ability("Magical Body", 1, "Your natural attacks count as magical for all purposes", 1, 0, 0, 0, 0, 0),
    Ability("Alter Form", 1, "1+ Mana, As a move action you may change minor details about your body such as " +
            "hair color, eye color, etc, Duration 1 Minute per Mana Spent", 1, 0, 0, 0, 0, 0),
    Ability("Treasure Sense", 1, "You can magically sense gems, magical items, and precious metals up to 100 " +
            "feet away", 1, 0, 0, 0, 0, 0),
    Ability("Nature's Call", 0, "+3 bonus to all nature related rolls", 1, 0, 0, 0, 0, 0),
    Ability("Flying", 0, "+3 to Dexterity Checks while Flying, can fly instead of regular ground movement", 1,
            0, 0, 0, 0, 0),
    Ability("Swimming", 0, "Allows the creature to swim without penalty or checks required", 1, 0, 0, 0, 0, 0),
    Ability("Camouflage", 0, "Add +3 to all survival checks related to stealth", 1, 0, 0, 0, 0, 0),
    Ability("Climbing", 0, "Allows the creature to climb without penalty or checks required", 1, 0, 0, 0, 0, 0),
    Ability("Scavenger", 0, "Add +3 to all rolls to search for items or information", 1, 0, 0, 0, 0, 0),
    Ability("Slippery", 0, "Add +1 to PD and +2 to escape Grapple checks", 1, 0, 0, 0, 1, 0),
    Ability("Venomous", 0, "When you deal damage to a target’s health, you do an additional 2 poison damage",
            1, 0, 0, 0, 0, 0),
    Ability("Friendly", 0, "+3 to charisma checks to befriend or persuade humanoids for aid", 1, 0, 0, 0, 0, 0),
    Ability("Scent", 0, "+3 to tracking checks related to scent", 1, 0, 0, 0, 0, 0),
    Ability("Natural Weapons", 0, "+2 to melee attack bonus", 1, 0, 0, 2, 0, 0),
    Ability("Charge", 0, "+3 to attack if the creature has moved this turn", 1, 0, 0, 0, 0, 0),
    Ability("Pack Hunter", 0, "+1 to attack for each ally within nearby range", 1, 0, 0, 0, 0, 0),
    Ability("Grappler", 0, "+3 to all grapple checks", 1, 0, 0, 0, 0, 0),
    Ability("Acrobatic", 0, "+3 to all Athletics checks", 1, 0, 0, 0, 0, 0),
    Ability("Tough", 0, "+2 Health per level", 1, 2, 0, 0, 0, 0),
    Ability("Healing Touch", 1, "1+ Mana Cost, 1 Health restored per mana spent on Close target", 2, 0, 0, 0, 0, 0),
    Ability("Smite", 1, "1+ Mana Cost, When making a weapon attack add +1 per mana spent", 2, 0, 0, 0, 0, 0),
    Ability("Earth Glide", 1, "You can move unhindered through rocks and other minerals as easily as humans through "
                              "water", 2, 0, 0, 0, 0, 0),
    Ability("Compel Enemy", 1, "As a move action you may attempt to force an enemy to attack themself instead of " +
            "others for 1 Round. Roll Charisma + Focus vs MD.", 2, 0, 0, 0, 0, 0),
    Ability("Aetheric Resonance", 1, "+1 to PD and MD against magical attacks, also whenever you are affected by " +
            "a hostile spell, you gain 1 mana", 2, 0, 0, 0, 0, 0),
    Ability("Construct Body", 0, "Immune to poison, disease, mind control and you do not need to breathe, eat, " +
            "drink, or sleep", 0, 0, 0, 0, 0, 0),
    Ability("Gestalt Entity", 1, "Your soul and body are one, you may add your Willpower to PD", 3, 0, 0, 0, 0, 0),
    Ability("Potent Venom", 0, "When you deal damage to a target’s health, you do an additional 4 " +
                               "poison damage", 2, 0, 0, 0, 0, 0),
    Ability("Durable", 0, "+2 to PD", 2, 0, 0, 0, 2, 0),
    Ability("Enhanced Natural Weapons", 0, "+4 to melee attack bonus", 2, 0, 0, 4, 0, 0),
    Ability("Stealth Specialist", 0, "+6 bonus to any stealth related checks", 2, 0, 0, 0, 0, 0),
    Ability("Mobile", 0, "Can move two movement increments per move action", 2, 0, 0, 0, 0, 0),
    Ability("Pack Mentality", 0, "+1 to MD for each ally within nearby range", 2, 0, 0, 0, 0, 0),
    Ability("Constrict", 0, "While you have another creature grappled, you may use your move action to make a " +
                            "constrict attack", 2, 0, 0, 0, 0, 0),
    Ability("Extra Attack", 0, "You may make two attacks whenever you take the Attack action.", 2, 0, 0, 0, 0, 0),
    Ability("Resistance", 0, "+1 to PD and MD", 2, 0, 0, 0, 1, 1),
    Ability("Elemental Breath", 1, "1+ Mana Cost, 2d6+Stamina+Level+Mana Spent, 1 target per mana " +
                                   "spent", 3, 0, 0, 0, 0, 0),
    Ability("Teleport", 1, "5 Mana Cost, As an action you may teleport anywhere you have visited " +
                           "before", 3, 0, 0, 0, 0, 0),
    Ability("Ideal Familiar", 1, "If this creature is someone's familiar it adds a +1 bonus to all rolls, +1 to "
                                 "Health per level, and +1 to PD and MD", 3, 0, 0, 0, 0, 0),
    Ability("Conjure Armor", 1, "2+ Mana Cost, As a Move action you may conjure magical armor that adds +1 PD per " +
                                "2 mana spent, Duration 1 Round Per 2 mana spent", 3, 0, 0, 0, 0, 0),
    Ability("Conjure Weapon", 1, "1+ Mana Cost, As a Move action you may conjure a magical weapon that adds +1 to " +
                                 "attack per mana spent, Duration 1 Round Per 2 mana spent", 3, 0, 0, 0, 0, 0),
    Ability("Greater Natural Weapons", 0, "+6 to melee attack bonus", 3, 0, 0, 6, 0, 0),
    Ability("Ironhide", 0, "+4 to PD", 3, 0, 0, 0, 4, 0),
    Ability("Greater Resistance", 0, "+2 to PD and MD", 3, 0, 0, 0, 2, 2),
    Ability("Fiendish Aura", 1, "+2 to PD and MD against magical attacks", 99, 0, 0, 0, 0, 0),
    Ability("Spiritual Body", 1, "Willpower is used in place of Strength, Dexterity, and Stamina", 99, 0, 0, 0, 0, 0),
    Ability("Fire Resistance", 1, "You take half damage from sources that deal fire " +
                                  "elemental damage", 1, 0, 0, 0, 0, 0),
    Ability("Water Resistance", 1, "You take half damage from sources that deal water " +
                                   "elemental damage", 1, 0, 0, 0, 0, 0),
    Ability("Lightning Resistance", 1, "You take half damage from sources that deal " +
                                       "lightning elemental damage", 1, 0, 0, 0, 0, 0),
    Ability("Earth Resistance", 1, "You take half damage from sources that deal earth " +
                                   "elemental damage", 1, 0, 0, 0, 0, 0),
    Ability("Air Resistance", 1, "You take half damage from sources that deal air elemental damage", 1, 0, 0, 0, 0, 0),
    Ability("Psychic Resistance", 1, "You take half damage from sources that deal psychic damage", 3, 0, 0, 0, 0, 0),
    Ability("Arcane Resistance", 1, "You take half damage from sources that deal arcane damage", 3, 0, 0, 0, 0, 0),
    Ability("Radiant Resistance", 1, "You take half damage from sources that radiant damage", 3, 0, 0, 0, 0, 0),
    Ability("Force Resistance", 1, "You take half damage from sources that deal force damage", 1, 0, 0, 0, 0, 0),
    Ability("Abyssal Resistance", 1, "You take half damage from sources that deal abyss damage", 2, 0, 0, 0, 0, 0),
    Ability("Radiant Shell", 1, "1+ Mana, Standard Action, Lasts until destroyed or 1 hour, 2 Health per mana spent" +
            ", reduces damage the caster would take until the shell is destroyed and reflects an equal amount of "
            "radiant damage back at the attacker. The reflected damage hits automatically.", 3, 0, 0, 0, 0, 0),
    Ability("Abyssal Investiture", 1, "All Mana, Standard Action, Lasts 1 Minute, your maximum and current health is " +
                                      "increased by your current amount of mana for the duration. " +
                                      "Your mana pool becomes 0 by using this ability. In addition, all physical " +
                                      "attacks deal Abyss damage while this ability is active", 3, 0, 0, 0, 0, 0),
]
