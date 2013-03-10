#!/usr/bin/env python
#coding: utf-8

import urwid

from plants import Plant
from names import random_name
from player import Player
from store import Store


class InputBox(urwid.Pile):
    def __init__(self, garden):
        self.edit = urwid.Edit(caption="> ")
        super(InputBox, self).__init__([self.edit])
        self.garden = garden

    def keypress(self, size, key):
        if key != 'enter':
            return super(InputBox, self).keypress(size, key)
        value = self.edit.edit_text
        if value:
            funcname = value.split()[0]
            self.edit.edit_text = ""

            if hasattr(self.garden, funcname) and funcname in COMMANDS:
                # Call the relevant function and blank our editbox.
                getattr(self.garden, funcname)(*value.split()[1:])
            else:
                self.garden.add_log("Syntax Error: "+funcname)
        self.garden.tick() # Tick after every command

COMMANDS = []
def command(func):
    global COMMANDS
    COMMANDS.append(func.__name__)
    return func


class Garden(object):
    '''
    >>> p = Plant(seed=34)
    >>> g = Garden()
    >>> g.objects.append(p)
    >>> g.format_objects()
    [u'\u2698 Qux']
    '''

    def __init__(self):
        self.player = Player()
        self.store = Store()
        self.objects = []

        # A simple log of things that have happened.
        self.log = urwid.Pile([])
        self.top = urwid.Frame(body=urwid.Pile([self.log]), footer=InputBox(garden=self), focus_part='footer')

        self.intro()

    def tick(self):
        self.add_log("* A day passes.")

        self.player.tick()
        for obj in self.objects:
            log = obj.tick()
            if log:
                self.add_log(log)

    @command
    def hi(self, *args):
        self.add_log("* You say hi {args}!".format(args=args))

    @command
    def help(self):
        self.add_log("Available commands:")
        self.add_log(", ".join(COMMANDS))

    @command
    def quit(self):
        raise urwid.ExitMainLoop()

    @command
    def shop(self, itemname=None):
        inventory = self.store.get_inventory()
        if not itemname:
            self.add_log("* You flip through your handy-dandy store catalog.")
            for item in inventory:
                if item.value <= (self.player.money*3):
                    self.add_log(u" {0}: {1} {2}".format(self.format_object(item), item.value, self.player.currency))
        else:
            for item in inventory:
                if item.name.lower() == itemname.lower():
                    self.add_log(item.description())

    @command
    def buy(self, itemname, number=1):
        inventory = self.store.get_inventory()
        for item in inventory:
            if item.name.lower() == itemname.lower():
                cost = (item.value * number)
                if (cost) > self.player.money:
                    self.add_log("Not enough {0} to buy that.".format(self.player.currency))
                else:
                    self.add_log("* You buy {0} {1} for {2} {3}".format(number, itemname, cost, self.player.currency))
                    self.player.money -= cost
                    self.objects.extend([item]*number)
                return
        else:
            self.add_log("No such item in the store.")

    def add_log(self, value):
        if isinstance(value, basestring):
            value = [value]

        for item in value:
            self.log.contents.append((urwid.Text(item.strip()), ('pack', None)))

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

    def intro(self):
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
        self.add_money(10)


def main():
    garden = Garden()
    urwid.MainLoop(garden.top).run()

if __name__ == "__main__":
    main()
