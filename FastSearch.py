# -*- coding: utf-8 -*-
from __future__ import division
from urllib.parse import quote


HelpMessage ='''------MCDR FastSearch------
一个支持游戏内搜索的插件
§a【格式说明】§r
§a指令缩写
!!fs -获取帮助信息
!!fs mw [搜索内容] -在Minecraft维基上搜索
!!fs bd [搜索内容] -在百度上搜索
!!fs bl [搜索内容] -在b站上搜索
!!fs zh [搜索内容] -在知乎上搜索
!!fs mb [搜索内容] -在mcbbs上搜索
!!fs mm [搜索内容] -在mc百科上搜索
§a指令全写
!!fs help -获取帮助信息
!!fs minecraftwiki [搜索内容] -在Minecraft维基上搜索
!!fs baidu [搜索内容] -在百度上搜索
!!fs bilibili [搜索内容] -在b站上搜索
!!fs zhihu [搜索内容] -在知乎上搜索
!!fs mcbbs [搜索内容] -在mcbbs上搜索
!!fs mcmod [搜索内容] -在mc百科上搜索
--------------------------------'''

def work(server, info):
  if info.is_player == 1:
    if info.content.startswith('!!fs mw '):
      result = info.content[8:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 Minecraft维基 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://minecraft-zh.gamepedia.com/index.php?search=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs bd '):
      result = info.content[8:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 百度 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://www.baidu.com/s?wd=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs bl ') or info.content.startswith('!!fs bilibili'):
      result = info.content[8:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 b站 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://search.bilibili.com/all?keyword=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs zh ') or info.content.startswith('!!fs zhihu'):
      result = info.content[8:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 知乎 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://www.zhihu.com/search?type=content&q=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs mb ') or info.content.startswith('!!fs mcbbs'):
      result = info.content[8:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 mcbbs 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://www.mcbbs.net/search.php?searchsubmit=yes&wd=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs mm ') or info.content.startswith('!!fs mcmod'):
      result = info.content[8:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 mc百科 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://www.mcmod.cn/s?key=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs minecraftwiki '):
      result = info.content[19:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 Minecraft维基 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://minecraft-zh.gamepedia.com/index.php?search=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs baidu '):
      result = info.content[12:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 百度 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://www.baidu.com/s?wd=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs bilibili '):
      result = info.content[14:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 b站 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://search.bilibili.com/all?keyword=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs zhihu '):
      result = info.content[11:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 知乎 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://www.zhihu.com/search?type=content&q=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs mcbbs '):
      result = info.content[11:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 mcbbs 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://www.mcbbs.net/search.php?searchsubmit=yes&wd=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs mcmod '):
      result = info.content[11:]
      search = 'tellraw ' + info.player + ' {"text":"[FastSearch]: 在 mc百科 上的搜索结果","underlined":"true","clickEvent":{"action":"open_url","value":"https://www.mcmod.cn/s?key=' + quote(result) + '"}}'
      server.execute(str(search))
    elif info.content.startswith('!!fs') or info.content.startswith('!!fs help'):
      server.say(HelpMessage)
      #else

# MCDaemon
def onServerInfo(server, info):
	if info.isPlayer == 1:
		work(server, info)


# MCDReforged
def on_info(server, info):
	if info.is_player:
		work(server, info)


def on_load(server, old):
	server.add_help_message('!!fs <mw/bd/bl/zh/mb/mm> <comment>', '在 <mc维基/百度/b站/知乎/mcbbs/mc百科> 上搜索 <comment>')