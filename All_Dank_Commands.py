import json

with open(r'All Dank Memer Commands (Categorised).json', 'r') as dank_cmds_json:
    dank_cmds: dict = json.load(dank_cmds_json)

all_cmds = []

for cmd_list in dank_cmds.values():
    for cmd in cmd_list:
        all_cmds.append(cmd)
all_cmds.sort()

with open(r'All Dank Memer Commands.json', 'w') as all_dank_cmds_json:
    json.dump(all_cmds, all_dank_cmds_json, indent='\t')
