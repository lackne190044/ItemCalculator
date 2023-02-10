"""Tests wether the project is even importable."""

from test_handler import TestHandler
import os

try:
    import src
except:
    src = None
try:
    from main import get_resources
except:
    get_resources = None
from src import ItemHandler

def test_output():
    assert src
    assert get_resources

    test_handler = TestHandler()

    test_handler.remove_files(["tmp/items.db"])
    test_handler.remove_folders(["tmp"])

    os.mkdir("tmp")
    test_handler.populate()

    item_handler = ItemHandler("sqlite:///tmp/items.db")
    item = item_handler.search_item("Zenith")

    assert get_resources(item) == """4956: Zenith
  757: Terra Blade
    675: True Night's Edge
      273: Night's Edge
        795: Blood Butcherer
          1257: Crimtane Bar
        155: Muramasa
        190: Blade of Grass
          209: Stinger
          331: Jungle Spores
          210: Vine
        121: Volcano
          175: Hellstone Bar
      547: Soul of Fright
      548: Soul of Might
      549: Soul of Sight
    674: True Excalibur
    1570: Broken Hero Sword
  3063: Meowmere
  3065: Star Wrath
  2880: Influx Waver
  1826: The Horseman's Blade
  3018: Seedler
  65: Starfury
  1123: Bee Keeper
  989: Enchanted Sword
  3507: Copper Shortsword
    20: Copper Bar"""

