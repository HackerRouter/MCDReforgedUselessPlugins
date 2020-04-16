# -*- coding: utf-8 -*-

from __future__ import division

HelpMessage = '''------MCDR Fast Caculate------
一个支持游戏中计算数据的插件
§a【格式说明】§r
§7!!fc help §r显示帮助信息
§7!!fc caculate <comment> §r计算<comment>
§7!!fc c <comment> §r计算<comment>
§a【例子】§r
<HackerRouter> !!fc caculate 1+1
2
<HackerRouter> !!fc c 1
1'''

def calc(text):
	whitelist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', '+', '-', '*', '/', '(', ')', '<', '>', '=']
	text = text.replace('**', '')  # to avoid eeasee
	text_clean = ''
	for c in text:
		if c in whitelist:
			text_clean += c

	if len(text_clean) == 0:
		return None
	try:
		return str(eval(text_clean))
	except Exception as e:
		return str(e)


def work(server, info):
	if info.content.startswith('!!fc caculate') or info.content.startswith('!!fc c'):
		result = calc(info.content[2:])
		if result is not None:
			server.say(result)
	elif info.content.startswith('!!fc help') or info.content.startswith('!!fc'):
		server.say(HelpMessage)


# MCDaemon
def onServerInfo(server, info):
	if info.isPlayer == 1:
		work(server, info)


# MCDReforged
def on_info(server, info):
	if info.is_player:
		work(server, info)


def on_load(server, old):
	server.add_help_message('!!fc caculate <comment>', '计算<comment>')
