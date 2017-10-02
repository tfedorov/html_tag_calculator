import sys

import gui_app
import tags_extractor.main_facade as main

# main - All logic object not depends from gui/console interface
main = main.MainFacade()

if (len(sys.argv) < 3):
    # gui command version
    gui_app.launch(main)
    exit()

console_command = sys.argv[1]
console_url_or_synonym = sys.argv[2]
if console_command == "--get":
    print("You launch console command get for " + console_url_or_synonym)
    print(main.get_command(console_url_or_synonym))
elif console_command == "--view":
    print("You launch console command view for " + console_url_or_synonym)
    command_result = main.view_command(console_url_or_synonym)
    print(command_result)
else:
    # if app does not know how to handle
    msg = """
    possible command:
    tagcounter --get http:\\google.com
    tagcounter --get ggl

    tagcounter --view ggl
    tagcounter --view http:\\google.com

    tagcounter
    """
    print(msg)
