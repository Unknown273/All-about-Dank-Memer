import json

with open(r'All Dank Memer Item Bundles.json', 'r') as dank_items_json:
    dank_cmds: dict = json.load(dank_items_json)

all_items = []

for cmd_list in dank_cmds.values():
    for cmd in cmd_list:
        all_items.append(cmd)
all_items.sort()

with open('All Dank Memer Items.txt', 'w') as all_dank_items_json:
    all_dank_items_json.write('\n'.join(all_items))

with open(r'All Dank Memer Items.json', 'w') as all_dank_items_json:
    json.dump(all_items, all_dank_items_json, indent='\t')
