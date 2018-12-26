#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `multiply_two` package."""

import pytest

from click.testing import CliRunner

from multiply_two import multiply_two
from multiply_two import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 2
    assert 'Error: Missing argument "number1"' in result.output


def test_command_line_interface_help():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--help'])
    assert result.exit_code == 0
    assert '--help  Show this message and exit.' in result.output


def test_command_line_interface_one_arg():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['1'])
    assert result.exit_code == 2
    assert 'Missing argument "number2"' in result.output


def test_command_line_interface_valid():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['1', '2'])
    assert result.exit_code == 0
    assert 'The answer is:' in result.output


def test_command_line_interface_nonnumeric_arg():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['hello world', 't'])
    assert result.exit_code == 0
    assert 'The expected arguments should be integers' in result.output
