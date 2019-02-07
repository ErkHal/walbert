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
        
        if rule.style.selectorText == 'QListView':
            print(rule.style.cssText)
            #property.value = colorArray['colors']['color6']
    
    except AttributeError as e:
        pass #Ignore error if attribute doesn't exist

with open('/usr/share/albert/org.albert.frontend.widgetboxmodel/themes/Walbert.qss', 'wb') as f:
    f.write(styleSheet.cssText)
    f.close()