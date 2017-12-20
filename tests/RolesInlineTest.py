# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class RolesInlineTest(BaseTest):
    def test_badge(self):
        """
        :badge:`42`
        """
        self.do_component_fixture_test('roles-inline', 'badge')

    def test_bg(self):
        """
        :bg-primary:`Primary BG`
        """
        self.do_component_fixture_test('roles-inline', 'bg')

    def test_headings(self):
        """
        :h1:`Heading 1 Role`
        """
        self.do_component_fixture_test('roles-inline', 'headings')

    def test_labels(self):
        """
        :label-default:`Default Label`
        """
        self.do_component_fixture_test('roles-inline', 'labels')

    def test_small(self):
        """
        :small:`tiny text`
        """
        self.do_component_fixture_test('roles-inline', 'small')

    def test_inline_decorators(self):
        """
        Inline decorators
        """
        self.do_component_fixture_test('roles-inline', 'inline-decorators')

    def test_text(self):
        """
        Contextual text roles
        :text-muted:`Muted Text`
        """
        self.do_component_fixture_test('roles-inline', 'text')

    def test_abbr(self):
        """
        abbreviation
        """
        self.do_component_fixture_test('roles-inline', 'abbr')


