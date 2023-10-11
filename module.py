from PIL import Image
import pillow_heif
import pathlib
import os

def multiple_process(target_object, status_function):
    if target_object:
        total = len(target_object)
        count = 1
        for tar in target_object:
            output_path = save_to_path_getter(tar)
            output_name = pathlib.Path(tar).name
            if converter(tar, output_path, "JPEG"):
                status_function(f"{count}/{total} Converted!")
                count += 1


def save_to_path_getter(dir, format=None):
    format_library = {"JPEG":".jpg"}
    source_path = pathlib.Path(dir)
    parent = source_path.parent
    filename = source_path.stem
    suffix = source_path.suffix
    if not format:
        con_suffix = format_library["JPEG"]
    else:
        con_suffix = format_library[format]
    output_filename = f"{filename}_converted{con_suffix}"
    output_path = os.path.join(parent, output_filename)
    sub = 1
    while os.path.exists(output_path):
        output_filename = f"{filename}_converted{str(sub)}{con_suffix}"
        output_path = os.path.join(parent, output_filename)
        sub += 1
    return output_path


def converter(path, save_to_path, format):
    heif = pillow_heif.read_heif(path)
    for attri in heif:
        convert_to_image = Image.frombytes(
        attri.mode,
        attri.size,
        attri.data,
        "raw",
        attri.mode,
        attri.stride
        )
    convert_to_image.save(save_to_path, format)
    return 1

def is_image(path):
    #image_file_suffixes = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.ico', '.jfif', '.heif', '.heic', '.svg', '.raw', '.indd', '.ai', '.eps', '.pdf')
    image_file_suffixes = ('.heif', '.heic')
    file_type = pathlib.Path(path).suffix.lower()
    if file_type in image_file_suffixes:
        return 1
    return 0
