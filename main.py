import os
import subprocess
import datetime
import json
from colorama import Fore, Style

viod = "              "

# Стандартные директории
directories = [
    "/storage/emulated/0/pubgmobile/",
    "/storage/emulated/0/pubgmobile/OutPut/",
    "/storage/emulated/0/pubgmobile/repack/",
    "/storage/emulated/0/PeaceElite/",
    "/storage/emulated/0/PeaceElite/output/",
    "/storage/emulated/0/PeaceElite/repack/"
]

def gradient_text(text, start_color, end_color):
    """Создает градиентный текст от start_color до end_color."""
    start_rgb = [int(start_color[i:i + 2], 16) for i in (0, 2, 4)]
    end_rgb = [int(end_color[i:i + 2], 16) for i in (0, 2, 4)]

    gradient = ''
    for i in range(len(text)):
        ratio = i / len(text)
        rgb = [int(start_rgb[j] + (end_rgb[j] - start_rgb[j]) * ratio) for j in range(3)]
        gradient += f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text[i]}"
    
    return gradient + Style.RESET_ALL

def get_current_datetime():
    """Возвращает текущую дату и время в отформатированной строке."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def print_main_menu():
    print(viod + gradient_text("\n\n\n\n\n\n" + " " + get_current_datetime() + " │ Telegram: @kejunwan │ Repacker • Free Tool", "0000FF", "00FFFF"))
    print()
    print(viod + gradient_text("┌───────────────────────────────┐", "0000FF", "00FFFF"))
    print(viod + gradient_text("│  PUBG Mobile  │  Peace Elite  │", "0000FF", "00FFFF"))
    print(viod + gradient_text("│───────────────────────────────│", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[1] Unpack OBB │[3] Unpack PAK │", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[2] Repack OBB │[4] Repack PAK │", "0000FF", "00FFFF"))
    print(viod + gradient_text("│───────────────────────────────│", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[5] Помощь/Help/帮助/Помощь/मदद│", "0000FF", "00FFFF"))
    print(viod + gradient_text("│───────────────────────────────│", "0000FF", "00FFFF"))
    print(viod + gradient_text("│[0] Выход/EXIT/退出/Выйти/पीछे  │", "0000FF", "00FFFF"))
    print(viod + gradient_text("└───────────────────────────────┘", "0000FF", "00FFFF"))
    print()

def print_unpack_menu():
    print()

def print_repack_menu():
    print()

def list_files_in_directory(directory, file_extension):
    """Показывает файлы в данном каталоге с заданным расширением."""
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Каталог не найден: '{directory}'")

        files = os.listdir(directory)
        target_files = [file for file in files if file.endswith(file_extension)]

        if not target_files:
            print(gradient_text(f"Не найдено файлов с расширением {file_extension} в каталоге {directory}.", "FF0000", "FFFFFF"))
            return None

        print(gradient_text(f"Файлы в каталоге {directory}: ", "00FF00", "FFFFFF"))
        for index, file_name in enumerate(target_files, start=1):
            print(gradient_text(f"{index}) {file_name}", "0000FF", "00FFFF"))

        return target_files

    except FileNotFoundError as e:
        print(gradient_text(str(e), "FF0000", "FFFFFF"))
    except PermissionError:
        print(gradient_text(f"Отказано в доступе к каталогу: '{directory}.", "FF0000", "FFFFFF"))
    except Exception as e:
        print(gradient_text(f"Ошибка доступа к каталогу: {e}", "FF0000", "FFFFFF"))

    return None

def execute_command(command):
    """Выполняет данную команду оболочки и выводит результат или ошибку."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(gradient_text(result.stdout.strip(), "00FF00", "FFFFFF"))  # Вывод результата команды
    except subprocess.CalledProcessError as e:
        print(gradient_text(f"Ошибка выполнения команды: {e}\n{e.stderr.strip()}", "FF0000", "FFFFFF"))

def main():
    subprocess.call("chmod +x quickbms", shell=True)

    while True:
        print_main_menu()
        choice = input(gradient_text("Введите ваш выбор: ", "00FF00", "FFFFFF")).strip()

        if choice == '1':
            print_unpack_menu()
            directory = "/storage/emulated/0/pubgmobile/"
            files = list_files_in_directory(directory, '.obb')
            if files:
                index_input = input(gradient_text("Введите индекс файла для распаковки (или 0 для возврата): ", "00FF00", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("Ввод не может быть пустым. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms pubgm_obb.bms \"{os.path.join(directory, files[index])}\" \"/storage/emulated/0/pubgmobile/OutPut/\""
                        execute_command(command)
                    else:
                        print(gradient_text("Недействительный индекс. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                except ValueError:
                    print(gradient_text("Пожалуйста, введите действительное целое число.", "FF0000", "FFFFFF"))

        elif choice == '2':
            print_repack_menu()
            directory = "/storage/emulated/0/pubgmobile/"
            files = list_files_in_directory(directory, '.obb')
            if files:
                index_input = input(gradient_text("Введите индекс файла для упаковки (или 0 для возврата): ", "00FF00", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("Ввод не может быть пустым. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms -g -w -r -r pubgm_obb.bms \"{os.path.join(directory, files[index])}\" \"/storage/emulated/0/pubgmobile/repack/\""
                        execute_command(command)
                    else:
                        print(gradient_text("Недействительный индекс. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                except ValueError:
                    print(gradient_text("Пожалуйста, введите действительное целое число.", "FF0000", "FFFFFF"))

        elif choice == '3':
            print_unpack_menu()
            directory = "/storage/emulated/0/PeaceElite/"
            files = list_files_in_directory(directory, '.pak')
            if files:
                index_input = input(gradient_text("Введите индекс файла для распаковки (или 0 для возврата): ", "00FF00", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("Ввод не может быть пустым. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms chinaNB.bms \"{os.path.join(directory, files[index])}\" \"/storage/emulated/0/PeaceElite/output/\""
                        execute_command(command)
                    else:
                        print(gradient_text("Недействительный индекс. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                except ValueError:
                    print(gradient_text("Пожалуйста, введите действительное целое число.", "FF0000", "FFFFFF"))

        elif choice == '4':
            print_repack_menu()
            directory = "/storage/emulated/0/PeaceElite/"
            files = list_files_in_directory(directory, '.pak')
            if files:
                index_input = input(gradient_text("Введите индекс файла для упаковки (или 0 для возврата): ", "00FF00", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("Ввод не может быть пустым. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms -g -w -r -r chinaNB.bms \"{os.path.join(directory, files[index])}\" \"/storage/emulated/0/PeaceElite/repack/\""
                        execute_command(command)
                    else:
                        print(gradient_text("Недействительный индекс. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                except ValueError:
                    print(gradient_text("Пожалуйста, введите действительное целое число.", "FF0000", "FFFFFF"))

        elif choice == '5':
            print(gradient_text("\n\nЭто инструмент для распаковки и упаковки PAK (Peace Elite) и распаковки и упаковки OBB (PUBG Mobile).\n\nКак начать использовать:\n1. Перетащите OBB или PAK файлы в соответствующие директории.\n2. Используйте выбранное меню для взаимодействия с файлами.\n3. Папка OutPut будет содержать распакованные файлы.\n4. Все готово! Инструмент готов к использованию!\nchannel: @kejunwan\n\n", "00FFFF", "0000FF"))

        elif choice == '0':
            print(gradient_text("Выход...", "FF0000", "FFFFFF"))
            break

        else:
            print(gradient_text("Недействительный выбор. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))

if __name__ == "__main__":
    main()