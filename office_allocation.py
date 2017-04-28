#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    Dojo create_room <input_details>...
    Dojo perform_action <input_details>
    Dojo (-i | --interactive)
    Dojo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit


from app.dojo.dojo import Dojo

dojo_instance = Dojo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'THIS IS THE DOJO' \
        + ' This application is for allocating space to the Dojo' \
        + ''\
        + ' For help, type "help" for instructions on how to start'
    prompt = '(The Dojo >>) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <input_details>... """
        room_details = arg['<input_details>']
        dojo_instance.create_room(room_details)
        print("Dojo has room(s): "+ ", ".join(str(x.name) for x in dojo_instance.allRooms) + " !operation successful\n")

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: create_room <input_details>... """
        person_details = arg['<input_details>']
        dojo_instance.add_person(person_details)
        print("Dojo has person(s): {0} !operation successful\n".format(
            ", ".join(str(x.name) for x in dojo_instance.allPeople)))

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: perform_action <input_details> """
        room_name = arg['<input_details>']
        print(dojo_instance.print_room(room_name))
        print("operation successful!\n")

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: perform_action <input_details> """
        room_name = arg['<input_details>']
        print("operation successful!\n Find file in the resources folder")




    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)