#!/usr/bin/env python
#coding: utf-8

import urwid

from plants import Plant
from names import random_name
from player import Player


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

            if hasattr(self.garden, funcname):
                # Call the relevant function and blank our editbox.
                self.edit.edit_text = ""
                getattr(self.garden, funcname)(*value.split()[1:])
        self.garden.tick() # Tick after every command


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
        self.objects = []

        # A simple log of things that have happened.
        self.log = urwid.Pile([])
        self.top = urwid.Frame(body=urwid.Pile([self.log]), footer=InputBox(garden=self), focus_part='footer')

        self.intro()

    def tick(self):
        self.add_log("* A day passes.")
        pass

    def hi(self, *args):
        self.add_log("* You say hi {args}!".format(args=args))

    def add_log(self, value):
        if isinstance(value, basestring):
            value = [value]

        for item in value:
            self.log.contents.append((urwid.Text(item.strip()), ('pack', None)))

    def format_objects(self):
        '''Format the objects list for printing to the screen.'''
        retval = []
        for obj in self.objects:
            if type(obj) == Plant:
                symbol = u"⚘"
            # elif type(obj) == Animal:
                # symbol = u"♘"
            retval.append(symbol+" "+obj.name)
        return retval

    def add_money(self, amount):
        self.player.money += amount
        self.add_log("* You got {0} money.".format(amount))

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
