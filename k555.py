# Напишите код, который запускается из командной строки
# и получает на вход путь до директории на ПК. Соберите
# информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
# имя файла без расширения или название каталога,
# расширение, если это файл,флаг каталога,название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

from collections import namedtuple
import os
import logging
import argparse




def directory_traversal(directory_address: str = "dir_f", directory_entry:str = "directory entry"):
    """Функция, которая получает на вход директорию
       и рекурсивно обходит её и все вложенные директории
    """

    folder_contents = namedtuple('folder_contents', ['file_name', 'file_extension','catalog', 'parent_directory'])
    logging.basicConfig(filename=directory_entry + '.log.', filemode='w',
                        encoding='utf-8', level=logging.INFO)
    for roots, dirs, files in os.walk(directory_address):
        for file in files:
            info_folder_contents = folder_contents(file.split(".")[0], str(*file.rsplit(".")[-1:]), str(*roots.rsplit("\\")[-1:]), roots.rsplit("\\")[0])
            logging.info(info_folder_contents)

def parse():
    parser = argparse.ArgumentParser(prog=directory_traversal)
    parser.add_argument('-c','--directory_address', default="dir_f")
    arguments = parser.parse_args()
    print(arguments.directory_address)

    return directory_traversal(f'{arguments.directory_address}')



if __name__ == '__main__':
    print(parse())
