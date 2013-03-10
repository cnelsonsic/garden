import inflect
p = inflect.engine()

# This is almost entirely from http://en.wikipedia.org/wiki/List_of_fictional_currencies
_CURRENCIES = '''
Altairian Dollar
Ankh-Morpork dollar
Bell
Belli
Beri
Bison Dollar
Bit
Bolt
Bottle Cap
Brandar Tile
Buckazoid
Cash
Clam
Copper Star
Cred
Credit
Crescent
Crindar
Crown
Cubit
Darsek
Dirak
Dollarpound
Dorak
Double dollar
Ducat
Ecu
Energy
Extol
Farthing
Federation credit
Fennik
Flanian Pobble Bead
Frang
Galleon
Gil
Gold
Golden Dragon
Influence
Interstellar Kredit
Isik
Jangle
Jenny
Jewel
Jovian credit
Kalganid
Kan
Knut
Kretmas
Latinum Brick
Legion Aureus
Legion Denari
Lek
Lita
Mark
Meld
Meseta
Meso
Monetary Unit
Monie
Munny
NCR Dollar
New Yen
Nick
Ningi
Ob
Ozol
Parsohn
Poke-Dollar
Quatloo
Red Orb
Renn
Rupee
Sen
Septim
Shell
Shyneum Pennie
Sickle
Silver Stag
Simoleon
Space buck
Sporebuck
Territ
Thaler
Token
Triganic Pu
UEO Credit
Wong
Woolong
Yuan
Zeni
Zenith
Zenny
Zulie
'''

CURRENCIES = [p.plural(money) for money in _CURRENCIES.split("\n") if money]
