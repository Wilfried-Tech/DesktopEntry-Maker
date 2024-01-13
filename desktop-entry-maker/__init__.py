#!/bin/env python3
import os

from ._core import create_desktop_file, empty


def run_console():
    import argparse

    parser = argparse.ArgumentParser(prog="desktop-entry-maker",
                                     epilog="""
    Made with ♥ by Wilfried-Tech.
""""",
                                     description="""
     Create .desktop file easily from comment line 
    """)

    parser.add_argument("-a", "--all", action="store_true", help="install for all user (Require root access)")
    parser.add_argument("-u", "--user", action="store_true", help="install for the current user")

    command = parser.add_subparsers(dest="command")

    create_parser = command.add_parser("create", description="create new .desktop file")
    create_parser.add_argument("-n", "--name", default="", help="Display name of launcher")
    create_parser.add_argument("-t", "--type", choices=["Application", "Link", "Directory"],
                               default="Application", help="Type of desktop entry")
    create_parser.add_argument("-v", "--version", type=float, default=1.0, help="Desktop entry version")
    create_parser.add_argument("-c", "--comment", default="", help="Desktop Entry comment (showed on tooltip)")
    create_parser.add_argument("-e", "--exec", default="", help="executable file")
    create_parser.add_argument("-i", "--icon", default="", help="Displayed icon file")
    create_parser.add_argument("-p", "--path", default="", help="executable working dir")
    create_parser.add_argument("-s", "--save", default=os.curdir, metavar="dir", help="save file into dir")
    create_parser.add_argument("-d", "--terminal", action="store_true", help="start in terminal")
    create_parser.add_argument("-f", "--filename", default="", dest="filename", metavar="filename",
                               help="save filename without extension")

    args = parser.parse_args()

    if args.command == "create":
        if empty(args.name):
            args.name = input("? Desktop Entry name: ")
        if empty(args.exec):
            args.exec = input("? Desktop Entry Executable: ")
        if empty(args.icon):
            args.icon = input("? Desktop Entry Icon: ")

        create_desktop_file(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    run_console()
