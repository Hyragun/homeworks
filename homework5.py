import colorama
from colorama import Fore, Back, Style

colorama.init()

print(Fore.GREEN + "Колірний текст")
print(Back.YELLOW + "Фоновий колір")
print(Style.RESET_ALL + "Скидання стилю")

#    colorama.init()     Запустити бібліотеку 
#    colorama.deinit()   Вимкнути бібліотеку
#    colorama.reinit()   Перезапустити бібліотеку