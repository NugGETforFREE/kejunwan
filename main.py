
import os
import subprocess
import datetime
from colorama import Fore, Style
import json

viod= "              "

directories = []

# Функция для загрузки директорий из файла
directories = []

# Файл для хранения директорий
DIRECTORY_FILE = "directories.json"

# Функция для загрузки директорий из файла
def load_directories(file_path):
    global directories
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            directories = json.load(file)
    else:
        # Настройка стандартных значений директорий
        directories = [
            "/storage/emulated/0/pubgmobile/",
            "/storage/emulated/0/pubgmobile/OutPut/",
            "/storage/emulated/0/pubgmobile/repack/",
            "/storage/emulated/0/PeaceElite/",
            "/storage/emulated/0/PeaceElite/output/",
            "/storage/emulated/0/PeaceElite/repack/"
        ]
        save_directories(file_path)

# Функция для сохранения директорий в файл
def save_directories(file_path):
    with open(file_path, 'w') as file:
        json.dump(directories, file, indent=4)

# Функция для редактирования директорий
def edit_directories():
    global directories
    print(gradient_text("Текущие директории:", "00FF00", "FFFFFF"))
    for index, directory in enumerate(directories, start=1):
        print(gradient_text(f"{index}) {directory}", "00FFFF", "FFFFFF"))

    try:
        index_input = input(gradient_text("Введите номер каталога для редактирования (или 0 для выхода): ", "00FF00", "FFFFFF")).strip()
        if index_input == '0':
            return

        index = int(index_input) - 1
        if 0 <= index < len(directories):
            new_directory = input(gradient_text("Введите новый путь для каталога: ", "00FF00", "FFFFFF")).strip()
            directories[index] = new_directory
            print(gradient_text(f"Каталог обновлён на: {new_directory}", "00FF00", "FFFFFF"))
            save_directories(DIRECTORY_FILE)  # Сохраняем изменения в файл
        else:
            print(gradient_text("Неверный индекс. Пожалуйста, попробуйте еще раз.", "FF0000", "FFFFFF"))
    except ValueError:
        print(gradient_text("Введите правильное целое число.", "FF0000", "FFFFFF"))
        
def gradient_text(text, start_color, end_color):
    """Creates gradient text from start_color to end_color."""
    start_rgb = [int(start_color[i:i + 2], 16) for i in (0, 2, 4)]
    end_rgb = [int(end_color[i:i + 2], 16) for i in (0, 2, 4)]

    gradient = ''
    for i in range(len(text)):
        ratio = i / len(text)
        rgb = [int(start_rgb[j] + (end_rgb[j] - start_rgb[j]) * ratio) for j in range(3)]
        gradient += f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text[i]}"
    
    return gradient + Style.RESET_ALL

def get_current_datetime():
    """Returns the current date and time as a formatted string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def print_main_menu():
    print(viod + gradient_text("\n\n\n\n\n\n" + get_current_datetime() + " │ Telegram: @kejunwan │ Repacker • Free Tool", "0000FF", "00FFFF"))
    print()
    print(viod + gradient_text("┌───────────────────────────────┐", "0000FF", "00FFFF"))
    print(viod + gradient_text("│  PUBG Mobile  │  Peace Elite  │", "0000FF", "00FFFF"))
    print(viod + gradient_text("│───────────────────────────────│", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[1] Unpack OBB │[3] Unpack PAK │", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[2] Repack OBB │[4] Repack PAK │", "0000FF", "00FFFF"))
    print(viod + gradient_text("│───────────────────────────────│", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[5] يساعد/Help/帮助/Помощь/मदद │", "0000FF", "00FFFF"))
    print(viod + gradient_text("│───────────────────────────────│", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[6] Settings/Настройки/设置    │", "0000FF", "00FFFF"))
    print(viod + gradient_text("│───────────────────────────────│", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[0] مخرج/EXIT/退出/Выйти/पीछे   │", "0000FF", "00FFFF"))
    print(viod + gradient_text("└───────────────────────────────┘", "0000FF", "00FFFF"))

def print_unpack_menu():
    print()
def print_repack_menu():
    print()

def list_files_in_directory(directory, file_extension):
    """Lists files in the given directory for the specified extension."""
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"目录不存在 '{directory}'")
        
        files = os.listdir(directory)
        target_files = [file for file in files if file.endswith(file_extension)]

        if not target_files:
            print(gradient_text(f"在目录{directory}中未发现 {file_extension} 文件。", "FF0000", "FFFFFF"))
            return None

        print(gradient_text(f"文件 {directory}: ", "00FF00", "FFFFFF"))
        for index, file_name in enumerate(target_files, start=1):
            print(gradient_text(f"{index}) {file_name}", "0000FF", "00FFFF"))

        return target_files

    except FileNotFoundError as e:
        print(gradient_text(str(e), "FF0000", "FFFFFF"))
    except PermissionError:
        print(gradient_text(f"访问目录的权限被拒绝: '{directory}.", "FF0000", "FFFFFF"))
    except Exception as e:
        print(gradient_text(f"访问目录出错: {e}", "FF0000", "FFFFFF"))

    return None

def execute_command(command):
    """Executes the given shell command and prints the output or error."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(gradient_text(result.stdout.strip(), "00FF00", "FFFFFF"))  # Print command output
    except subprocess.CalledProcessError as e:
        print(gradient_text(f"执行命令出错: {e}\n{e.stderr.strip()}", "FF0000", "FFFFFF"))

