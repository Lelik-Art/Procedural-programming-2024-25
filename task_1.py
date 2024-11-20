"""
Вам поставлена задача реализовать функцию, которая прочитает JSON файл и найдет сумму произведений двух значений в каждом словаре.
Значения для умножения находятся по ключам "score" и "weight".
Вам нужно вычислить произведение "score" * "weight" в каждом словаре и найти сумму этих произведений.

Функция должна вернуть значение с плавающей запятой, округленное до 3 знаков после запятой. В ответе распечатайте полученную сумму.
"""

import json


def calculations(file):
    with open(file, 'r') as file:
        json_list = json.load(file)

    result_list = []

    for i in range(len(json_list)):
        dics = json_list[i]  # разделяем список на словари
        score = dics["score"]
        weight = dics["weight"]
        result = score * weight
        result_list.append(result)

    return (round(sum(result_list), 3))


print(calculations("input.json"))
