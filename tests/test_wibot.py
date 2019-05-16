#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `wibot` package."""

import logging
import unittest

from click.testing import CliRunner

from wibot import cli
from wibot.endpoint import SparkEndpoint
from wibot.rbac import rbac_init
from wibot.cli.cli import admin, compute

logging.getLogger('wibot.spark').setLevel(logging.DEBUG)
logging.getLogger('wibot.spark').addHandler(logging.StreamHandler())

TEST_CDOT = "sjc02cdot03.webex.com"
TEST_SOLIDFIRE = "sin01sdfr01.webex.com"


class TestWibot(unittest.TestCase):
    """Tests for `wibot` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.spark_ws = SparkEndpoint()

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

    def test_rbac_init(self):
        users_db = '/Users/vpatil3/projects/wibot/users.db'
        users = rbac_init(users_db)
        for user in users.keys():
            print(user, users[user])

    def test_admin_cli(self):
        runner = CliRunner()
        cmds = [
            "cdot --help",
            "cdot disks {}".format(TEST_CDOT),
            "cdot health {}".format(TEST_CDOT),
            "cdot interfaces {}".format(TEST_CDOT),
            "cdot nodes {}".format(TEST_CDOT),
            "cdot inventory",
            "pure inventory",
            "solidfire capacity {}".format(TEST_SOLIDFIRE),
            "solidfire health {}".format(TEST_SOLIDFIRE),
            "solidfire inventory",
            "solidfire nodes {}".format(TEST_SOLIDFIRE),
            "solidfire utilization {}".format(TEST_SOLIDFIRE),
        ]

        for cmd in cmds:
            print("cmd: {}".format(cmd))
            result = runner.invoke(admin, cmd.split())
            assert result.exit_code == 0

    def test_compute_cli(self):
        runner = CliRunner()
        cmds = [
            "solidfire capacity {}".format(TEST_SOLIDFIRE),
            "solidfire inventory",
            "solidfire utilization {}".format(TEST_SOLIDFIRE),
        ]

        for cmd in cmds:
            print("cmd: {}".format(cmd))
            result = runner.invoke(admin, cmd.split())
            assert result.exit_code == 0

