import os
import sys
from datetime import datetime
from colorama import Fore, init

#вызываем init() для консоли Windows
init()

date_int = datetime.now()
date_str = date_int.strftime('%d %b %Y')
all_cursors = None
cursors_name = [
    'Основной режим',
    'Выбор справки',
    'Фоновый режим',
    'Система занята',
    'Графическое выделение',
    'Выделение текста ',
    'Рукописный ввод',
    'Операция недоступна',
    'Изменение вертикальных размеров',
    'Изменение горизонтальных размеров ',
    'Изменение размеров по диагонали 1',
    'Изменение размеров по диагонали 2',
    'Перемещение',
    'Специальный выбор',
    'Выбор ссылки',
    'Выбор места',
    'Выбор человека',
]

selects_cursors = []

def tire(v):
    symbols = []
    len_v = len(v)
    for i in range(len_v):
        symbols.append('_')
    return symbols

def print_list(l):
    for i in range(len(l)):
        l[i] = f'{i}|' + l[i]
    print(', '.join(l))

#узнаем директорию папки
current_dir = os.path.dirname(sys.executable)#если хотите запустить программу ввиде python file то замените sys.executable на os.path.abspath(__file__)
print(f'Директория папки --> {current_dir}')
print(f'_____________________{''.join(tire(current_dir))}')

#узнаем все файлы в папке
all_files = os.listdir(current_dir)
for file in all_files[:]:
    if '.cur' not in file and '.ani' not in file:
        all_files.remove(file)
    
print(f'Количество фалов: {len(all_files)}')
print()
all_cursors = all_files.copy()
print_list(all_files)
print()
print()

for cursor in cursors_name:
    while True:
        choice = input(Fore.WHITE + f"Выберите курсор '{cursor}': ")
        try:
            print(Fore.GREEN + f'{cursor} это {all_files[int(choice)]}')
            selects_cursors.append(choice)
            print()
            break
        except IndexError:
            print(Fore.RED + 'Данного курсора не существует!')
        except ValueError:
            print(Fore.RED + 'Введите номер курсора!') 

name_cursor = input(Fore.WHITE + 'Выберете имя курсора :')

with open('install.inf', 'w') as file:
    file.write(
        f'''; {name_cursor} set made by CursorInstallerMaker
; {date_str}

[Version]
signature="$CHICAGO$"

[DefaultInstall]
CopyFiles = Scheme.Cur, Scheme.Txt
AddReg    = Scheme.Reg

[DestinationDirs]
Scheme.Cur = 10,"%CUR_DIR%"
Scheme.Txt = 10,"%CUR_DIR%"

[Scheme.Reg]
HKCU,"Control Panel\\Cursors\\Schemes","%SCHEME_NAME%",,"%10%\\%CUR_DIR%\\%pointer%,%10%\\%CUR_DIR%\\%help%,%10%\\%CUR_DIR%\\%work%,%10%\\%CUR_DIR%\\%busy%,%10%\\%CUR_DIR%\\%cross%,%10%\\%CUR_DIR%\\%text%,%10%\\%CUR_DIR%\\%hand%,%10%\\%CUR_DIR%\\%unavailiable%,%10%\\%CUR_DIR%\\%vert%,%10%\\%CUR_DIR%\\%horz%,%10%\\%CUR_DIR%\\%dgn1%,%10%\\%CUR_DIR%\\%dgn2%,%10%\\%CUR_DIR%\\%move%,%10%\\%CUR_DIR%\\%link%,%10%\\%CUR_DIR%\\%alternate%,%10%\\%CUR_DIR%\\%pin%,%10%\\%CUR_DIR%\\%person%"

[Scheme.Cur]
{all_cursors[int(selects_cursors[0])]}
{all_cursors[int(selects_cursors[1])]}
{all_cursors[int(selects_cursors[2])]}
{all_cursors[int(selects_cursors[3])]}
{all_cursors[int(selects_cursors[4])]}
{all_cursors[int(selects_cursors[5])]}
{all_cursors[int(selects_cursors[6])]}
{all_cursors[int(selects_cursors[7])]}
{all_cursors[int(selects_cursors[8])]}
{all_cursors[int(selects_cursors[9])]}
{all_cursors[int(selects_cursors[10])]}
{all_cursors[int(selects_cursors[11])]}
{all_cursors[int(selects_cursors[12])]}
{all_cursors[int(selects_cursors[13])]}
{all_cursors[int(selects_cursors[14])]}
{all_cursors[int(selects_cursors[15])]}
{all_cursors[int(selects_cursors[16])]}

[Scheme.Txt]

[Strings]
CUR_DIR       = "Cursors\\{name_cursor}"
SCHEME_NAME   = "{name_cursor}"
pointer       = "{all_cursors[int(selects_cursors[0])]}"
help          = "{all_cursors[int(selects_cursors[1])]}"
work          = "{all_cursors[int(selects_cursors[2])]}"
busy          = "{all_cursors[int(selects_cursors[3])]}"
text          = "{all_cursors[int(selects_cursors[4])]}"
unavailiable  = "{all_cursors[int(selects_cursors[5])]}"
vert          = "{all_cursors[int(selects_cursors[6])]}"
horz          = "{all_cursors[int(selects_cursors[7])]}"
dgn1          = "{all_cursors[int(selects_cursors[8])]}"
dgn2          = "{all_cursors[int(selects_cursors[9])]}"
move          = "{all_cursors[int(selects_cursors[10])]}"
link          = "{all_cursors[int(selects_cursors[11])]}"
cross         = "{all_cursors[int(selects_cursors[12])]}"
hand          = "{all_cursors[int(selects_cursors[13])]}"
alternate     = "{all_cursors[int(selects_cursors[14])]}"
pin           = "{all_cursors[int(selects_cursors[15])]}"
person        = "{all_cursors[int(selects_cursors[16])]}"	'''
    )

print()
print('Курсор инсталлер успешно создан!')
print()
exit = input('Press enter to exit ')
