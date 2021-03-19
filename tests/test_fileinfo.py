#!/usr/bin/env python

"""Tests for `fileinfo` package."""


import unittest
from click.testing import CliRunner
from unittest.mock import patch


from fileinfo import fileinfo
from fileinfo import cli


class TestFileinfo(unittest.TestCase):
    """Tests for `fileinfo` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'fileinfo.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output


def test_init():
    filename = 'somefile.net'
    fi = fileinfo.FileInfo(filename)
    assert fi.filename == filename


def test_init_relative():
    filename = 'somefile.ext'
    relative_path = '../{}'.format(filename)
    fi = fileinfo.FileInfo(relative_path)
    assert fi.filename == filename


@patch('os.path.getsize')
@patch('os.path.abspath')
def test_get_info(abspath_mock, getsize_mock):
    filename = 'somefile.ext'
    original_path = '../{}'.format(filename)

    test_abspath = 'some/abs/path'
    abspath_mock.return_value = test_abspath

    test_size = 1234
    getsize_mock.return_value = test_size
    fi = fileinfo.FileInfo(original_path)
    assert fi.get_info() == (filename, original_path, test_abspath, test_size)
