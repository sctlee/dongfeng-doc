# coding=utf8
from __future__ import unicode_literals

import codecs
import os

project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def test_project():
    with codecs.open('{}/README.md'.format(project_path), encoding='utf-8') as f:
        assert 'slate' in f.read()
