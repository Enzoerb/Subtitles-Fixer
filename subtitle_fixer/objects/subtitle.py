from datetime import datetime

class SubtitleItem:

    def __init__(self, index=None, begining_time=None, end_time=None, text="", color="#FFFFFF"):
        self.index = index
        self.begining_time = None
        self.end_time = None
        self.color = color
        self.text = text


        if type(begining_time) == type(datetime(1, 1, 1)):
            self.begining_time = begining_time
        else:
            try:
                self.begining_time = datetime.strptime(begining_time, '%H:%M:%S,%f')
            except (ValueError, TypeError) as e:
                if isinstance(e, ValueError):
                    raise ValueError(f"begining_time '{begining_time}' does not match format '%H:%M:%S,%f'")
                elif isinstance(e, TypeError):
                    raise TypeError(f"begining_time must be {str(type(datetime(1, 1, 1)))[8:-2]} or {str(type(str()))[8:-2]}, not {str(type(begining_time))[8:-2]}")
                else:
                    raise e

        if type(end_time) == type(datetime(1, 1, 1)):
            self.end_time = end_time
        else:
            try:
                self.end_time = datetime.strptime(end_time, '%H:%M:%S,%f')
            except (ValueError, TypeError) as e:
                if isinstance(e, ValueError):
                    raise ValueError(f"end_time '{end_time}' does not match format '%H:%M:%S,%f'")
                elif isinstance(e, TypeError):
                    raise TypeError(f"end_time must be {str(type(datetime(1, 1, 1)))[8:-2]} or {str(type(str()))[8:-2]}, not {str(type(end_time))[8:-2]}")
                else:
                    raise e

    def __repr__(self):
        text_without_linebreak = self.text.replace('\n', ' \\n ')
        begining_time = datetime.strftime(self.begining_time, '%H:%M:%S,%f')
        end_time = datetime.strftime(self.end_time, '%H:%M:%S,%f')
        return f"SubtitleItem({self.index}, {begining_time[:-3]}, {end_time[:-3]}, {text_without_linebreak}, {self.color})"

    def __str__(self):
        begining_time = datetime.strftime(self.begining_time, '%H:%M:%S,%f')
        end_time = datetime.strftime(self.end_time, '%H:%M:%S,%f')
        item = f"{self.index}\n{begining_time[:-3]} --> {end_time[:-3]}\n<font color={self.color}>{self.text}</font>\n"
        return item
