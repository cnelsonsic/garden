GARDEN - (Graphical Artificial Random Dungeon Except Not)
======

[![Build Status](https://travis-ci.org/cnelsonsic/garden.png?branch=master)](https://travis-ci.org/cnelsonsic/garden)

Garden is a text-only game where you manage a garden/menagerie.
You buy seeds, which grow into plants, which attract animals, which attract bigger animals.

Only, right now the only part of the above that is true is the "text-only game" part, the rest is a bald-faced lie.

The interesting part is that all the content is randomly generated, a la [Corruption of Champions](http://cocwiki.org) (:warning: NSFW :warning:)
The main difference though, is that instead of randomly generating descriptions of body parts, GARDEN generates descriptions of plants and animals.

Well, just plants right now, animals will undoubtedly come later.

For example, here's a sample plant from a doctest over in garden/plants.py:
This tree is roughly 136 cm tall by 12 cm wide. It has oval-shaped leaves, 1 cm wide by 4 cm long. The plant takes 50 days to reach maturity and begin flowering. It produces gray colored blooms, with a pungeant aroma. After flowering, it produces tangy fruit that is 2 cm wide by 2 cm long. In a growing season, it can produce anywhere from 1 to 5 fruit. The fruit takes 4 days to ripen fully from the day the bud first forms. Its seeds are roughly 0.7 cm wide by 5.5 cm long. They take 14 days to germinate.

