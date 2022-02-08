import json

file_contents = ''

with open('Casual\All Dank Memer Item Bundles.json', 'r') as categ_all_dank_cmds_json:
	all_dank_cmds_categ: dict = json.load(categ_all_dank_cmds_json)

for category in all_dank_cmds_categ:
	file_contents += '-' * 20 + f'  {category}  ' + '-' * 20 + '\n'

	for command in all_dank_cmds_categ.get(category):
		file_contents += (' ' * 24) + command + '\n'
	
	file_contents += '-' * (40 + len(str(category) + '    ')) + '\n\n\n\n'
		# print(command)

with open('Casual\All Dank Memer Items.txt', 'w') as all_dank_cmds_txt:
	print(all_dank_cmds_txt.write(file_contents))
