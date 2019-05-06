#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `wibot` package."""


import unittest
from click.testing import CliRunner
import os
from wibot.endpoint import SparkEndpoint
from wibot import cli
import logging

logging.getLogger('wibot.spark').setLevel(logging.DEBUG)
logging.getLogger('wibot.spark').addHandler(logging.StreamHandler())


class TestWibot(unittest.TestCase):
    """Tests for `wibot` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        bot_name = "Storage"
        bot_token = os.environ.get('STORAGE_BOT_TOKEN')
        self.spark_ws = SparkEndpoint(bot_name, bot_token)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_get_all_bot_devices(self):
        print(list(map(lambda device: device['webSocketUrl'], self.spark_ws.get_all_devices())))

    def test_delete_all_bot_devices(self):
        self.spark_ws.delete_all_existing_devices()

    def test_get_device_ws_url(self):
        print(self.spark_ws.get_websocket_url())

    def test_register_device(self):
        print(self.spark_ws.register_device())

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'wibot.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
