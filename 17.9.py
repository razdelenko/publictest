nums = input('Введите целые числа через пробел: ')
user_num = int(input('Введите любое число: '))

# Определяем цифру в строке
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

# Проверяем на правильность ввода
if " " not in nums:
    nums = input('Введите целые числа ЧЕРЕЗ ПРОБЕЛ: ')
if not is_int(nums):
    print('Введите ТОЛЬКО целые числа')
else:
    nums = nums.split()

list_nums = [int(item) for item in nums]

# Сортируем список
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_nums = merge_sort(list_nums)#

# Находим позицию элемента
def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за рамки списка, введите друшое число.'

# Устанавливаем номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу.
print(f'Упорядоченный по возрастанию список: {list_nums}')

if not binary_search(list_nums, user_num, 0, len(list_nums)):
    rI = min(list_nums, key=lambda x: (abs(x - user_num), x))
    ind = list_nums.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_num:
        print(f'''Число не в списке 
Ближайшее мин число: {rI}, с индексом: {ind}
Ближайшее макс число: {list_nums[max_ind]} с индексом: {max_ind}''')
    elif min_ind < 0:
        print(f'''Число не в списке
Ближайшее макс число: {rI}, с индексом: {list_nums.index(rI)}
нет числа меньше''')
    elif rI > user_num:
        print(f'''Число не в списке
Ближайшее макс число: {rI}, с индексом: {list_nums.index(rI)}
Ближайшее мин число: {list_nums[min_ind]} с индексом: {min_ind}''')
    elif list_nums.index(rI) == 0:
        print(f'Индекс введенного числа: {list_nums.index(rI)}')
else:
    print(f'Индекс введенного числа: {binary_search(list_nums, user_num, 0, len(list_nums))}')