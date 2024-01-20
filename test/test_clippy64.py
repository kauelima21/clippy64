import pytest
import pyperclip
from src.clippy64 import decode, encode
from click.testing import CliRunner


@pytest.fixture()
def runner():
    return CliRunner()


def test_it_should_be_able_to_decode(runner):
    pyperclip.copy('SGVsbG8gV29ybGQ=')
    runner.invoke(decode)
    assert pyperclip.paste() == 'Hello World'


def test_it_should_be_able_to_encode(runner):
    pyperclip.copy('Hello World')
    runner.invoke(encode)
    assert pyperclip.paste() == 'SGVsbG8gV29ybGQ='


if __name__ == '__main__':
    pytest.main()
