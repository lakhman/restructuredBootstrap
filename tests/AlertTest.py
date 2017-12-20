# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class AlertTest(BaseTest):
    def test_classes(self):
        """
        Custom classes should be added and in correct order. `.alert-info` should be placed before custom user classes.
        """
        self.do_component_fixture_test('alert', 'alert-classes')

    def test_dismissible(self):
        """
        Test dismissible class and button is added to the alert
        """
        self.do_component_fixture_test('alert', 'alert-dismissible')

    def test_link(self):
        """
        Test alert-link class is added to links within an alert box
        """
        self.do_component_fixture_test('alert', 'alert-link')

    def test_title(self):
        """
        Test title is added as first <p> tag
        e.g: .. alert:: This is the title
        """
        self.do_component_fixture_test('alert', 'alert-title')

    def test_no_title(self):
        """
        Test no title is added, text should not be in a <p>
        """
        self.do_component_fixture_test('alert', 'alert-no-title')

    def test_type(self):
        """
        Test alert type is added
        """
        self.do_component_fixture_test('alert', 'alert-type')

    def test_argument_type(self):
        """
        Test alert argument type can be added via argument
        """
        self.do_component_fixture_test('alert', 'alert-argument-type')