import os
import random

from PIL import Image


def puzzle_photo(file_path, parts):
    name, ext = os.path.splitext(file_path)
    img = Image.open(file_path)
    w, h = img.size

    table = []
    for i in range(parts):
        for j in range(parts):
            box = (int(i * w / parts), int(j * h / parts), int((i + 1) * w / parts), int((j + 1) * h / parts))
            table.append(img.crop(box))

    random.seed()
    random.shuffle(table)
    new_im = Image.new('RGB', (w, h))

    for i in range(parts):
        for j in range(parts):
            box = (int(i * w / parts), int(j * h / parts), int((i + 1) * w / parts), int((j + 1) * h / parts))
            new_im.paste(table[i*parts + j], box)

    new_im.save("result.jpg")

