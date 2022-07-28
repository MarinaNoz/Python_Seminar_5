#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

from ntpath import join


enter_text = 'абвгдейка - это передача'
def delete_words(enter_text):
    enter_text = list(filter(lambda x: 'абв' not in x, enter_text.split()))
    return " " .join(enter_text)

enter_text = delete_words(enter_text)
print(enter_text) 