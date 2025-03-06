import click
import json
import os
from pyautostart import SmartAutostart
from reminder import start_reminder, stop_reminder, check_status

APP_NAME = 'Gulp'
DEFAULT_INTERVAL = 10
DEFAULT_MESSAGE = 'Drink water, stay hydrated!'
CONFIG = os.path.join(os.path.dirname(__file__), 'config.json')

autostart = SmartAutostart()
options = {
    "args": [
        os.path.join(os.path.dirname(__file__), 'reminder.py')
    ]
}

def load_config():
    try:
        with open(CONFIG, "r") as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        return {
            "interval": DEFAULT_INTERVAL, 
            "message": DEFAULT_MESSAGE,
            "is_running": False
        }

@click.group()
def cli():
    pass

@cli.command(help='To start reminder')
def start():
    start_reminder()

@cli.command(help='To stop reminder')
def stop():
    stop_reminder()

@cli.command(help='To check reminder status')
def status():
    is_running = check_status()
    click.echo('Gulp is running!' if is_running else 'Gulp is not running!')

@cli.command(help='To set new reminder interval and message')
@click.option('--interval', '-i', default=DEFAULT_INTERVAL, help='Reminder interval in minutes')
@click.option('--message', '-m', default=DEFAULT_MESSAGE, help='Reminder message')
def set(interval, message):
    config = load_config()

    is_running = config.get("is_running")
    if is_running:
        click.echo('Please stop the reminder before making any edits.')
        return
    
    config["interval"] = interval
    config["message"] = message

    try:
        with open(CONFIG, "w") as config_file:
            json.dump(config, config_file, indent=4)

        click.echo(f"Reminder set every {interval} minutes with message: '{message}'")
    except Exception as e:
        click.echo(f'Error when saving reminder settings: {e}')

@cli.command(help='To enable reminder at startup')
def enable_startup():
    autostart.enable(APP_NAME, options=options)
    click.echo('Gulp has been successfully enabled at startup')

@cli.command(help='To disable reminder at startup')
def disable_startup():
    autostart.disable(APP_NAME)
    click.echo('Gulp startup is already disabled')

if __name__ == '__main__':
    cli()
