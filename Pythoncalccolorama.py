# калькулятор by ilnaz/G

from colorama import init
from colorama import Fore, Back, Style

init()

print( Fore.WHITE )
print( Back.GREEN )

what = input( "Что делаем? (+, /, *, -): " )

print( Back.CYAN )

a = float( input("Введи первое число: ") )
b = float( input("Введи второе число: ") )

print( Back.BLUE )

if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
	c = a - b
	print("Результат: " + str(c))
elif what == "*":
	c = a * b
	print("Результат: " + str(c))
elif what == "/":
	c = a / b
	print("Результат: " + str(c))
else:
	print("Выбрана неправильная операция!")

input()
