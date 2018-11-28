import os
# import sys
import json
import subprocess
import click


def get_cmd_file():
    """
    creates basic config file and returns path to it
    :return: str - path to config file
    """
    user_home = os.path.expanduser("~")
    os.chdir(user_home)
    if not (os.path.exists(".exqt.json")):
        file = open(".exqt.json", "w+")
        file.close()
    return str(os.getcwd() + "/.exqt.json")


def run_script(script):
    click.echo("script:")
    click.secho(script, fg='bright_blue')
    click.echo("result:")
    click.secho(subprocess.Popen(script, shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8"),
                fg="yellow")
    # if next=="": return
    return


@click.group()
# @click.option('--verbose', default=False)
def exqt():
    return


@exqt.command()
@click.argument('name', nargs=-1)
def run(name):
    with open(get_cmd_file(), "r", encoding="UTF-8") as json_data:
        json_lst = json.load(json_data)
        if not json_lst:
            click.secho("config file not found", fg='red')
            return
        keys_lst = json_lst["scripts"].keys()
        for i, el in enumerate(name):
            if el not in keys_lst:
                click.secho("command " + el + " not found", fg='red')
                click.secho("consider using `exqt add` to add new scripts", fg='red')
            else:
                script = json_lst["scripts"][el]["script"]
                run_script(script)
        json_data.close()
    return


@exqt.command()
# @click.argument('-N', '--name')
def add():
    with open(get_cmd_file(), "r", encoding="UTF-8") as json_data:
        json_lst = json.load(json_data)
        if not json_lst:
            click.secho("config file empty", fg='red')

        names = json_lst["scripts"].keys()
        name = str(input("name the script: "))
        while name in names:
            click.secho("this name is already taken, chose another one")
            name = str(input("name the script: "))
        script = str(input("type the script: "))
        click.secho("in which environment to run?\nchoose one of the below: ", fg="yellow")
        for i, el in enumerate(json_lst["envs"]):
            click.echo("\t" + str(i + 1) + ">", nl=False)
            click.secho(el, fg="green")
        env = int(input())
        while env not in range(1, len(json_lst["envs"]) + 1):
            click.secho("in which environment to run?\nchoose one of the below: ", fg="yellow")
            for i, el in enumerate(json_lst["envs"]):
                click.echo("\t" + str(i + 1) + ">", nl=False)
                click.secho(el, fg="green")
            env = int(input())
        env = json_lst["envs"][env - 1]
        json_lst["scripts"][name] = dict(script=script, env=env)
    with open(get_cmd_file(), "w", encoding="UTF-8") as json_data:
        json.dump(json_lst, json_data)
    return


@exqt.command()
def ls():
    with open(get_cmd_file(), "r", encoding="UTF-8") as json_data:
        json_lst = json.load(json_data)
        if not json_lst:
            click.secho("config file empty", fg='red')
            return

        names = json_lst['scripts'].keys()
        click.secho(f"Found " + str(len(names)) + " scripts:")
        for i, script_name in enumerate(names):
            click.echo("\t " + str(i + 1) + ") ", nl=False)
            click.secho(script_name, fg='green')
            script_code = json_lst['scripts'][script_name]['script']
            click.echo("\t   script: ", nl=False)
            click.secho(script_code, fg="bright_blue")
