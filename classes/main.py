from classes.game import Person, Bcolors
from classes.magic import Spell

# creata balck magic
fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('Quake', 14, 140, 'black')

#create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")


player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

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