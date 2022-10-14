from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
    InlineKeyboardButton, InlineKeyboardMarkup

# Create button to interact with
inline_keyboard_mas = InlineKeyboardButton('MAS', callback_data='MAS')
inline_keyboard_fem = InlineKeyboardButton('FEM', callback_data='FEM')
inline_keyboard_gen = InlineKeyboardButton('GEN', callback_data='GEN')

# combine buttons
inline_kb = InlineKeyboardMarkup()

inline_kb.add(inline_keyboard_mas)
inline_kb.add(inline_keyboard_fem)
inline_kb.add(inline_keyboard_gen)
