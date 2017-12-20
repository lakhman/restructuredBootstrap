# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class ClearfixTest(BaseTest):
    def test_simple(self):
        """
        Test an empty div.clearfix
        """
        self.do_component_fixture_test('clearfix', 'clearfix-simple')

    def test_custom_class(self):
        """
        Test a div.clearfix with a custom class
        """
        self.do_component_fixture_test('clearfix', 'clearfix-custom-class')
