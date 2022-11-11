namedict = {"Smith", "Johnson", "Steve", "Smith", "Steve"}
namecounts = {}

for name in namedict:
    if name not in namecounts:
        namecounts[name] = 1
    else:
        namecounts[name] += 1

print(namecounts)