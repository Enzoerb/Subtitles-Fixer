from datetime import datetime
from datetime import timedelta
from objects.subtitle import SubtitleItem
import re

class FixerFunctions:

    @classmethod
    def regex(cls, pattern, text, group):
        re_pattern = re.compile(pattern)
        query = re_pattern.search(text)
        result = query.group(group)
        return result

    @classmethod
    def create_subtitle(cls, subtitle_block):
        index = subtitle_block[0]
        time = subtitle_block[1].split('-->')
        begining_time = time[0].strip()
        end_time = time[-1].strip()
        raw_text = subtitle_block[2:]

        if '<font' in raw_text[0]:
            if len(raw_text) > 1:
                first_line = FixerFunctions.regex(r"(<font color=#[\w\W]{6}>)([\w\W]*)", raw_text[0], 2)
                last_line = FixerFunctions.regex(r"([\w\W]*)(</font>)", raw_text[-1], 1)

                raw_text[0] = first_line
                raw_text[-1] = last_line

            elif len(raw_text) == 1:
                first_line = FixerFunctions.regex(r"(<font color=#[\w\W]{6}>)([\w\W]*)(</font>)", raw_text[0], 2)
                raw_text[0] = first_line

        text = '\n'.join(raw_text)
        block = SubtitleItem(index=index,
                             begining_time=begining_time, end_time=end_time,
                             text=text)

        return block

    @classmethod
    def update_seconds(cls, block: SubtitleItem, add_or_remove, seconds):
        difference = timedelta(seconds=seconds)
        if add_or_remove == "+":
            block.begining_time += difference
            block.end_time += difference
        elif add_or_remove == "-":
            begining_time_seconds = (block.begining_time - datetime(year=1900, month=1, day=1)).total_seconds()
            end_time_seconds = (block.end_time - datetime(year=1900, month=1, day=1)).total_seconds()
            block.begining_time = block.begining_time - difference if begining_time_seconds > seconds\
                                  else datetime.strptime('00:00:00,000000', '%H:%M:%S,%f')
            block.end_time = block.end_time - difference if end_time_seconds > seconds\
                                  else datetime.strptime('00:00:00,000000', '%H:%M:%S,%f')
        else:
            raise TypeError(f"add_or_remove must be '+' or '-' in str format, not {add_or_remove}: {str(type(add_or_remove))[8:-2]}")
        return block

    @classmethod
    def update_color(cls, block: SubtitleItem, color):
        block.color = color
        return block



if __name__ == '__main__':
    print(datetime(year=1900, month=1, day=1))
