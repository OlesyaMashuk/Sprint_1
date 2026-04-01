time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
# объявляем общее кол-во минут
total_minutes = 0

#разбиваем строку на отдельные пять блоков
blocks = time_string.split(',')

#цикл для обработки каждого блока, заменяем пробелы на запятые
for block in blocks:
    normalized_block = block.replace(' ', ',')
 
    #разбиваем на отдельные единицы времени
    units  = normalized_block.split(',')

    #проходим по каждому значению
    for unit in units:

    #берем число часов и переводим в минуты
        if 'h' in unit:
            hours = int(unit.replace('h', ''))
            total_minutes += hours * 60

        #берем число минут и добавляем к общему кол-ву
        elif 'm' in unit:
            minutes = int(unit.replace('m', ''))
            total_minutes += minutes

        #берем число секунд и переводим в минуты
        elif 's' in unit:
            seconds = int(unit.replace('s', ''))
            total_minutes += seconds // 60

#выводим переменную на экран
print(f"Общее количество в минутах составило: {total_minutes}")
