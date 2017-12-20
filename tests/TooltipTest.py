# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class TooltipTest(BaseTest):
    def test_tooltip(self):
        """
        Test a tooltip-top is rendered.
        """
        self.do_component_fixture_test_with_real_sphinx('tooltip', 'tooltip')

    def test_invalid_tooltip(self):
        """
        Test an error is thrown with invalid tooltip text
        """
        self.do_component_fixture_test('tooltip', 'tooltip-invalid-text')

