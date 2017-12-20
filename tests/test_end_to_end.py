# -*- coding: utf-8 -*-

from __future__ import print_function

import unittest2 as unittest

from .BaseTest import BaseTest
import util


class TestEndToEnd(BaseTest):
    @util.with_app(testapp='test-example-doc')
    def xtest_example_document_build(self, app, *args):
        self.skipTest('Not ready')
        app.build()

        html = (app.outdir / 'index.html').read_text()
        self.assertIn('<h1>Heading 1 Role</h1>', html)
        self.assertIn('<h2>Heading 2 Role <span class="label label-default">HTML should render normally</span></h2>', html)
        self.assertIn('<h3>Heading 3 Role</h3>', html)
        self.assertIn('<h4>Heading 4 Role</h4>', html)
        self.assertIn('<h5>Heading 5 Role</h5>', html)
        self.assertIn('<h6>Heading 6 Role</h6>', html)

if __name__ == '__main__':
    unittest.main(verbosity=2)
