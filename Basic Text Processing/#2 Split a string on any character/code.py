# To Do
"""
- Split a string on a word and include the splitting character in the 
resulting output
"""
text = """
The collapse JavaScript plugin is used to show and hide content. 
Buttons or anchors are used as triggers that are mapped to specific elements you toggle. Collapsing an element will animate the height from its current value to 0. Given how CSS handles animations, you cannot use padding on a .collapse element. Instead, use the class as an independent wrapping element.
"""

text.split()
text.split(',')
text.split('.')

# split on word

text.split('plugin')

len(text.split('plugin'))

# using re

import re

#re.split

pattern = '(plugin)'

re.split(pattern,text)
