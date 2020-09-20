from collections import OrderedDict

myOrderedDict = OrderedDict()
myOrderedDict['A'] = 'Python'
myOrderedDict['B'] = 'C++'
myOrderedDict['C'] = 'Somers'
myOrderedDict['D'] = 'c'

for name, language in myOrderedDict.items():
    print(name.title() + "'s favourite language is " + language.title() + '.')