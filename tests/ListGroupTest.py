# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class ListGroupTest(BaseTest):
    def test_class(self):
        """
        Test list group class
        """
        self.do_component_fixture_test('list-group', 'lg-class')

    def test_button(self):
        """
        Test list group button
        """
        self.do_component_fixture_test('list-group', 'lg-button')

    def test_contextual(self):
        """
        Test list group contextual
        """
        self.do_component_fixture_test('list-group', 'lg-contextual')

    def test_heading(self):
        """
        Test list group heading
        """
        self.do_component_fixture_test('list-group', 'lg-heading')

    def test_href(self):
        """
        Test list group href
        """
        self.do_component_fixture_test('list-group', 'lg-href')

    def test_paragraph(self):
        """
        Test list group paragraph
        """
        self.do_component_fixture_test('list-group', 'lg-paragraph')

    def test_target(self):
        """
        Test list group target
        """
        self.do_component_fixture_test('list-group', 'lg-target')

    def test_linked_items(self):
        """
        Test a single p tag is unwrapped inside a reference (link)
        """
        self.do_component_fixture_test('list-group', 'lg-linked-items')




