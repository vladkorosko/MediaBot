from aiogram import types


def make_functional_markup():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_resize = types.KeyboardButton("Resize")
    button_compress = types.KeyboardButton("Compress")
    button_crop = types.KeyboardButton("Crop")
    button_change_format = types.KeyboardButton("Change format")

    markup.add(button_resize, button_change_format, button_crop, button_compress)

    return markup


def photo_or_video_text(is_photo: bool):
    if is_photo:
        return "photo"
    return "video"


def is_integer(number: str):
    for i in number:
        if i not in '0123456789':
            return False
    return True

