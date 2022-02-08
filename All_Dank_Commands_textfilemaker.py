import json

file_contents = ''

with open('All Dank Memer Commands (Categorised).json', 'r') as categ_all_dank_cmds_json:
	categ_all_dank_cmds: dict = json.load(categ_all_dank_cmds_json)

for category in categ_all_dank_cmds:
	file_contents += '-' * 20 + f'  {category}  ' + '-' * 20 + '\n'

	for command in categ_all_dank_cmds.get(category):
		file_contents += (' ' * 24) + command + '\n'
	
	file_contents += '-' * (40 + len(str(category) + '    ')) + '\n\n\n\n'
		# print(command)

with open('All Dank Memer Commands.txt', 'w') as all_dank_cmds_txt:
	print(all_dank_cmds_txt.write(file_contents))
