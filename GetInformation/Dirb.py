import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI

import dirb_help


def mydirb():
    commands = ["back", "how to use dirb", "dirb"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32mdirb > \033[0m')
    while True:
        choice = prompt(formatted_text1, completer=completer)
        if choice == 'back':
            break
        elif choice == "":
            continue
        elif choice == 'how to use dirb':
            dirb_help.help()
            continue
        os.system(choice)
        continue
