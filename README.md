# DesktopEntry-Maker

![GitHub stars](https://img.shields.io/github/stars/Wilfried-Tech/DesktopEntry-Maker.svg?style=social)
![GitHub forks](https://img.shields.io/github/forks/Wilfried-Tech/DesktopEntry-Maker.svg?style=social)

```bash
    desktop-entry-maker --help
```

```
usage: desktop-entry-maker [-h] [-a] [-u] {create} ...

Create .desktop file easily from comment line

positional arguments:
  {create}

options:
  -h, --help  show this help message and exit
  -a, --all   install for all user (Require root access)
  -u, --user  install for the current user

Made with ♥ by Wilfried-Tech.
               
```


```bash
    desktop-entry-maker create --help
```

```
usage: desktop-entry-maker create [-h] [-n NAME] [-t {Application,Link,Directory}] [-v VERSION] [-c COMMENT] [-e EXEC] [-i ICON] [-p PATH] [-s dir] [-d]
                                  [-f filename]

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Display name of launcher
  -t {Application,Link,Directory}, --type {Application,Link,Directory}
                        Type of desktop entry
  -v VERSION, --version VERSION
                        Desktop entry version
  -c COMMENT, --comment COMMENT
                        Desktop Entry comment (showed on tooltip)
  -e EXEC, --exec EXEC  executable file
  -i ICON, --icon ICON  Displayed icon file
  -p PATH, --path PATH  executable working dir
  -s dir, --save dir    save file into dir
  -d, --terminal        start in terminal
  -f filename, --filename filename   
                        save filename without extension
```