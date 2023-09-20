import math
from math import factorial
def f(val):
    if val is None:
        return False
    try:
        float(val)
        return True
    except ValueError:
        return False
a = 0
while True:
      print("Выберите операцию:"
            "\n 1. Сложение"
            "\n 2. Вычитание"
            "\n 3. Умножение"
            "\n 4. Деление"
            "\n 5. Возведение в степень"
            "\n 6. Квадратный корень"
            "\n 7. Факториал"
            "\n 8. Синус"
            "\n 9. Косинус"
            "\n 10. Тангенс"
            "\n 11. Завершить программу")
      a = input()
      if a == "11":
            break
      elif a in ("1","2", "3", "4", "5", "6", "7", "8", "9", "10"):
            print("Введите первое число:")
            x = input()
            print("Введите второе число:")
            y = input()
      else:
            print("Введите число, соответсвутющее номеру операции")
      match a:
            case '1':
                  if f(x) == True and f(y) == True:
                        x = float(x)
                        y = float(y)
                        print(x + y)
                  else:
                        print("Напишите числа")
            case '2':
                  if f(x) == True and f(y) == True:
                        x = float(x)
                        y = float(y)
                        print(x - y)
                  else:
                        print("Напишите числа")
            case '3':
                  if f(x) == True and f(y) == True:
                        x = float(x)
                        y = float(y)
                        print(x * y)
                  else:
                        print("Напишите числа")
            case '4':
                  if f(x) == True and f(y) == True:
                        x = float(x)
                        y = float(y)
                  if y != 0:
                        print(x / y)
                  else:
                        print("Делить на 0 нельзя!!!")
                  if f(x) == False or f(y) == False:
                        print("Напишите числа")
            case '5':
                  if f(x) == True and f(y) == True:
                        x = float(x)
                        y = float(y)
                        print(x ** y)
                  else:
                        print("Напишите числа")
            case '6':
                  if f(x) == True and f(y) == True:
                        x = float(x)
                        if x < 0:
                              print("Отрицательного корня нет!")
                        else:
                              print(math.sqrt(x))
                  if f(x) == False or f(y) == False:
                        print("Напишите числа")
            case '7':
                  if f(x) == True and f(y) == True:
                        x = int(x)
                  if x < 0:
                        print("Нет отрицательного факториала!")
                  elif x >= 0:
                        print(factorial(x))
                  elif f(x) == False or f(y) == False:
                        print("Напишите числа")
            case '8':
                  if f(x) == True and f(y) == True:
                        x = float(x)
                        y = float(y)
                        print(math.sin(x))
                  else:
                        print("Напишите числа")
            case '9':
                  if f(x) == True and f(y) == True:
                        x = float(x)
                        y = float(y)
                        print(math.cos(x))
                  else:
                        print("Напишите числа")
            case '10':
                  if f(x) == True and f(y) == True:
                        x = float(x)
                        y = float(y)
                        print(math.tan(x))
                  else:
                        print("Напишите числа")