#!/usr/bin/env python
# Uses PyWal colors and adds them to a predefined Albert launcher theme

__author__ = "ErkHal"

import os
import json
import cssutils

#Edit these to change the color variables assigned to the QSS rules
SELECTION_COLOR = 'color6'

pywalFilepath = os.path.join(os.environ['HOME'], '.cache/wal/colors.json')
styleSheet = cssutils.parseFile('/usr/share/albert/org.albert.frontend.widgetboxmodel/themes/Walbert.qss')

#Load pywal JSON properties
with open(pywalFilepath) as f:
    colorArray = json.load(f)

for rule in styleSheet.cssRules:
    try:
        if rule.selectorText == '*':
            rule.style.color = colorArray['special']['foreground']
            rule.style.backgroundColor = colorArray['special']['background']
        
        if rule.selectorText == '#settingsButton':
            rule.style.color = colorArray['colors'][SELECTION_COLOR]

        if rule.selectorText == '#frame' or rule.selectorText == '#inputLine':
            rule.style.backgroundColor = colorArray['special']['background']
        
        if rule.selectorText == 'QListView':
            rule.style['selection-color'] = colorArray['colors'][SELECTION_COLOR]
    
    except AttributeError as e:
        pass #Ignore error if attribute doesn't exist

# Overwrite the stylesheet file with the new rules
with open('/usr/share/albert/org.albert.frontend.widgetboxmodel/themes/Walbert.qss', 'wb') as f:
    f.write(styleSheet.cssText)
    f.close()
