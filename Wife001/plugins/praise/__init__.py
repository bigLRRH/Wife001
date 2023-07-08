from nonebot import get_driver

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

from nonebot import on_keyword

prise = on_keyword(keywords={"how", "如何", "怎么样"})


@prise.handle()
async def prise_handle():
    await prise.finish("太强了")