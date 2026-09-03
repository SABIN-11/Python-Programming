import random

class Character:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

    
class Warrior(Character):

    attack = {
        0: "Shield Bash",
        "Shield Bash": 8,
        1: "Power Slash",
        "Power Slash": 10,
        2: "Earth Slam",
        "Earth Slam": 9,
        3: "Berserk Strike",
        "Berserk Strike": 11
    }
    
    defense = {
        0: "Iron Wall",
        "Iron Wall": 10,
        1: "Block Stance",
        "Block Stance": 8,
        2: "Fortify",
        "Fortify": 9,
        3: "Second Wind",
        "Second Wind": 7
    }

class Mage(Character):

    attack = {
        0: "Fireball",
        "Fireball": 15,
        1: "Frost Spike",
        "Frost Spike": 12,
        2: "Lightning Bolt",
        "Lightning Bolt": 18,
        3: "Meteor Strike",
        "Meteor Strike": 25
    }
    defense = {
        0: "Arcane Shield",
        "Arcane Shield": 4,
        1: "Mana Barrier",
        "Mana Barrier": 3,
        2: "Invisibility Cloak",
        "Invisibility Cloak": 5,
        3: "Time Warp",
        "Time Warp": 6
    }


class Archer(Character):

    attack = {
        0: "Quick Shot",
        "Quick Shot": 10,
        1: "Piercing Arrow",
        "Piercing Arrow": 12,
        2: "Poison Arrow",
        "Poison Arrow": 11,
        3: "Rain of Arrows",
        "Rain of Arrows": 13
    }
    defense = {
        0: "Dodge Roll",
        "Dodge Roll": 6,
        1: "Wind Step",
        "Wind Step": 5,
        2: "Camouflage",
        "Camouflage": 4,
        3: "Agile Guard",
        "Agile Guard": 7
    }


def battle(player1, player2, visual):
    print("BATTLE BEGINS!")
    print(f"{player1.name} {visual[player1]}   ⚔️   {player2.name} {visual[player2]}")
    print()
    print()

    option = random.randint(1, 2)   # to choose which player will attack first

    while player1.is_alive() and player2.is_alive():    # Until both players are alive

        attack_no = random.randint(0, 3)
        defense_no = random.randint(0, 3)

        if option == 1:

            # ATTACK BY PLAYER 1
            attack_name = player1.attack[attack_no]
            damage_given = player1.attack[attack_name]  # value for the respected attack
            print(f"{player1.name} has attacked with {attack_name} giving {damage_given} damage.")

            # DEFENSE BY PLAYER 2
            defense_name = player2.defense[defense_no]
            defense_applied = player2.defense[defense_name] # value for the respected defense
            print(f"{player2.name} blocked {defense_applied} damage using {defense_name}.")

            net_damage = max(damage_given - defense_applied, 0) # max function returns whichever number is greater. This is to avoid negative damage
            player2.hp -= net_damage   # Hp of player two is reduced
            print(f"{player2.name} takes {net_damage} damage! HP left: {player2.hp}")

            option = option + 1
        
        else:
            
            # ATTACK BY PLAYER 2
            attack_name = player2.attack[attack_no]
            damage_given = player2.attack[attack_name]  # value for the respected attack
            print(f"{player2.name} has attacked with {attack_name} giving {damage_given} damage.")

            # DEFENSE BY PLAYER 1
            defense_name = player1.defense[defense_no]
            defense_applied = player1.defense[defense_name] # value for the respected defense
            print(f"{player1.name} blocked {defense_applied} damage using {defense_name}.")

            net_damage = max(damage_given - defense_applied, 0) # max function returns whichever number is greater. This is to avoid negative damage
            player1.hp -= net_damage  # Hp of player two is reduced
            print(f"{player1.name} takes {net_damage} damage! HP left: {player1.hp}")


            option = option - 1
        
        print()
        print()

    if player1.is_alive():
        print(f"{player1.name} is Victorious ❤️")
    else:
        print(f"{player2.name} is Victorious ❤️")



warrior = Warrior("Sabin The Warrior", 200)
mage = Mage("Romans The Mage", 185)
archer = Archer("Gorey The Archer", 190)

visual = {
    warrior : '🗡️',
    mage : '🧙',
    archer : '🏹'
}

battle(warrior, archer, visual)


