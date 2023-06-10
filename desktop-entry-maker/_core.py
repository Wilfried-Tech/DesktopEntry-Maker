import os.path
import subprocess
import tempfile
from configparser import ConfigParser
from shlex import quote


def empty(var: str):
    return var.strip() == ""


def create_desktop_file(args, gui=False):
    if empty(args.name):
        print("Desktop Entry name not specified")
        exit()
    if empty(args.filename):
        args.filename = "-".join([x.lower() for x in args.name.split()])
    if empty(args.exec) or not os.path.exists(args.exec):
        print(f"Executable {args.exec} not found")
        exit()
    if not os.path.exists(args.save):
        print(f"Save dir {args.save} not found")
        exit()

    if args.all and args.user:
        args.all = False
        create_desktop_file(args, gui)
        args.all = True
        args.user = False
        create_desktop_file(args, gui)
        exit()

    if args.all:
        args.save = "/usr/share/applications"
    elif args.user:
        args.save = os.path.expanduser("~/.local/share/applications")

    args.filename = os.path.join(os.path.abspath(args.save), args.filename) + ".desktop"
    args.exec = os.path.abspath(args.exec)

    parser = ConfigParser()
    parser.optionxform = str
    parser["Desktop Entry"] = {
        "Version": "{:.1f}".format(args.version),
        "Type": args.type,
        "Name": quote(args.name),
        "Comment": args.comment,
        "Exec": args.exec,
        "Icon": args.icon,
        "Path": args.path,
        "Terminal": str(args.terminal).lower(),
        "StartupNotify": "false"
    }
    try:
        with open(args.filename, "w") as f:
            parser.write(f, False)
    except PermissionError:
        file = os.path.join(tempfile.gettempdir(), os.path.basename(args.filename))
        with open(file, "w") as f:
            parser.write(f, False)
        command = ["pkexec" if gui else "sudo", "cp", file, args.filename]
        try:
            if subprocess.run(command).returncode != 0:
                raise KeyboardInterrupt
        except KeyboardInterrupt:
            print("Permission Denied")
