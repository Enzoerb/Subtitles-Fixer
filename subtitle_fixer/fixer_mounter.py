from fixer_functions import FixerFunctions


class FixerMounter:

    @classmethod
    def fix_subtitle(cls, subtitle, add_or_remove, seconds, color):
        treated_subtitle_list = [item.replace('\n', '') for item in subtitle]

        subtitle_in_blocks = list()
        for item in treated_subtitle_list:
            if item:
                if item.isnumeric():
                    subtitle_in_blocks.append([])
                subtitle_in_blocks[len(subtitle_in_blocks)-1].append(item)

        new_subtitle_list = [FixerFunctions.create_subtitle(block) for block in subtitle_in_blocks]
        new_subtitle_color = [FixerFunctions.update_color(block, color) for block in new_subtitle_list]
        ready_new_subtitle = [FixerFunctions.update_seconds(block, add_or_remove, seconds)
                              for block in new_subtitle_color]
        string_subtitle = "\n".join([str(block) for block in ready_new_subtitle])
        return string_subtitle



if __name__ == '__main__':
    pass
