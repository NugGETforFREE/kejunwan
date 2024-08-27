
import os
import subprocess
from colorama import Fore, Style

def print_menu():
    print(Fore.CYAN + "\n\n1) Unpack PAK/解压缩pak文件")
    print(Fore.YELLOW + "2) Repack PAK/打包pak文件")
    print(Fore.MAGENTA + "3) HELP/帮助")
    print(Fore.RED + "4) EXIT/出去" + Style.RESET_ALL)

def list_files(folder_path):
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    except Exception as e:
        print(Fore.RED + f"\n访问文件夹时出错： {e}" + Style.RESET_ALL)
        return []

    if not files:
        print(Fore.RED + "\n没有可用的文件！" + Style.RESET_ALL)
    return files

def select_file(files, prompt):
    if not files:
        return None

    print(Fore.GREEN + prompt + Style.RESET_ALL)
    for index, file in enumerate(files, start=1):
        print(Fore.WHITE + f"{index}) {file}" + Style.RESET_ALL)

    print(Fore.RED + "\n0) 输出" + Style.RESET_ALL)

    while True:
        try:
            choice = input(Fore.CYAN + "\n输入文件编号 (0 — 输出): " + Style.RESET_ALL)
            if choice == '0':
                return None
            choice = int(choice)
            if 1 <= choice <= len(files):
                return files[choice - 1]
            else:
                print(Fore.RED + "\n选择错误！请重试。" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "\n输入无效！请输入一个数字。" + Style.RESET_ALL)

def unpack_pak():
    folder_path = "/storage/emulated/0/Download/for_pak/"
    if not os.path.exists(folder_path):
        print(Fore.RED + "\n未找到 for_pak 文件夹" + Style.RESET_ALL)
        return

    files = list_files(folder_path)
    selected_file = select_file(files, "\n选择要解压的文件:")

    if selected_file is None:
        print(Fore.YELLOW + "\n退出 Repacker GameForPeace (@kejunwan)." + Style.RESET_ALL)
        return

    full_path = os.path.join(folder_path, selected_file)
    command = f"qemu-i386 quickbms chinaNB.bms {full_path} /storage/emulated/0/Download/for_pak/output/"

    try:
        subprocess.run(command, shell=True, check=True)
        print(Fore.GREEN + "\n成功" + Style.RESET_ALL)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"\n执行命令时出错: {e}" + Style.RESET_ALL)

def repack_pak():
    folder_path = "/storage/emulated/0/Download/for_pak/"
    repack_path = os.path.join("/storage/emulated/0/Download/for_pak/repack/")

    if not os.path.exists(folder_path):
        print(Fore.RED + "\n未找到 for_pak 文件夹" + Style.RESET_ALL)
        return

    files_for_pak = list_files(folder_path)
    selected_file_for_pak = select_file(files_for_pak, "\n选择要重打包的文件:")

    if selected_file_for_pak is None:
        print(Fore.YELLOW + "\n退出 Repacker GameForPeace (@kejunwan)" + Style.RESET_ALL)
        return

    full_path_for_pak = os.path.join(folder_path, selected_file_for_pak)
    
    command = f"qemu-i386 quickbms -w -g -r -r chinaNB.bms {full_path_for_pak} /storage/emulated/0/Download/for_pak/repack/"

    try:
        subprocess.run(command, shell=True, check=True)
        print(Fore.GREEN + "\n重打包成功" + Style.RESET_ALL)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"\n执行命令时出错: {e}" + Style.RESET_ALL)

def help_info():
    print(Fore.RED + "\n帮助信息：" + Style.RESET_ALL)
    print(Fore.GREEN + "\n这是一个用于解压缩 <Game For Peace> 游戏中 pak 文件的工具\n"
          "\n在开始使用此工具之前\n"
          "\n1. 您需要在 \"/Download/\" 文件夹下创建一个名为 \"for_pak\" 的文件夹，在此存放 .pak 文件，以便解压\n"
          "\n2. 在 \"for_pak\" 文件夹中创建 \"repack\" 文件夹，您将在此存储用于重新导入的文件（最常见的是 .uexp）。\n"
          "\n3. 就是这样！工具就可以使用了。\n"
          "Telegram：@kejunwan")


def main():
    while True:
        print_menu()
        choice = input(Fore.CYAN + "\n选择一个选项：" + Style.RESET_ALL)
        if choice == '1':
            unpack_pak()
        elif choice == '2':
            repack_pak()
        elif choice == '3':
            help_info()
        elif choice == '4':
            print(Fore.GREEN + "\n退出程序" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\n选择错误。 请重试。" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
