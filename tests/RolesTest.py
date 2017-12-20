# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class RolesTest(BaseTest):
    def test_badge(self):
        """
        :badge:`42`
        """
        self.do_component_fixture_test('roles', 'badge')

    def test_bg(self):
        """
        :bg-primary:`Primary BG`
        """
        self.do_component_fixture_test('roles', 'bg')

    def test_headings(self):
        """
        :h1:`Heading 1 Role`
        """
        self.do_component_fixture_test_with_real_sphinx('roles', 'headings')

    def test_labels(self):
        """
        :label-default:`Default Label`
        """
        self.do_component_fixture_test('roles', 'labels')

    def test_inline_decorators(self):
        """
        Test kbd, ins, del, mark, strike, underline, etc
        :text-muted:`Muted Text`
        """
        self.do_component_fixture_test('roles', 'inline-decorators')

    def test_small(self):
        """
        :small:`tiny text`
        """
        self.do_component_fixture_test('roles', 'small')

    def test_text(self):
        """
        Contextual text roles
        :text-muted:`Muted Text`
        """
        self.do_component_fixture_test('roles', 'text')

    def test_list_group_heading_class(self):
        """
        Test list group heading class

        We apply a new line after jiggling the tree in list group.
        """
        self.do_component_fixture_test('roles', 'lg-heading-class')

    def test_invalid_chars(self):
        """
        We had a bug where + and - was parsed into lists.
        Fixed by parsing via Inliner.parse, this tests that.
        """
        self.do_component_fixture_test('roles', 'invalid-chars')

