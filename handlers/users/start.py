from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Text
from loader import dp
from loader import bot
from keyboards.default.main import back
from keyboards.inline.viloyat import *
from api import get_hayvon,get_osimlik
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.dispatcher.filters import Text



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\n"
                         f"Viloyatlardan birini tanlang.",reply_markup=inline_keyboard)
    # await bot.send_location(chat_id=message.chat.id,latitude=41.6693848423844,longitude=69.9577555065197)



@dp.callback_query_handler(Text(equals="Andijon"))
async def andijan(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=andijon_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='andijon_hayvon'))
async def andijan(call:types.CallbackQuery):
    hayvonlar = get_hayvon('Andijon')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='andijon_osimlik'))
async def andijan(call:types.CallbackQuery):
    osimliklar = get_osimlik('Andijon')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
    await call.answer(cache_time=60)

############################# Farg'ona #####################
@dp.callback_query_handler(Text(equals="Fargona"))
async def fargona(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=fargona_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='fargona_hayvon'))
async def fargona(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Fargona')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi,reply_markup=joylashuv_locatsiya)
@dp.callback_query_handler(Text(equals='fargona_osimlik'))
async def fargona(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Fargona')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi,reply_markup=joylashuv_locatsiya)
@dp.callback_query_handler(lambda c: c.data == 'fargona_hayvon_malumot')
async def joylashuv_locatsiya_malumot(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Fargona')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        oilasi = hayvon['nomi']['oilasi']['name']
        yili = hayvon['nomi']['yili']
        maqomi = hayvon['nomi']['maqomi']
        tarqalishi = hayvon['nomi']['tarqalishi']
        yashash_joylari = hayvon['nomi']['yashash_joylari']
        soni = hayvon['nomi']['soni']
        yashash_tarzi = hayvon['nomi']['yashash_tarzi']
        cheklovchi_omillar = hayvon['nomi']['cheklovchi_omillar']
        kupaytirish = hayvon['nomi']['kupaytirish']
        choralari = hayvon['nomi']['choralari']

    await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=f"Nomi : {nomi}\n\n Oilasi : {oilasi}\n\n Yili : {yili}\n\n Maqomi : {maqomi}\n\n Tarqalishi : {tarqalishi}\n\n Yashah joylari : {yashash_joylari}\n\n Soni : {soni}\n\n Yashash tarzi : {yashash_tarzi}\n\n Cheklovchi omillar : {cheklovchi_omillar}\n\n Ko'yaptirish : {kupaytirish}\n\n Choralar : {choralari}",reply_markup=back)
@dp.callback_query_handler(lambda c: c.data == 'fargona_hayvon_joylashuv')
async def joylashuv_locatsiya_joylashuv(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Fargona')
    for hayvon in hayvonlar:
        latitude = hayvon['x']
        longitude = hayvon['y']
    await bot.send_location(chat_id=call.from_user.id, latitude=latitude, longitude=longitude,reply_markup=back)
@dp.message_handler(Text('⬅️ back'))
async def orqaga(message:types.Message):
    await message.answer("Kerakli turni tanlang : ",reply_markup=inline_keyboard)


#################### Namangan #######################################
@dp.callback_query_handler(Text(equals="Namangan"))
async def namangan(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=namangan_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='namangan_hayvon'))
async def namangan(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Namangan')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
@dp.callback_query_handler(Text(equals='namangan_osimlik'))
async def namangan(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Namangan')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)


@dp.callback_query_handler(Text(equals="Xorazm"))
async def xorazm(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=xorazm_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='xorazm_hayvon'))
async def xorazm(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Xorazm')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
@dp.callback_query_handler(Text(equals='xorazm_osimlik'))
async def xorazm(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Xorazm')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)


@dp.callback_query_handler(Text(equals="Surxondaryo"))
async def surxondaryo(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=surxondaryo_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='surxondaryo_hayvon'))
async def surxondaryo(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Surxondaryo')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
@dp.callback_query_handler(Text(equals='surxondaryo_osimlik'))
async def surxondaryo(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Surxondaryo')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)


@dp.callback_query_handler(Text(equals="Nukus"))
async def nukus(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=nukus_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='nukus_hayvon'))
async def nukus(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Nukus')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
@dp.callback_query_handler(Text(equals='nukus_osimlik'))
async def nukus(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Nukus')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)

@dp.callback_query_handler(Text(equals="Buxoro"))
async def buxoro(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=buxoro_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='buxoro_hayvon'))
async def buxoro(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Buxoro')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
@dp.callback_query_handler(Text(equals='buxoro_osimlik'))
async def buxoro(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Buxoro')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)

@dp.callback_query_handler(Text(equals="Jizzax"))
async def jizzax(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=jizzax_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='jizzax_hayvon'))
async def jizzax(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Jizzax')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
@dp.callback_query_handler(Text(equals='jizzax_osimlik'))
async def jizzax(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Jizzax')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)

@dp.callback_query_handler(Text(equals="Toshkent"))
async def toshkent(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=toshkent_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='toshkent_hayvon'))
async def toshkent(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Toshkent')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
@dp.callback_query_handler(Text(equals='toshkent_osimlik'))
async def toshkent(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Toshkent')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)

@dp.callback_query_handler(Text(equals="Qarshi"))
async def qarshi(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=qarshi_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='qarshi_hayvon'))
async def qarshi(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Qarshi')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
@dp.callback_query_handler(Text(equals='qarshi_osimlik'))
async def qarshi(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Qarshi')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)

@dp.callback_query_handler(Text(equals="Navoiy"))
async def navoiy(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=navoiy_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='navoiy_hayvon'))
async def navoiy(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Navoiy')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
@dp.callback_query_handler(Text(equals='navoiy_osimlik'))
async def navoiy(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Navoiy')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)

@dp.callback_query_handler(Text(equals="Samarqand"))
async def samarqand(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=samarqand_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='samarqand_hayvon'))
async def samarqand(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Navoiy')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
@dp.callback_query_handler(Text(equals='samarqand_osimlik'))
async def samarqand(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Navoiy')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)

@dp.callback_query_handler(Text(equals="Sirdaryo"))
async def sirdaryo(call:types.CallbackQuery):
    await call.message.answer("Kerakli turni tanlang : ",reply_markup=sirdaryo_keyboard)
    await call.answer(cache_time=60)
@dp.callback_query_handler(Text(equals='sirdaryo_hayvon'))
async def sirdaryo(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    hayvonlar = get_hayvon('Sirdaryo')
    for hayvon in hayvonlar:
        nomi = hayvon['nomi']['nomi']
        photo = hayvon['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)
@dp.callback_query_handler(Text(equals='sirdaryo_osimlik'))
async def sirdaryo(call:types.CallbackQuery):
    await call.answer(cache_time=60)
    osimliklar = get_osimlik('Sirdaryo')
    for osimlik in osimliklar:
        nomi = osimlik['nomi']['nomi']
        photo = osimlik['nomi']['img']
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=nomi)