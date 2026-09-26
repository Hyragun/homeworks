result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше b")
    if b > 100:
        raise IndexError("b більше 100")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 6: 15, 8: 4}


for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError as e:
        print("ValueError:", e)
    except IndexError as e:
        print("IndexError:", e)
    except ZeroDivisionError:
        print("ZeroDivisionError: ділення на нуль")
    except TypeError:
        print("TypeError: неправильний тип даних")

print("Результат:", result)