# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class PanelTest(BaseTest):
    def test_classes(self):
        """
        Tests a panel with a user specified custom class
        """
        self.do_component_fixture_test('panel', 'panel-classes')

    def test_panel_footer(self):
        """
        Test the panel footer and you can use custom directives within it (e.g: buttons)
        """
        self.do_component_fixture_test('panel', 'panel-footer')

    def test_panel_footer_simple(self):
        """
        Tests a simple panel footer, simple text can be provided via argument
        and test custom class via :class: option
        """
        self.do_component_fixture_test('panel', 'panel-footer-simple')

    def test_panel_heading(self):
        """
        Test panel heading not inside a .panel-title
        """
        self.do_component_fixture_test('panel', 'panel-heading')

    def test_panel_heading_inline_role(self):
        """
        Test panel heading not inside a .panel-title with our inline parser (font awesome icons)
        """
        self.do_component_fixture_test('panel', 'panel-heading-inline-role')

    def test_panel_list(self):
        """
        Tests lists inside a panel are rendered outside the `.panel-body`
        Tests a single list only (no other nodes in a panel)
        """
        self.do_component_fixture_test_with_real_sphinx('panel', 'panel-list')

    def test_panel_list_class(self):
        """
        Test we can apply a class to list items in a panel
        """
        self.do_component_fixture_test_with_real_sphinx('panel', 'panel-list-class')

    def test_panel_list_node_first(self):
        """
        Tests lists inside a panel are rendered outside the `.panel-body`
        Tests multiple nodes, the list should be outside the panel FIRST, the paragraphs inside.
        """
        self.do_component_fixture_test_with_real_sphinx('panel', 'panel-list-node-first')

    def test_panel_list_node_last(self):
        """
        Tests lists inside a panel are rendered outside the `.panel-body`
        Tests multiple nodes, the list should be outside the panel LAST, the paragraphs inside.
        """
        self.do_component_fixture_test_with_real_sphinx('panel', 'panel-list-node-last')

    def test_panel_simple(self):
        """
        Tests a simple panel, By default, we default to the default class if nothing provided.
        """
        self.do_component_fixture_test('panel', 'panel-simple')

    def test_panel_table(self):
        """
        Tests tables inside a panel are rendered outside the `.panel-body`
        Tests a single table only (no other nodes in a panel)
        """
        self.do_component_fixture_test_with_real_sphinx('panel', 'panel-table')

    def test_panel_table_node_first(self):
        """
        Tests tables inside a panel are rendered outside the `.panel-body`
        Tests multiple nodes, the table should be outside the panel FIRST, the paragraphs inside.
        """
        self.do_component_fixture_test_with_real_sphinx('panel', 'panel-table-node-first')

    def test_panel_table_node_last(self):
        """
        Tests tables inside a panel are rendered outside the `.panel-body`
        Tests multiple nodes, the table should be outside the panel LAST, the paragraphs inside.
        """
        self.do_component_fixture_test_with_real_sphinx('panel', 'panel-table-node-last')

    def test_panel_title(self):
        """
        Tests the panel heading with an exclamation mark ! (to indicate it should be placed inside a .panel-title)
        """
        self.do_component_fixture_test('panel', 'panel-title')

    def test_panel_title_inline_role(self):
        """
        Tests we can use inline roles in a panel title
        """
        self.do_component_fixture_test('panel', 'panel-title-inline-role')

    def test_panel_contextual(self):
        """
        Tests panel contextual
        """
        self.do_component_fixture_test('panel', 'panel-contextual')
