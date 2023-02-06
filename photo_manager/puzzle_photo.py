import os
import random

from PIL import Image


def puzzle_photo(file_path, parts):
    name, ext = os.path.splitext(file_path)
    img = Image.open(file_path)
    w, h = img.size

    if w % parts != 0:
        w = parts * (w // parts)
    if h % parts != 0:
        h = parts * (h // parts)

    new_size = (w, h)

    part_w = w // parts
    part_h = h // parts

    table = []
    for i in range(parts):
        for j in range(parts):
            box = (int(i * part_w), int(j * part_h), int((i + 1) * part_w), int((j + 1) * part_h))
            table.append(img.crop(box))

    random.seed()
    random.shuffle(table)
    new_im = Image.new('RGB', new_size)

    for i in range(parts):
        for j in range(parts):
            box = (int(i * part_w), int(j * part_h), int((i + 1) * part_w), int((j + 1) * part_h))
            new_im.paste(table[i*parts + j], box)

    result = file_path[:-4:] + "_result.jpg"
    new_im.save(result)

