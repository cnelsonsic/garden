'''This is a subset of colors from X11's rgb.txt.
The CamelCase and numbered colors have been removed,
as well as all "grey" colors in favor of "gray".'''

_COLORS = '''
alice blue
antique white
aquamarine
azure
beige
bisque
black
blanched almond
blue
blue violet
brown
burlywood
cadet blue
chartreuse
chocolate
coral
cornflower blue
cornsilk
cyan
dark blue
dark cyan
dark goldenrod
dark gray
dark green
dark khaki
dark magenta
dark olive green
dark orange
dark orchid
dark red
dark salmon
dark sea green
dark slate blue
dark slate gray
dark turquoise
dark violet
deep pink
deep sky blue
dim gray
dodger blue
firebrick
floral white
forest green
gainsboro
ghost white
gold
goldenrod
gray
green
green yellow
honeydew
hot pink
indian red
ivory
khaki
lavender
lavender blush
lawn green
lemon chiffon
light blue
light coral
light cyan
light goldenrod
light goldenrod yellow
light gray
light green
light pink
light salmon
light sea green
light sky blue
light slate blue
light slate gray
light steel blue
light yellow
lime green
linen
magenta
maroon
medium aquamarine
medium blue
medium orchid
medium purple
medium sea green
medium slate blue
medium spring green
medium turquoise
medium violet red
midnight blue
mint cream
misty rose
moccasin
navajo white
navy
navy blue
old lace
olive drab
orange
orange red
orchid
pale goldenrod
pale green
pale turquoise
pale violet red
papaya whip
peach puff
peru
pink
plum
powder blue
purple
red
rosy brown
royal blue
saddle brown
salmon
sandy brown
sea green
seashell
sienna
sky blue
slate blue
slate gray
snow
spring green
steel blue
tan
thistle
tomato
turquoise
violet
violet red
wheat
white
white smoke
yellow
yellow green
'''

COLORS = [color for color in _COLORS.split("\n") if color]
