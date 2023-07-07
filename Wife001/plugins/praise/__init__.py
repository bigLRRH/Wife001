from nonebot import get_driver

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

from nonebot import on_command

prise = on_command("怎么样")
prise = on_command("如何")

@prise.handle()
async def prise_response():
    await prise.finish("太强了")