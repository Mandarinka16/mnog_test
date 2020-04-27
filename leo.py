import random

print(" Сейчас можно будете ввести слова в наш словарь")
print("Если хотите остановить ввод слов, напишите q на английском")

slovar = {}

while True:
    key = input("Введите слово на английском\n:").lower().strip()
    if key == 'q':
        break
    value = input("Введите перевод на русском\n:").lower().strip()
    slovar[key] = value

print(slovar)
print("Пора потренироваться, ошибок у нас не более 3")

errors = 0
bonus = 0

random_words = []
for key in slovar.keys():
    random_words.append(key)
print(random_words)
random.shuffle(random_words)

for key in random_words:
    print('Введите значение слова: ' + key)
    answer = input("Вы считаете, что это слово переводится как\n :").lower().strip()
    if slovar[key] == answer:
        bonus += 1
        print("Отлично! Ваш счет составляет: ", bonus)
    elif errors > 3:
        print("Game over")
        break
    else:
        errors += 1
        print('Количество ошибок', errors)