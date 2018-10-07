from wxpy import *


# 初始化机器人，扫码登陆
# bot = Bot()
bot = Bot(console_qr=True, cache_path=True) # 保留缓存自动登录
friends = bot.friends()
for friend in friends:
    print(friend.name,friend.sex,friend.signature,friend.province,friend.city)
    # name
    # sex   (0:不清楚 1:男 2:女)
    # signature
    # province
    # city




