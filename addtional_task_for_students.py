# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(l: list, item):
    result = {}
    n = 0

    for el in l:
        if item == el:
            n += 1
    
    return n
    
test_list = [1, 1, 2, 5, 6, "яблоко", "яблоко"]
res = my_count(test_list, 1)

print(f"Заданное значение входит в список {res} раз(a)")
