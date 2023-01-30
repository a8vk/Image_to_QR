import qrcode.image.svg  # https://pypi.org/project/qrcode/
import os
from pathlib import Path

factory = qrcode.image.svg.SvgImage
image_dir = input("Каталог изображений: ")
web_dir = input("Сайт: ")

image_dir_svg = image_dir + "\\svg"

file_name = None

if os.path.isdir(image_dir):  # проверяет наличие пути
    if not os.path.isdir(image_dir_svg):  # проверяет наличие пути svg
        os.mkdir(Path(image_dir_svg))  # создать директорию svg
    for root, dirs, files in os.walk(image_dir):  # проход файлов
        for image_name in files:
            if not image_name[-3:] == "svg":
                data = web_dir + image_name
                file_name = Path(image_dir_svg).joinpath(image_name[:-4] + ".svg")
                img = qrcode.make(data, image_factory=factory)
                img.save(file_name)
            else:
                continue
else:
    print("Каталог не найден")
