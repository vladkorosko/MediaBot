from PIL import Image
from get_extension import get_format as gf


def resize_photo(file_path: str, new_width: int, new_height: int):
    try:
        name, format_file = gf(file_path)
        if format_file not in [".bmp", ".gif", ".jpg", ".jpeg", ".png", ".tiff"]:
            return "File format is not supported for this operation"

        img = Image.open(file_path)
        result_name = name + "_result" + format_file
        img.resize((new_width, new_height)).save(result_name)
    except FileNotFoundError:
        return "Missing file"
