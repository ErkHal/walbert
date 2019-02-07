#!/usr/bin/env python
# Uses PyWal colors and adds them to a predefined Albert launcher theme

__author__ = "ErkHal"

import os
import json
import cssutils

pywalFilepath = os.path.join(os.environ['HOME'], '.cache/wal/colors.json')
styleSheet = cssutils.parseFile('/usr/share/albert/org.albert.frontend.widgetboxmodel/themes/Walbert.qss')

with open(pywalFilepath) as f:
    colorArray = json.load(f)

for rule in styleSheet.cssRules:
    try:
        if rule.selectorText == '*':
            rule.style.color = colorArray['colors']['color3']
            rule.style.backgroundColor = colorArray['colors']['color0']
        
        if rule.selectorText == '#settingsButton':
            rule.style.color = colorArray['colors']['color3']

        if rule.selectorText == '#frame' or rule.selectorText == '#inputLine':
            rule.style.backgroundColor = colorArray['colors']['color0']
        
        if rule.selectorText == 'QListView':
            rule.style['selection-color'] = colorArray['colors']['color7']
    
    except AttributeError as e:
        pass #Ignore error if attribute doesn't exist

with open('/usr/share/albert/org.albert.frontend.widgetboxmodel/themes/Walbert.qss', 'wb') as f:
    f.write(styleSheet.cssText)
    f.close()
