#!/usr/bin/env python
#coding: utf-8

from cmd import Cmd

from copy import deepcopy

from plants import Plant
from names import random_name
from player import Player
from store import Store
from items import Item
from savegame import Saveable


class App(Cmd, Saveable):
    prompt = "> "

    def __init__(self):
        Cmd.__init__(self)

        self.player = Player()
        self.store = Store()
        self.objects = [] # All objects in the garden.

        self._do_intro()

    def emptyline(self):
        pass

    def default(self, line):
        self.add_log("Arglebargle, glop-glyf?")

    def postcmd(self, stop, line):
        self.tick()
        Cmd.postcmd(self, stop, line)
        return False

    def tick(self):
        self.add_log("* A day passes.")

        self.player.tick()
        for obj in self.objects:
            log = obj.tick()
            if log:
                self.add_log(log)

    def do_save(self, arg):
        '''Save your game.'''
        # temporarily remove stdout/stdin for pickling
        stdout = self.stdout
        stdin = self.stdin
        self.stdout = None
        self.stdin = None

        self.save()

        # reattach stdout/stdin
        self.stdout = stdout
        self.stdin = stdin

    def do_load(self, arg):
        '''Load your game.'''
        # temporarily remove stdout/stdin for pickling
        stdout = self.stdout
        stdin = self.stdin
        self.stdout = None
        self.stdin = None

        self.load()

        # reattach stdout/stdin
        self.stdout = stdout
        self.stdin = stdin

    def do_shop(self, itemname=None):
        '''Show a list of items available for purchase.'''
        inventory = self.store.get_inventory()
        if not itemname:
            self.add_log("* You flip through your handy-dandy store catalog.")
            self.add_log("* (You have {0} {1})".format(self.player.money, self.player.currency))
            for item in inventory:
                if item.value <= (self.player.money*3): # TODO: Make this the total worth of the garden instead.
                    self.add_log(u" {0}: {1} {2}".format(item.fancy_name(), item.value, self.player.currency))
        else:
            for item in inventory:
                if item.name.lower() == itemname.lower():
                    self.add_log(item.description())

    def do_buy(self, itemname, number=1):
        '''Buy a specific item, or a number of items.'''
        if not itemname:
            self.add_log("Please specify the name of an item to buy.")
            return

        inventory = self.store.get_inventory()
        for item in inventory:
            if item.name.lower() == itemname.lower():
                cost = (item.value * number)
                if (cost) > self.player.money:
                    self.add_log("Not enough {0} to buy that.".format(self.player.currency))
                else:
                    self.add_log("* You buy {0} {1} for {2} {3}".format(number, itemname, cost, self.player.currency))
                    self.player.money -= cost
                    self.objects.extend([deepcopy(item)]*number)
                return
        else:
            self.add_log("No such item in the store.")

    def do_inspect(self, arg):
        '''Inspect a specific item to see all its details.'''
        pass

    def do_look(self, arg):
        '''Look around your garden to see the general inventory.'''
        self.add_log("* You look around your garden, you see:")
        self.add_log("="*30)
        self.add_log(self.format_objects() or "Nothing but barren dirt.")
        self.add_log("="*30)

    def do_gather(self, arg):
        '''Gather all the fruit from your plants. for sale or planting.'''
        wasfruit = False
        for obj in self.objects:
            if obj.num_fruit:
                wasfruit = True
                self.player.inventory.extend([Item("{0} Fruit".format(obj.name), value=obj.value/10)]*obj.num_fruit)
                self.add_log("* You gather {num_fruit} fruit from one of your {name} {plant_shape}s".format(**obj.__dict__))
                obj.num_fruit = 0

        if not wasfruit:
            self.add_log("There's no fruit to gather...")
            return

        self.add_log("* Your inventory is now:")
        self.add_log(self.player.inventory)

    def do_sell(self, arg):
        '''List salable items or sell a specific item.'''
        if not arg:
            self.add_log("* You open your pack")
            for item in self.player.inventory:
                self.add_log(("{item.name}: "
                              "{item.value} "
                              "{money}").format(item=item,
                                                money=self.player.currency))
        else:
            for item in self.player.inventory[:]:
                if arg.lower() in item.name.lower():
                    self.player.money += item.value
                    self.player.inventory.remove(item)
                    self.add_log("* You sell {item.name} for {item.value}.".format(item=item))
                    break

    def add_log(self, value):
        if isinstance(value, basestring):
            value = [value]

        for item in value:
            self.stdout.write(unicode(item).strip()+"\n")

    def format_objects(self):
        '''Format the objects list for printing to the screen.'''
        return [obj.short_description() for obj in self.objects]

    def add_money(self, amount):
        self.player.money += amount
        self.add_log("* You got {0} {1}.".format(amount, self.player.currency))

    def _do_intro(self):
        intro = '''Long ago in a realm known as {world_name},
        you were granted a plot of land.
        You were told to go forth and populate it with plants and animals.
        Then there was something about an amulet.
        But you can't quite recall what.
        To be honest, you got kind of bored right about then.
        ...
        Buy plants, attract animals.
        That's pretty much it.
        Here's some money.'''.format(world_name=random_name())
        self.add_log(intro.split("\n"))
        self.add_money(100)


def main():
    app = App()
    app.cmdloop()

if __name__ == "__main__":
    main()
