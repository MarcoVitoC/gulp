import click
from plyer import notification

def notify():
    notification.notify(
        title='💧 Gulp',
        message='Drink water, stay hydrated!',
        timeout=3
    )

@click.command()
@click.option('--count', default=1, help='number of greetings')
def cli(count):
    for i in range(count):
        notify()

if __name__ == '__main__':
    cli()