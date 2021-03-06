from vanilla.dialogs import *
import os
from mojo.UI import AskString

newLayer = AskString('Layer to copy all existing glyphs to, e.g. "overlap"')

font = CurrentFont()

glyphsToCopyToNewLayer = font.selectedGlyphNames

for name in glyphsToCopyToNewLayer:
    font[name].layers[0].copyLayerToLayer("foreground", newLayer)
    font[name].layers[-1].width = font[name].layers[0].width
    print(
        f"Glyphs copied to {newLayer}! Please save font to keep changes.")
