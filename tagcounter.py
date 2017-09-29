import sys

import gui_app
import main_facade

main = main_facade.MainFacade()

if (len(sys.argv) < 3):
    gui_app.launch(main)
    exit()

import pprint

pp = pprint.PrettyPrinter(indent=4)
console_command = sys.argv[1]
console_url_or_synonym = sys.argv[2]
if console_command == "--get":
    command_result = main.get_command(console_url_or_synonym)
    pp.pprint(command_result)
elif console_command == "--view":
    command_result = main.view_command(console_url_or_synonym)
    pp.pprint(command_result)
else:
    msg = """
    possible command:
    tagcounter --get http:\\google.com
    tagcounter --get ggl

    tagcounter --view ggl
    tagcounter --view http:\\google.com

    tagcounter
    """
    print(msg)
