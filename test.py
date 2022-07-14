import pandas as pd

d = pd.read_csv("marvel_cinematic_universe.csv", header = 0)

mcu = {}

mcu['shows'] = []
mcu['films'] = []

for film in d[d['media'] == "Film"].property:
    mcu['films'].append({'name': film})

for show in d[d['media'] == 'Series'].property:
    mcu['shows'].append({'name': show})

print(mcu)