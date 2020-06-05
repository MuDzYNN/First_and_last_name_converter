import json
import os
import re

names = ""

def readConfig():
    try:
        with open(os.path.join(path, 'config.json'), 'r', encoding='utf-8') as setting:
            config = json.load(setting)
            output = config['output']
            input = config['input']
            return config
            print('Succesfully loaded "config.json"')
    except:
        print('Failed loading "config.json"')

def writeFile(namesAndLastnames):
    f = open("%s\\%s" % (path, config['output']), "a")
    for i in range(int((len(namesAndLastnames))/2)):
        f.write("%s\n" % (namesAndLastnames[i]))
    print('Succesfully saved %s names and lastnames, from %s st/nd/rd/th file.' % (int((len(namesAndLastnames))/2), valFiles))

def checkNames(name):
    namesAndLastnames = []
    bigLetters = re.findall('([A-Z])', name)
    valBigLetters = len(bigLetters)
    for i in range(valBigLetters):
        comma = name.find(",")
        namesAndLastnames.append(name[1:comma])
        name = name.replace(name[1:comma+2], "")
    writeFile(namesAndLastnames)

def readFiles(dict):
    f = open(dict, "r", encoding="utf-8")
    names = f.read()
    checkNames(names)
    #index1 = names.find(","))


path = os.path.dirname(os.path.realpath(__file__))
config = readConfig()
output = "%s\\%s" % (path, config['input'])
f = open("%s\\%s" % (path, config['output']), "w+")
files = []
valFiles = 1

for r, d, f in os.walk(output):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

for f in files:
    readFiles(f)
    valFiles = valFiles + 1