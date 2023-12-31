# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  
    
# 1.    
d = ['а', 'ы', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и']

text = input("Введите стих: ") # Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами.
list_of_words = text.split()

list_result = []
for i in range(len(list_of_words)):
    list_result.append(0)
    for j in d:
        list_result[i] += list_of_words[i].count(j)

print("Количество гласных в словах:", list_result)

def find_vowels(characteristic, objects):
    for i in range(len(list_result) - 1):
        if(list_result[i]) !=(list_result[i + 1]):
            return False
    return True

print("Парам пам-пам") if find_vowels(list_result, list_of_words) else print("Пам парам")