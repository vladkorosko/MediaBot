from PIL import Image
from get_extension import get_format as gf


def crop_photo(file_path: str, start_x: int, start_y: int, finish_x: int, finish_y: int):
    try:
        img = Image.open(file_path)
        w, h = img.size

        name, format_file = gf(file_path)
        result_name = name + "_result" + format_file
        if start_y >= finish_y or start_x >= finish_x or finish_y > h or finish_x > w:
            return "Wrong coordinates"
        img.crop((start_x, start_y, finish_x, finish_y))\
            .save(result_name)
    except FileNotFoundError:
        return "Missing file"
