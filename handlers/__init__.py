from aiogram import Router
from .users import user_router




def setup_handlers():
    main_router=Router()
    main_router.include_router(user_router)


    return main_router