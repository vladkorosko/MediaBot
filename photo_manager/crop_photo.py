from PIL import Image
from get_extension import get_format as gf


def crop_photo(file_path: str, start_x: int, start_y: int, finish_x: int, finish_y: int):
    try:
        name, format_file = gf(file_path)
        if format_file not in ['.bmp', '.gif', '.jpg', '.jpeg', '.png', '.tiff']:
            return 'File format is not supported for this operation'

        img = Image.open(file_path)
        w, h = img.size

        result_name = 'result_' + file_path
        if start_y >= finish_y or start_x >= finish_x or finish_y > h or finish_x > w:
            return 'Wrong coordinates'
        img.crop((start_x, start_y, finish_x, finish_y))\
            .save(result_name)
    except FileNotFoundError:
        return 'Missing file'
