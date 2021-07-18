# MIT License
#
# Copyright (c) 2021 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#
# p - 'who'-like tool, yeah colorful (executable, maybe a bit library)
#
# github.com/ferhatgec/p
# github.com/ferhatgec/f (c++)

class p:
    @staticmethod
    def get_time() -> (int, int, int):
        from pathlib import Path
        days, hours, minutes = 0, 0, 0

        if Path('/proc/uptime').exists():
            s = 0
            with open('/proc/uptime', 'r') as file:
                s = int(float(file.readline().split()[0]))

            days = (int(s / 60 / 60 / 24) ^ 0) if (s / 60 / 60 / 24) else 0
            hours = (int(s / 60 / 60 % 24) ^ 0) if (s / 60 / 60 % 24) else 0
            minutes = (int(s / 60 % 60) ^ 0) if (s / 60 % 24) else 0

        return days, hours, minutes

    @staticmethod
    def process(days, hours, minutes):
        d = f'\x1b[1;93m{days}\x1b[0;97md\x1b[0;97m, ' if days != 0 else ''
        h = f'\x1b[1;94m{hours}\x1b[0;97mh\x1b[0;97m, ' if hours != 0 else ''
        m = f'\x1b[1;95m{minutes}\x1b[0;97mm' if minutes != 0 else ''

        return d + h + m

    @staticmethod
    def init(days, hours, minutes):
        from os import getenv, ttyname
        from sys import stdin

        data = getenv('USER')
        lang = getenv('LANG')
        disp = getenv('DISPLAY')
        term = getenv('TERM')
        desk = getenv('DESKTOP_SESSION')
        tty = ttyname(stdin.fileno())
        upt = p.process(days, hours, minutes)

        if len(data) != 0:
            print(end=f'\x1b[1;94m{data}\x1b[0m')

        if len(tty) != 0:
            print(end=f'\x1b[0;97m -> \x1b[1;91m:{tty[-1]} ')

        if len(disp) != 0:
            print(end=f'\x1b[0;97md(\x1b[0;95m{disp}\x1b[0;97m) ')

        if len(lang) == 0:
            lang == getenv('LANGUAGE')

        print(end=f'l(\x1b[1;97m{lang}\x1b[0;97m) ')

        print(end=f'u({upt})\x1b[0;97m)')

        if len(term) != 0:
            print(end=f' \x1b[1;93m{term}\x1b[0;97m ')

        if len(desk) != 0:
            print(f' d(\x1b[1;90m{desk}\x1b[0;97m)')


d, h, m = p.get_time()
p.init(d, h, m)
