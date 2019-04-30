#Fix Subtitles
first = int(input('First Part(number): '))
last = int(input('Last Part(number): '))
seconds_to_remove = int(input('Seconds to Remove: '))
subtitle = input('Subtitle:\n')

subtitle = subtitle.split(sep = '\n')
index = 0
block = [[]]
for line in subtitle:
    block[index].append(line)
    if line == '':
        block.append([])
        index += 1

for lst in block:
    if len(lst) < 3:
        block.remove(lst)

del block[last:]
del block[:first - 1]

count = 0
fixed_subtitle = ''
for lst in block:
    count += 1
    lst[0] = str(count)
    time_i, arrow, time_f = lst[1].split(sep = ' ')
    time_i = time_i.replace(',', '.').split(sep = ':')
    time_f = time_f.replace(',', '.').split(sep = ':')
    time_i = float(time_i[0]) * 3600 + float(time_i[1]) * 60 + float(time_i[2]) - seconds_to_remove
    time_f = float(time_f[0]) * 3600 + float(time_f[1]) * 60 + float(time_f[2]) - seconds_to_remove
    hour_i, min_i = str(int(time_i // 3600)), str(int((time_i - (time_i // 3600) * 3600) // 60))
    sec_i = f'{(time_i - int(hour_i) * 3600 - int(min_i) * 60):.3f}'
    hour_f, min_f = str(int(time_f // 3600)), str(int((time_f - (time_f // 3600) * 3600) // 60))
    sec_f = f'{(time_f - int(hour_f) * 3600 - int(min_f) * 60):.3f}'
    time_i = f'{hour_i if len(hour_i) > 1 else "0" + hour_i}:{min_i if len(min_i) > 1 else "0" + min_i}:{sec_i if len(sec_i) > 5 else "0" + sec_i}'.replace('.', ',')
    time_f = f'{hour_f if len(hour_f) > 1 else "0" + hour_f}:{min_f if len(min_f) > 1 else "0" + min_f}:{sec_f if len(sec_f) > 5 else "0" + sec_f}'.replace('.', ',')
    lst[1] = f'{time_i} {arrow} {time_f}'
    for i in lst:
        fixed_subtitle += i + '\n'
