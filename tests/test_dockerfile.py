# coding=utf8
from __future__ import unicode_literals

import os

project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def test_dockerfile():
    with open('{}/Dockerfile'.format(project_path)) as f:
        assert 'FROM ubuntu:trusty' in f.read()
