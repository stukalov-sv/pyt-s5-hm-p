# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

import os


def rle_zip_algorithm(data):
    zipping = ''
    prev_char = ''
    count = 1

    for char in data:
        if char != prev_char:
            if prev_char:
                zipping += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        zipping += str(count) + prev_char
        return zipping


def rle_restore_algorithm(data):
    restore = ''
    count = ''

    for char in data:
        if char.isdigit():
            count += char
        else:
            restore += char * int(count)
            count = ''

    return restore


path1 = os.path.join('folder', 'file4hm_1.txt')
path2 = os.path.join('folder', 'file4hm_2.txt')

with open(path1, 'w') as writer:
    writer.write('aaaaaaabbbbbbbbbddddjjjjjjkkkkkkkoooooo')

correct_list = []

with open(path1, 'r') as reader:
    text = reader.readline()
    print(f'Original text: {text}\n')
    zipped_text = rle_zip_algorithm(text)
    restored_text = rle_restore_algorithm(zipped_text)

with open(path2, 'w') as writer:
    writer.write(zipped_text + '\n')
    writer.write(restored_text)

with open(path2, 'r') as reader:
    text1 = reader.readline()
    print(f'Zipped text: {text1}')
    text2 = reader.readline()
    print(f'Restored text: {text2}')
