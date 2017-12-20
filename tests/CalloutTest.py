# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class CalloutTest(BaseTest):
    def test_callouts(self):
        """
        A custom callout which appends a ``bs-callout`` and ``bs-callout-{type}`` class.
        """
        self.do_component_fixture_test('callout', 'callout')

    def test_contextual_class(self):
        """
        Test contextual variants
        """
        self.do_component_fixture_test('callout', 'callout-contextual')

    def test_title_added_as_heading(self):
        """
        Test a title can be added, it should be a heading element
        """
        self.do_component_fixture_test('callout', 'callout-title')

