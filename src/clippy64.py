import pyperclip
import click
import base64


def base64_decode(string_to_decode):
    return base64.b64decode(string_to_decode).decode('utf-8')


def base64_encode(string_to_encode):
    return base64.b64encode(string_to_encode.encode('utf-8')).decode('utf-8')


@click.group()
def cli():
    pass


@cli.command()
def decode():
    get_from_transfer_area = pyperclip.paste()
    decoded = base64_decode(get_from_transfer_area)
    pyperclip.copy(decoded)
    click.echo('Decode realizado com sucesso!')


@cli.command()
def encode():
    get_from_transfer_area = pyperclip.paste()
    encoded = base64_encode(get_from_transfer_area)
    pyperclip.copy(encoded)
    click.echo('Encode realizado com sucesso!')


if __name__ == '__main__':
    cli()
