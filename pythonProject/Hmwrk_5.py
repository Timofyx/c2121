from colorama import Fore, Style
import colorama

print(dir(colorama))

print(Fore.BLUE + 'Fore.(якийсь колір) міняє колір тексту, стиль') # Fore.(якийсь коліо) міняє колір тексту, стиль
print(Fore.BLUE + 'Також Fore має не всі кольори')
print("якщо стиль був ізминеним він залишаеться") # якщо стиль був ізминеним він залишаеться
print(Style.RESET_ALL + 'Style.RESET_ALL убирає стиль, зміняє колір тексту до нормального') # убирає стиль, зміняє колір тексту до нормального
print(Style.NORMAL + "Style.Normal Робить стиль який стоїть наскільки розумію стандартним")
print(Style.BRIGHT + "Style.BRIGHT робить текст жирним")
