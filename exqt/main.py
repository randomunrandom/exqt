import os
import sys
import click
import json
import argparse
import subprocess
from termcolor import colored


def get_cmd_file():
    user_home = os.path.expanduser("~")
    os.chdir(user_home)
    if not (os.path.exists(".exqt.json")):
        file = open(".exqt.json", "w+")
        file.close()
    return str(os.getcwd() + "/.exqt.json")


@click.command()
@click.argument('name')
def exqt(name):
    cmd_lst = get_cmd_file()
    if cmd_lst == "":
        print("error, home dir not found")
        return
    with open(cmd_lst) as json_data:
        if json_data.readline() == "":
            print("command not found")
            print("consider using `exqt add` to add new command")
            return
        json_lst = json.load(json_data)
        print(json_lst)
        print(json_lst.keys())
        json_data.close()

    print(cmd_lst)
    print(name)

    return


def main():
    exqt()
    return
    """
    user_home = os.path.expanduser("~")

    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="exqt",
        description="cli program to save and execute difficult/long commands on demand"
    )
    parser.add_argument("command_name", help="execute command saved by given name", type=str)
    arguments = parser.parse_args(argv)
    prog_name = arguments.command_name
    if ".exqt" not in os.listdir(user_home):
        with open(f"{user_home}/.exqt", 'w', encoding='utf-8') as f:
            json.dump({
                "commands": {
                    "echo_test": {
                        "name": "echo_test",
                        "script": 'echo "hello world"'
                    },
                    "ping_google": {
                        "name": "ping_google",
                        "script": 'ping -c 5 google.com'
                    }
                }
            }, fp=f, ensure_ascii=False)

    with open(f"{user_home}/.exqt", 'r', encoding='utf-8') as f:
        commands = json.loads(f.read())

    prog_script = commands['commands'][prog_name]['script']
    print("- script:", file=fp)
    print(colored(prog_script, "green"), file=fp)
    print("- output:", file=fp)
    print(colored(subprocess.Popen(prog_script, shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8"),
                  "yellow"), file=fp)
    """
    return
