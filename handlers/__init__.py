from aiogram import F, Router

from .menu import menu_router
from .echo import echo_router
from .review_dialog import review_router
from .start import start_router
# from .picture import picture_router
from .my_info import my_info_router
from .recipes import recipe_router
from .dishes import dishes_router
from .house_kg import house_router

from .group_activities import group_router

private_router = Router()

private_router.include_router(review_router)
private_router.include_router(start_router)
# private_router.include_router(picture_router)
private_router.include_router(menu_router)

private_router.include_router(my_info_router)
private_router.include_router(recipe_router)
private_router.include_router(dishes_router)
private_router.include_router(house_router)
private_router.include_router(echo_router)

private_router.message.filter(F.chat.type == "private")