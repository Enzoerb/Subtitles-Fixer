from fixer_controller import FixerController
from os import path, getcwd

def get_path(message='Enter a path', check_exists=False, check_srt=False):
    subtitle_path = input(message)
    subtitle_path = path.join(getcwd(), subtitle_path) if subtitle_path[0] != '/' else subtitle_path
    if check_exists:
        while not path.exists(subtitle_path):
            print('Wrong Input')
            subtitle_path = input(message)
    if check_srt:
        if path.splitext(subtitle_path)[1] != '.srt':
            subtitle_path += '.srt'
    return subtitle_path

def get_add_or_remove(message):
    add_or_remove = input(message)
    while add_or_remove not in ["+", "-"]:
        print('Wrong Input')
        add_or_remove = input(message)
    return add_or_remove

def fix_subtitle(subtitle_path, new_subtitle_path, add_or_remove, seconds, color):

    with open(subtitle_path, 'r', encoding="ISO-8859-1") as raw_subtitle:
        subtitle = raw_subtitle.readlines()
    new_subtitle = FixerController.fix_subtitle(subtitle, add_or_remove, seconds, color)
    with open(new_subtitle_path, 'w') as srt_subtitle:
        srt_subtitle.write(new_subtitle)

if __name__ == '__main__':
    subtitle_path = get_path('\nEnter Subtitle Path: ', check_exists=True)
    new_subtitle_path = get_path('\nEnter New Subtitle Path: ', check_srt=True)
    add_or_remove = get_add_or_remove('\nEnter "+" to add seconds and "-" to remove: ')
    seconds = int(input("\nEnter how many seconds do you want to change: "))
    color = input('\n(#FFFFFF = white, #FFFF00 = yellow)\nEnter Color Hex: ')
    print()
    print('---------------------------------------')
    print('---------Creating-New-Subtitle---------')
    print('---------------------------------------')
    fix_subtitle(subtitle_path, new_subtitle_path, add_or_remove, seconds, color)

    from datetime import datetime
