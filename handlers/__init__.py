from aiogram import F, Router

from .menu import menu_router
from .echo import echo_router
from .review_dialog import review_router
from .start import start_router
# from .picture import picture_router
from .my_info import my_info_router
from .recipes import recipe_router
from .dishes import dishes_router

# from .group_activities import group_router

private_router = Router()

private_router.include_router(review_router)
private_router.include_router(start_router)


private_router.message.filter(F.chat.type == "private")