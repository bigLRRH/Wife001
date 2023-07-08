from nonebot import get_driver

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler

# @scheduler.scheduled_job("cron", hour='8', minute='00', id="play_genshin")
# async def play_genshin():
    