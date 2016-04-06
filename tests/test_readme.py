# coding=utf8
from __future__ import unicode_literals

import codecs


def test_project():
    with codecs.open('../README.md', encoding='utf-8') as f:
        assert 'slate' in f.read()
