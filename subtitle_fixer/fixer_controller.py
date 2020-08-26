from fixer_mounter import FixerMounter


class FixerController:

    @classmethod
    def fix_subtitle(cls, subtitle, add_or_remove, seconds, color):
            return FixerMounter.fix_subtitle(subtitle, add_or_remove, seconds, color)



if __name__ == '__main__':
    pass
