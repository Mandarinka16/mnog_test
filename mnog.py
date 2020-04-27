#сегодня мы с вами попробуем выступить в роли детектива
# у нас есть множество людей, которые пользуется машиной той же марки, которую пользуется убийца
# есть множество людей, которые живут недалеко от мест преступления
# и множество людей, у которых и работа недалеко от мест преступления

#имена обычно значения неуникальные, но предплоложим, это были бы номер соц страховок
shevrole_owner = {'sam', 'edit', 'semen', 'petr'}

work_near = {'konstantin', 'vladislav', 'sam', 'petr', 'edit'}

live_near = {'john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo'}

#  д/з объединить множество людей, которые живут и работают рядом
# вывести множество людей, которые и владеют авто нужной марки, и живут и работают рядом

print("*****   Результаты расследования:   *****")
print("Люди, которые живут и работают рядом с местом преступления: ")
live_work = work_near & live_near
if len(live_work) == 0:
    print("  Таких нет")
for chel in live_work:
    print("- ", chel)

print("Люди, которые владеют авто шевроле, при этом живут и работают рядом: ")
live_work_auto = work_near & live_near & shevrole_owner
if len(live_work_auto) == 0:
    print("  Таких нет")
for chel in live_work_auto:
    print("- ", chel)

print("Люди, которые владеют авто шевроле, при этом живут рядом: ")
live_auto = live_near & shevrole_owner
if len(live_auto) == 0:
    print("  Таких нет")
for chel in live_auto:
    print("- ", chel)

print("Люди, которые владеют авто шевроле, при этом работают рядом: ")
work_auto = work_near & shevrole_owner
if len(work_auto) == 0:
    print("  Таких нет")
for chel in work_auto:
    print("- ", chel)