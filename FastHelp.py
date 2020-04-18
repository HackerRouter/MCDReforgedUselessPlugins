# -*- coding: utf-8 -*-
import copy
import re
import time

# set it to 0 to disable hightlight
# 将其设为0以禁用高亮
HIGHLIGHT_TIME = 15
# 将其设为0以禁用游戏模式更换
EFFECT_TIME = 15
# 将其设为0以禁用药水效果自救
CHANGE_MODE_TIME = 15
# 将其设为1开启游戏模式自救
CHANGE_MODE = 0
here_user = 0


def process_coordinate(text):
	data = text[1:-1].replace('d', '').split(', ')
	data = [(x + 'E0').split('E') for x in data]
	return tuple([int(float(e[0]) * 10 ** int(e[1])) for e in data])

#tellraw @a {"text":"\u70b9\u51fb\u4ee5\u4f20\u9001\uff01","clickEvent":{"action":"run_command","value":"tp @s ~ ~ ~"}}
def process_dimension(text):
	return int(text.lstrip(re.match(r'[\w ]+: ', text).group()))      #/effect give @a saturation 15 255


def display(server, name, position, dimension):
	global HIGHLIGHT_TIME
	global CHANGE_MODE
	dimension_display = {0: '§2主世界', -1: '§4地狱', 1: '§5末地'}
	position_show = '[x:{}, y:{}, z:{}]'.format(*position)
	server.say('[FastHelp] §e{}§r 在 {} §r{} 寻求帮助！'.format(name, dimension_display[dimension], position_show))
	#server.execute('tellraw @a {"text":"' + '§e{}§r @ {} §r{}'.format(name, dimension_display[dimension], position_show) + ' ,点击以传送！","clickEvent":{"action":"run_command","value":"tp @s {} {} {}'.format(*position) + '"}}')
	if HIGHLIGHT_TIME > 0:
		if CHANGE_MODE == 1:
			server.execute('gamemode spectator {}'.format(name))
			server.tell(name, '[FastHelp] 你将会无敌{}秒'.format(CHANGE_MODE_TIME))
			time.sleep( CHANGE_MODE_TIME )
			server.execute('gamemode survival {}'.format(name))
		else:
			server.execute('effect give {} minecraft:saturation {} 255 true'.format(name, EFFECT_TIME))
			server.execute('effect give {} minecraft:resistance {} 255'.format(name, EFFECT_TIME))
			server.execute('effect give {} minecraft:regeneration {} 255'.format(name, EFFECT_TIME))
			server.execute('effect give {} minecraft:glowing {} 0 true'.format(name, EFFECT_TIME))
			server.tell(name, '[FastHelp] 你将会被高亮且无敌{}秒'.format(HIGHLIGHT_TIME))


def on_info(server, info):
	if info.is_player and info.content == '!!fh':
		if hasattr(server, 'MCDR') and server.is_rcon_running():
			name = info.player
			position = process_coordinate(re.search(r'\[.*\]', server.rcon_query('data get entity {} Pos'.format(name))).group())
			dimension = process_dimension(server.rcon_query('data get entity {} Dimension'.format(name)))
			display(server, name, position, dimension)
		else:
			global here_user
			here_user += 1
			server.execute('data get entity ' + info.player)
	if not info.is_player and here_user > 0 and re.match(r'\w+ has the following entity data: ', info.content) is not None:
		name = info.content.split(' ')[0]
		dimension = int(re.search(r'(?<=Dimension: )-?\d', info.content).group())
		position_str = re.search(r'(?<=Pos: )\[.*?\]', info.content).group()
		position = process_coordinate(position_str)
		display(server, name, position, dimension)
		here_user -= 1


def onServerInfo(server, info):
	info2 = copy.deepcopy(info)
	info2.is_player = info2.isPlayer
	on_info(server, info2)


def on_load(server, old):
	server.add_help_message('!!fh', '输入!!fh以自救')
