import os
#import sys
import json
import subprocess
import click


def get_cmd_file():
    user_home = os.path.expanduser("~")
    os.chdir(user_home)
    if not (os.path.exists(".exqt.json")):
        file = open(".exqt.json", "w+")
        file.close()
    return str(os.getcwd() + "/.exqt.json")


cmd_json = get_cmd_file()
if cmd_json == "":
    click.echo("error:\nhome dir not found")


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
    # I don't know what to put here
    return


@exqt.command()
@click.argument('name', nargs=-1)
def run(name):
    with open(cmd_json) as json_data:
        json_lst = json.load(json_data)
        if not json_lst:
            click.secho("config file not found", fg='red')
            return
        keys_lst = json_lst["scripts"].keys()
        for i, el in enumerate(name):
            if el not in keys_lst:
                click.secho("command "+el+" not found", fg='red')
                click.secho("consider using `exqt add` to add new scripts", fg='red')
            else:
                script = json_lst["scripts"][el]["script"]
                run_script(script)

            # click.echo(json_lst)
            # click.echo(json_lst.keys())
        json_data.close()
    return


@exqt.command()
#@click.argument('name', nargs=-1)
def add():

    return

