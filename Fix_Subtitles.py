#Fix Subtitles

# Asking for the essential inputs
subtitle = input('Subtitle:\n')

first = input('First Part(number): ')
while first.isnumeric() == False:
    first = input('First Part(number): ')
first = int(first)

last = input('Last Part(number): ')
while last.isnumeric() == False:
    last = input('Last Part(number): ')
last = int(last)

color = input('Yellow or White Subtitles? [\033[33mY\033[m/\033[37mW\033[m]\n').upper()
while 'Y' != color != 'W':
    print('\n\033[31mtype a valid color\033[m("\033[33mY\033[m" for Yellow and "\033[37mW\033[m" for White)\033[m')
    color = input('Yellow or White Subtitles? [\033[33mY\033[m/\033[37mW\033[m]\n').upper()
    
choice = input('Add or Remove Seconds? [\033[36m+\033[m/\033[31m-\033[m]\n')
while '+' != choice != '-':
    print('\n\033[31mtype a valid choice\033[m("\033[36m+\033[m" to Add and "\033[31m-\033[m" to Remove)')
    choice = input('Add or Remove Seconds? [\033[36m+\033[m/\033[31m-\033[m]\n')
if choice == '-':
    seconds_to_edit = 0 - int(input('Seconds to Remove: '))
elif choice == '+':
    seconds_to_edit = int(input('Seconds to Add: '))
    
index_choice = input(f'''type "1" to substitute in place ({first} --> {last})
type "2" to create a new subtitle indexed from 1 to {last - first + 1}
''')
while '1' != index_choice != '2':
    print('\n\033[31mtype a valid choice\033[m')
    index_choice = input(f'''type "1" to substitute in place ({first} --> {last})
type "2" to create a new subtitle indexed from 1 to {last - first + 1}
''')
    
# Preprocessing Subtitle
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
    if lst[-1] != '':
        lst.append('')

if index_choice == '2':
    del block[last:]
    del block[:first - 1]
    rng = [c for c in range(1, len(block) + 1)]
else:
    rng = [c for c in range(first, last + 1)]

# Fixing Subtitle
count = 0
fixed_subtitle = ''
for lst in block:
    # Adding New Index
    count += 1
    lst[0] = str(count)
    if count in rng:
        # Adding or Removing Seconds
        time_i, arrow, time_f = lst[1].split(sep = ' ')
        time_i = time_i.replace(',', '.').split(sep = ':')
        time_f = time_f.replace(',', '.').split(sep = ':')
        time_i = float(time_i[0]) * 3600 + float(time_i[1]) * 60 + float(time_i[2]) + seconds_to_edit
        time_f = float(time_f[0]) * 3600 + float(time_f[1]) * 60 + float(time_f[2]) + seconds_to_edit
        # Separting back hours, minutes and seconds
        hour_i, min_i = str(int(time_i // 3600)), str(int((time_i - (time_i // 3600) * 3600) // 60))
        sec_i = f'{(time_i - int(hour_i) * 3600 - int(min_i) * 60):.3f}'
        hour_f, min_f = str(int(time_f // 3600)), str(int((time_f - (time_f // 3600) * 3600) // 60))
        sec_f = f'{(time_f - int(hour_f) * 3600 - int(min_f) * 60):.3f}'
        # Fitting time back into the right format 'hh:mm:ss,s --> hh:mm:ss,s'
        time_i = f'{hour_i if len(hour_i) > 1 else "0" + hour_i}:{min_i if len(min_i) > 1 else "0" + min_i}:{sec_i if len(sec_i) > 5 else "0" + sec_i}'.replace('.', ',')
        time_f = f'{hour_f if len(hour_f) > 1 else "0" + hour_f}:{min_f if len(min_f) > 1 else "0" + min_f}:{sec_f if len(sec_f) > 5 else "0" + sec_f}'.replace('.', ',')
        lst[1] = f'{time_i} {arrow} {time_f}'
    #Changing Colors
    lst[2] = lst[2].replace('<font color=#FFFF00>', '')
    lst[-2] = lst[-2].replace('</font>', '')
    if color == 'Y':
        lst[2] = '<font color=#FFFF00>' + lst[2]
        lst[-2] += '</font>'
    #Implementing Changes
    for i in lst:
        fixed_subtitle += i + '\n'
