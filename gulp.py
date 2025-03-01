import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def cli(count, name):
    for i in range(count):
        click.echo(f'Hello {name}!')

if __name__ == '__main__':
    cli()