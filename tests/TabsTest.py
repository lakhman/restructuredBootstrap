# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class TabsTest(BaseTest):
    def test_tabs_basic(self):
        """
        Test our basic outer tab container with 2 simple tabs
        """
        self.do_component_fixture_test_with_real_sphinx('tabs', 'tabs-basic')

    def test_tabs_name(self):
        """
        Test a custom name can be used
        """
        self.do_component_fixture_test_with_real_sphinx('tabs', 'tabs-tab-name')

    def test_tabs_titles(self):
        """
        Test titles are rendered in tabs
        """
        self.do_component_fixture_test_with_real_sphinx('tabs', 'tabs-titles')

    def test_tabs_basic_active(self):
        """
        Test our tabs active class is applied
        """
        self.do_component_fixture_test_with_real_sphinx('tabs', 'tabs-basic-active')

    def test_tabs_class(self):
        """
        Test a tabs class via argument
        """
        self.do_component_fixture_test_with_real_sphinx('tabs', 'tabs-class')

    def test_tab_class(self):
        """
        Test a single tab class (via option and argument)
        """
        self.do_component_fixture_test_with_real_sphinx('tabs', 'tabs-tab-class')

    def test_tab_title(self):
        """
        Test tab title is parsed for inline roles
        """
        self.do_component_fixture_test_with_real_sphinx('tabs', 'tabs-tab-title')

    def test_tab_title_empty_error(self):
        """
        Test tab title throws an error for blank titles
        """
        self.do_component_fixture_test('tabs', 'tabs-tab-title-empty-error')

    def test_tab_invalid_children(self):
        """
        Test tabs throws an error when has invalid child
        """
        self.do_component_fixture_test('tabs', 'tabs-invalid-children')
