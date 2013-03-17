#!/usr/bin/env python
#coding: utf-8

from cmd import Cmd

from copy import deepcopy

from plants import Plant
from names import random_name
from player import Player
from store import Store


class App(Cmd):
    prompt = "> "

    def __init__(self):
        Cmd.__init__(self)

        self.player = Player()
        self.store = Store()
        self.objects = []

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

    def do_shop(self, itemname=None):
        inventory = self.store.get_inventory()
        if not itemname:
            self.add_log("* You flip through your handy-dandy store catalog.")
            for item in inventory:
                if item.value <= (self.player.money*3): # TODO: Make this the total worth of the garden instead.
                    self.add_log(u" {0}: {1} {2}".format(self.format_object(item), item.value, self.player.currency))
        else:
            for item in inventory:
                if item.name.lower() == itemname.lower():
                    self.add_log(item.description())

    def do_buy(self, itemname, number=1):
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

    def add_log(self, value):
        if isinstance(value, basestring):
            value = [value]

        for item in value:
            self.stdout.write(item.strip()+"\n")

    def format_object(self, obj):
        if type(obj) == Plant:
            symbol = u"⚘"
        # elif type(obj) == Animal:
            # symbol = u"♘"
        return(symbol+" "+obj.name)

    def format_objects(self):
        '''Format the objects list for printing to the screen.'''
        retval = []
        for obj in self.objects:
            retval.append(self.format_object(obj))
        return retval

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
