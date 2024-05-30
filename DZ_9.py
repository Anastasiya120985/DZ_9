# Необходимо отсортировать первые две трети списка в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть. Остальную часть списка не сортировать, а расположить
# в обратном порядке.

a = [5, 9, 6, -5, 3, -7, 0, 8, 1]
summ = 0
for i in a:
    summ = summ + i
arith_mean = summ/len(a)
if arith_mean > 0:
    b = sorted(a[:(len(a)//3)*2]) + sorted(a[len(a)//3*2:], reverse = True)
else:
    b = sorted(a[:len(a)//3]) + sorted(a[len(a)//3:], reverse = True)
print(b)

# Написать программу «успеваемость». Пользователь вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
# меню для пользователя:
# ■ Вывод оценок (вывод содержимого списка);
# ■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
# ■ Выходит ли стипендия (стипендия выходит, если средний бал не ниже 10.7);
# ■ Вывод отсортированного списка оценок: по возрастанию или убыванию.
def output_ratings(ratings):
    result = 'Оценки: ' + ', '.join(str(i) for i in ratings)
    return result

def retake_exam(ratings, num_element, estimate):
    ratings[num_element] = estimate

def scholarship(ratings):
    summ = 0
    for i in ratings:
        summ += i
    if summ/len(ratings) >= 10.7:
        result = f'По результатам оценок будет степендия!'
    else:
        result = f'По результатам оценок не будет степендии! Средний балл - {round(summ/len(ratings), 1)}'
    return result

def sort(ratings):
    answer = input('Сортировать оценки по возрастанию или убыванию? (в/у) ')
    if answer == 'в':
        result = sorted(ratings, reverse=False)
        result = output_ratings(result)
        return result
    elif answer == 'у':
        result = sorted(ratings, reverse=True)
        result = output_ratings(result)
        return result
    else:
        print('Введено некорректное значение!')

if __name__ == '__main__':
    ratings = list(map(int, input('Введите 10 оценок через пробел (оценки от 1 до 12): ').split()))
    while True:
        print('1. Вывод оценок')
        print('2. Пересдача экзамена')
        print('3. Выходит ли стипендия')
        print('4. Вывод отсортированного списка оценок: по возрастанию или убыванию.')
        print('5. Выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            print(f'{output_ratings(ratings)} \n')
        elif choice == '2':
            num_element = int(input('Введите номер оценки в списке для пересдачи: ')) - 1
            if 0 <= num_element <= len(ratings):
                estimate = int(input('Введите новую оценку после пересдачи: '))
                retake_exam(ratings, num_element, estimate)
                print(f'{output_ratings(ratings)} \n')
            else:
                print('Указан неверный номер элемента в списке оценок!')
        elif choice == '3':
            print(f'{scholarship(ratings)} \n')
        elif choice == '4':
            print(f'{sort(ratings)} \n')
        elif choice == '5':
            break
        else:
            print('Неверный пункт меню')

# Написать программу, реализующую сортировку списка методом усовершенствованной сортировки пузырьковым
# методом. Усовершенствование состоит в том, чтобы анализировать количество перестановок на каждом шагу, если
# это количество равно нулю, то продолжать сортировку нет смысла — список отсортирован.

def buble_sort(lst):
    n = 0
    for i in range(len(lst)-1):
        for j in range(len(lst) - (i+1)):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                n += 1
        if n == 0:
            break
    return lst

lst = [5, 2, 8, 5, 4, 9, 5, 3]
print(buble_sort(lst))