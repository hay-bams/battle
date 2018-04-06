from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item

# creata balck magic
fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('Quake', 14, 140, 'black')

#create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create some item
potion = Item('Potion', 'potion', 'Heals 50 hit point', 50)
highpotion = Item('Hi-potion', 'potion', 'Heals 100 hit point', 100)
superpotion = Item('Super potion', 'potion', 'Heals 500 hit point', 500)
elixer = Item('Elixer', 'elixer', 'Fully restores HP/MP of one party member', 9999)
highelixer = Item('MegaElixer', 'elixer', 'Fully restores party\'s HP/MP', 9999)

grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)

player_spell = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [potion, highpotion, superpotion, elixer, highelixer, grenade]


player = Person(460, 65, 60, 34, player_spell, player_items)
enemy = Person(1200, 65, 45, 25, [], [ ])

running = True
i = 0

print(Bcolors.FAIL +  Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
    print('==============')
    player.choose_action()
    choice = input('Choose action: ')
    index = int(choice) - 1

    if index == 0:
        damage = player.generate_damage()
        enemy.take_damage(damage)
        print('You attacked for', damage, 'points of damage. Enemy Hit Point:')
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input('Choose magic: ')) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_damage = spell.generate_damage()


        current_mpoint = player.get_mpoint()

        if spell.cost > current_mpoint:
            print(Bcolors.FAIL + "\nNot enough mpoint")
            continue
        player.reduce_mpoint(spell.cost)

        if spell.type == 'white':
            player.heal(magic_damage )
            print(Bcolors.OKBLUE + '\n' + spell.name + ' heals for', str(magic_damage), 'points of damage' + Bcolors.ENDC)
        elif spell.type == 'black':
            enemy.take_damage(magic_damage)
            print(Bcolors.OKBLUE + '\n' + spell.name + ' deals', str(magic_damage), 'points of damage' + Bcolors.ENDC)
    elif index == 2:
        player.choose_item()
        item_choice = int(input('Choose item: ')) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]
        if item.type == 'potion':
            player.heal(item.prop)
            print(Bcolors.OKGREEN + '\n' + item.name + ' heals for', str(item.prop) + Bcolors.ENDC)
        elif item.type == 'elixer':
            player.hit_point = player.max_hit_point
            player.mpoint = player.max_mpoint
            print(Bcolors.OKGREEN + '\n' + item.name + ' fully restores HP/MP' + Bcolors.ENDC)
        elif item.type == 'attack':
            enemy.take_damage(item.prop)

            print(Bcolors.FAIL + '\n' + item.name + ' deals' + str(item.prop), 'points of damage' + Bcolors.ENDC)

    enemy_choice = 1
    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print('Enemy attacks for', enemy_damage)

    print('--------------------------------')
    print('Enemy hit point:', Bcolors.FAIL + str(enemy.get_hit_point()) + '/' + str(enemy.get_max_hit_point()) + Bcolors.ENDC + '\n')

    print('Your Hit point:', Bcolors.OKGREEN + str(player.get_hit_point()) + '/' + str(player.max_hit_point) + Bcolors.ENDC + '\n ')
    print('Your magic point:', Bcolors.OKBLUE + str(player.get_mpoint()) + '/' +  str(player.get_max_mpoint()) + Bcolors.ENDC + '\n')


    if enemy.get_hit_point() == 0:
        print(Bcolors.OKGREEN + 'You win' + Bcolors.ENDC)
        running = False
    elif player.get_hit_point() == 0:
        print(Bcolors.FAIL + 'Your Enemey has defeated you' + Bcolors.ENDC)
        running = False