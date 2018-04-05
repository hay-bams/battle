import random

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE =  '\033[94m'
    OKGREEN =  '\033[93m'
    WARNING =  '\033[92m'
    FAIL =  '\033[91m'
    ENDC =  '\033[0m'
    BOLD =  '\033[1m'
    UNDERLINE =  '\033[4m'


class Person:
    def __init__(self, hit_point, mpoint, attack, defense, magic):
        self.max_hit_point = hit_point
        self.hit_point = hit_point
        self.max_mpoint = mpoint
        self.mpoint = mpoint
        self.attack_low = attack - 10
        self.attack_high =  attack + 10
        self.defense = defense
        self.magic = magic
        self.actions = ['Attack', 'Magic']

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def take_damage(self, damage):
        self.hit_point -= damage

        if self.hit_point < 0:
            self.hit_point = 0

        return self.hit_point

    def get_hit_point(self):
        return self.hit_point

    def get_max_hit_point(self):
        return self.max_hit_point

    def get_mpoint(self):
        return self.mpoint

    def get_max_mpoint(self):
        return self.max_mpoint

    def reduce_mpoint(self, cost):
        self.mpoint -= cost

    def heal(self, damage):
        self.hit_point += damage
        if self.hit_point > self.max_hit_point:
            self.hit_point = self.max_hit_point

    def choose_action(self):
        i = 1
        print(Bcolors.OKBLUE + Bcolors.BOLD + 'Actions' + Bcolors.ENDC)
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(Bcolors.OKBLUE + Bcolors.BOLD + 'Magic' + Bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ":", spell.name, "(cost", str(spell.cost) + ")")
            i += 1


