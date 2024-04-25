from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

inline_keyboard = InlineKeyboardMarkup()
inline_keyboard.row(InlineKeyboardButton('Andijan Viloyati', callback_data='Andijon'), (InlineKeyboardButton('Namangan Viloyati', callback_data='Namangan')))
inline_keyboard.row(InlineKeyboardButton('Farg\'ona Viloyati', callback_data='Fargona'), (InlineKeyboardButton('Xorazm Viloyati', callback_data='Xorazm')))
inline_keyboard.row(InlineKeyboardButton('Surxondaryo Viloyati', callback_data='Surxondaryo'), (InlineKeyboardButton('Qoraqalpog\'iston Respublikasi', callback_data='Nukus')))
inline_keyboard.row(InlineKeyboardButton('Buxoro Viloyati', callback_data='Buxoro'), (InlineKeyboardButton('Jizzax Viloyati', callback_data='Jizzax')))
inline_keyboard.row(InlineKeyboardButton('Toshkent Viloyati', callback_data='Toshkent'), (InlineKeyboardButton('Qarshi Viloyati', callback_data='Qarshi')))
inline_keyboard.row(InlineKeyboardButton('Navoiy Viloyati', callback_data='Navoiy'), (InlineKeyboardButton('Samarqand Viloyati', callback_data='Samarqand')))
inline_keyboard.row(InlineKeyboardButton('Sirdaryo Viloyati', callback_data='Sirdaryo'))

andijon_keyboard = InlineKeyboardMarkup()
andijon_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='andijon_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='andijon_osimlik'))

fargona_keyboard = InlineKeyboardMarkup()
fargona_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='fargona_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='fargona_osimlik'))

namangan_keyboard = InlineKeyboardMarkup()
namangan_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='namangan_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='namangan_osimlik'))

xorazm_keyboard = InlineKeyboardMarkup()
xorazm_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='xorazm_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='xorazm_osimlik'))

surxondaryo_keyboard = InlineKeyboardMarkup()
surxondaryo_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='surxondaryo_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='surxondaryo_osimlik'))

nukus_keyboard = InlineKeyboardMarkup()
nukus_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='nukus_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='nukus_osimlik'))

buxoro_keyboard = InlineKeyboardMarkup()
buxoro_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='buxoro_hayvon'),InlineKeyboardButton('🌱O\'simliklar',callback_data='buxoro_osimlik'))

jizzax_keyboard = InlineKeyboardMarkup()
jizzax_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='jizzax_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='jizzax_osimlik'))

toshkent_keyboard = InlineKeyboardMarkup()
toshkent_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='toshkent_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='toshkent_osimlik'))

qarshi_keyboard = InlineKeyboardMarkup()
qarshi_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='qarshi_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='qarshi_osimlik'))

navoiy_keyboard = InlineKeyboardMarkup()
navoiy_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='navoiy_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='navoiy_osimlik'))

samarqand_keyboard = InlineKeyboardMarkup()
samarqand_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='samarqand_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='samarqand_osimlik'))

sirdaryo_keyboard = InlineKeyboardMarkup()
sirdaryo_keyboard.row(InlineKeyboardButton('🐍 Hayvonlar',callback_data='sirdaryo_hayvon'),InlineKeyboardButton('🌱 O\'simliklar',callback_data='sirdaryo_osimlik'))


joylashuv_locatsiya = InlineKeyboardMarkup()
joylashuv_locatsiya.row(InlineKeyboardButton('📋 Ma\'lumot',callback_data='fargona_hayvon_malumot'),InlineKeyboardButton('📌 Joylashuv',callback_data='fargona_hayvon_joylashuv'))
