from PIL import Image
from get_extension import get_format as gf


def convert_to_jpg(file_path):
    name, format_file = gf(file_path)
    result_name = name + "_result" + ".jpg"
    try:
        if format_file in [".bmp", ".gif", ".jpg", ".jpeg", ".png", ".tiff"]:
            im = Image.open(file_path)
            im.save(result_name)
        else:
            return "File format is not supported for this operation"
    except FileNotFoundError:
        return "Missing file"
    except OSError:
        im = Image.open(file_path)
        im = im.convert('RGB')
        im.save(result_name)


def convert_to_jpeg(file_path):
    name, format_file = gf(file_path)
    result_name = name + "_result" + ".jpeg"
    try:
        if format_file in [".bmp", ".gif", ".jpg", ".jpeg", ".png", ".tiff"]:
            im = Image.open(file_path)
            im.save(result_name)
        else:
            return "File format is not supported for this operation"
    except FileNotFoundError:
        return "Missing file"
    except OSError:
        im = Image.open(file_path)
        im = im.convert('RGB')
        im.save(result_name)


def convert_to_png(file_path):
    name, format_file = gf(file_path)
    result_name = name + "_result" + ".png"
    try:
        if format_file in [".bmp", ".gif", ".jpg", ".jpeg", ".png", ".tiff"]:
            im = Image.open(file_path)
            im.save(result_name)
        else:
            return "File format is not supported for this operation"
    except FileNotFoundError:
        return "Missing file"

