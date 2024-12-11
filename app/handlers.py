from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

admin = Router()


@admin.message(CommandStart)
async def cmd_start(message: Message):
    await message.answer('Привет Админ')