def main():
    global directories
    load_directories(DIRECTORY_FILE)  # Загружаем директории при запуске
   
    subprocess.call("chmod +x quickbms", shell=True)

    while True:
        print_main_menu()
        choice = input(gradient_text("输入您的选择: ", "00FF00", "FFFFFF")).strip()

        if choice == '1':
            
                print_unpack_menu()
                directory = directories[0]
                files = list_files_in_directory(directory, '.obb')
                if files:
                    index_input = input(gradient_text("Enter the file index to unpack (or 0 to go back): ", "00FF00", "FFFFFF")).strip()
                    if index_input == '0':
                        break
                    if not index_input:
                        print(gradient_text("输入内容不能为空。 请重试。", "FF0000", "FFFFFF"))
                        continue
                    try:
                        index = int(index_input) - 1
                        if 0 <= index < len(files):
                            command = f"qemu-i386 quickbms pubgm_obb.bms {os.path.join(directory, files[index])} {directory[1]}"
                            execute_command(command)
                        else:
                            print(gradient_text("索引无效。 请重试。", "FF0000", "FFFFFF"))
                    except ValueError:
                        print(gradient_text("请输入有效的整数。", "FF0000", "FFFFFF"))

        elif choice == '2':
            
                print_repack_menu()
                directory = directories[0]
                files = list_files_in_directory(directory, '.obb')
                if files:
                    index_input = input(gradient_text("Enter the file index to repack (or 0 to go back): ", "00FF00", "FFFFFF")).strip()
                    if index_input == '0':
                        break
                    if not index_input:
                        print(gradient_text("输入内容不能为空。 请重试。", "FF0000", "FFFFFF"))
                        continue
                    try:
                        index = int(index_input) - 1
                        if 0 <= index < len(files):
                            command = f"qemu-i386 quickbms -g -w -r -r pubgm_obb.bms {os.path.join(directory, files[index])} {directory[2]}"
                            execute_command(command)
                        else:
                            print(gradient_text("索引无效。 请重试。", "FF0000", "FFFFFF"))
                    except ValueError:
                        print(gradient_text("请输入有效的整数。", "FF0000", "FFFFFF"))

        elif choice == '3':
                print_unpack_menu()
                directory = directories[3]
                files = list_files_in_directory(directory, '.pak')
                if files:
                    index_input = input(gradient_text("输入要解压的文件索引（或 0 表示返回）：", "00FF00", "FFFFFF")).strip()
                    if index_input == '0':
                        break
                    if not index_input:
                        print(gradient_text("输入内容不能为空。 请重试。", "FF0000", "FFFFFF"))
                        continue
                    try:
                        index = int(index_input) - 1
                        if 0 <= index < len(files):
                            command = f"qemu-i386 quickbms chinaNB.bms {os.path.join(directory, files[index])} {directories[4]}"
                            execute_command(command)
                        else:
                            print(gradient_text("索引无效。 请重试。", "FF0000", "FFFFFF"))
                    except ValueError:
                        print(gradient_text("", "FF0000", "FFFFFF"))

        elif choice == '4':
            
                print_repack_menu()
                directory = directories[3]
                files = list_files_in_directory(directory, '.pak')
                if files:
                    index_input = input(gradient_text("输入要重新打包的文件索引（或 0 表示返回）：", "00FF00", "FFFFFF")).strip()
                    if index_input == '0':
                        break
                    if not index_input:
                        print(gradient_text("输入内容不能为空。 请重试。", "FF0000", "FFFFFF"))
                        continue
                    try:
                        index = int(index_input) - 1
                        if 0 <= index < len(files):
                            command = f"qemu-i386 quickbms -g -w -r -r chinaNB.bms {os.path.join(directory, files[index])} {directories[5]}"
                            execute_command(command)
                        else:
                            print(gradient_text("索引无效。 请重试。", "FF0000", "FFFFFF"))
                    except ValueError:
                        print(gradient_text("请输入有效的整数。", "FF0000", "FFFFFF"))

        elif choice == '5':
            print(gradient_text("\n\n\n\n\n它是一款用于解压和打包 PAK（和平精英）、解压和打包 OBB（PUBG Mobile）的工具。 \n如何开始使用\n1. 输入 9999 创建您想要的文件夹\n2. （《PUBG Mobile》）转到以下目录：/storage/emulated/0/PubgMobile/ 并将 OBB 文件拖放到此处，以便与它们进一步互动。\n3. （和平精英版）转到以下目录：/storage/emulated/0/PeaceEilte/ 并将 PAK 文件拖放到此处，以便进一步交互。\n4. 在 Repack 文件夹中拖放已修改的 .uexp 或 .dat 文件。\n5. OutPut 文件夹将包含已解压的文件。\n6. 一切准备就绪！ 工具已准备就绪\nchannel: @kejunwan\nchannel: @kejunwan\nchannel: @kejunwan\n\n\n9999) 创建文件夹（创建的文件夹将显示在控制台中)", "00FFFF", "0000FF"))
        elif choice == '9999':
    
               for director in directories:
                    try:
                       os.makedirs(director, exist_ok=True)
                       print(f"Directory created: {director}")
                    except Exception as e:
                       print(f"Error creating directory {director}: {e}")
        elif choice == '6':
            edit_directories()

        elif choice == '0':
            print(gradient_text("Exiting...", "FF0000", "FFFFFF"))
            break
            
        else:
            print(gradient_text("选择无效。 请重试。", "FF0000", "FFFFFF"))

if __name__ == "__main__":
    main()