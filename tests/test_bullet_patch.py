# -*- coding: utf-8 -*-

from __future__ import print_function

import unittest2 as unittest
from sphinx_testing import TestApp

from .BaseTest import BaseTest
import util
from util import with_app


# python setup.py test -s bootstrap.tests.test_bullet_patch.TestBulletListPatch
# tox -e py27 -- -s bootstrap.tests.test_bullet_patch.TestBulletListPatch
class TestBulletListPatch(BaseTest):

    @with_app()
    def xtest_relations(self, app, *args):
        self.skipTest('Not ready')
        """
        Test our visit bullet list patch

        Not used, disabled in generated test
        """
        app = TestApp(
            srcdir=util.test_apps + '/test-toctree-glob',
            copy_srcdir_to_tmpdir=True,
        )
        app.builder.build_all()
        assert app.builder.relations['index'] == [None, None, 'foo']
        assert app.builder.relations['foo'] == ['index', 'index', 'bar/index']
        assert app.builder.relations['bar/index'] == ['index', 'foo', 'bar/bar_1']
        assert app.builder.relations['bar/bar_1'] == ['bar/index', 'bar/index', 'bar/bar_2']
        assert app.builder.relations['bar/bar_2'] == ['bar/index', 'bar/bar_1', 'bar/bar_3']
        assert app.builder.relations['bar/bar_3'] == ['bar/index', 'bar/bar_2', 'bar/bar_4/index']
        assert app.builder.relations['bar/bar_4/index'] == ['bar/index', 'bar/bar_3', 'baz']
        assert app.builder.relations['baz'] == ['index', 'bar/bar_4/index', 'qux/index']
        assert app.builder.relations['qux/index'] == ['index', 'baz', 'qux/qux_1']
        assert app.builder.relations['qux/qux_1'] == ['qux/index', 'qux/index', 'qux/qux_2']
        assert app.builder.relations['qux/qux_2'] == ['qux/index', 'qux/qux_1', None]
        assert 'quux' not in app.builder.relations


if __name__ == "__main__":
    unittest.main(verbosity=2)
