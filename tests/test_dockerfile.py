# coding=utf8
from __future__ import unicode_literals


def test_dockerfile():
    with open('../Dockerfile') as f:
        assert 'FROM ubuntu:trusty' in f.read()
