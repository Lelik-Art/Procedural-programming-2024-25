"""
Вы работаете в компании, которая разрабатывает программное обеспечение для управления запасами на складе.
Вашей задачей является написать функцию для поиска индекса первого вхождения элемента в списке товаров.
"""
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def find_index(request):
    for i in range(len(items_list)):
        if request is items_list[i]:
            return i

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index('банан')  
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
        break
    else:
        print(f"Товар не найден в списке.")
        break
