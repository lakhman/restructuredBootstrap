# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class FontAwesomeTest(BaseTest):
    def test_fa(self):
        """
        Test a simple icon
        """
        self.do_component_fixture_test('font-awesome', 'fa')

    def test_auto_prepend(self):
        """
        An icon without the 'fa' for icon, size and spin - we add it automatically
        """
        self.do_component_fixture_test('font-awesome', 'fa-auto-prepend')

    def test_no_prepend(self):
        """
        If a user provides an 'fa' - no problem, we check it against our known list and fix it
        """
        self.do_component_fixture_test('font-awesome', 'fa-no-prepend')

    def test_custom_class(self):
        """
        Custom classes (classes not found in our list), should be added as is, ie: we don't prepend "fa-"
        """
        self.do_component_fixture_test('font-awesome', 'fa-custom-class')

    def test_heading(self):
        """
        Roles (all of them) can be used AT THE END of inline tags only, due to the back ticks regex provided by rest.
        """
        self.do_component_fixture_test('font-awesome', 'fa-heading')

    def test_shortcut_classes(self):
        """
        pl,pr => pull-left pull-right, etc - View the test
        """
        self.do_component_fixture_test('font-awesome', 'fa-shortcuts')

    def test_collapse_spaces(self):
        """
        Here, we are testing that the space (between "Role" and ":fa:" is collapsed in the HTML
        If a user wants a space they can add an extra one (use 2 spaces, we only remove 1 space).
        This allows users to butt up icons right next to the header text

        :h1:`Heading 1 Role :fa:`book``
                           ↑        ↓ - Notice this space!
        <p class="h1">Heading 1 Role <span class="fa fa-book"></span> some more text</p>
        "Heading 1 Role <i> some more text"

        We want to get rid of that space so it looks like this
                                   ↓ - No space
        <p class="h1">Heading 1 Role<span class="fa fa-book"></span> some more text</p>
        "Heading 1 Role <i>some more text"

        View the rst test file comments for more info
        """
        self.do_component_fixture_test_with_real_sphinx('font-awesome', 'fa-collapse-spaces')
