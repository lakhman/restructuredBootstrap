# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class HTMLTranslatorOverridesTest(BaseTest):
    def test_alert_link_class(self):
        """
        Test .alert-link is added to links inside an alert
        """
        self.do_component_fixture_test_with_real_sphinx('HTMLTranslatorOverrides', 'alert-link-class')

    def test_bullet_list_dropdown_class(self):
        """
        Tests a .dropdown-menu class is added to a bullet list inside a button group
        """
        self.do_component_fixture_test_with_real_sphinx('HTMLTranslatorOverrides', 'bullet-list-dropdown')

    def test_bullet_list_panel_list(self):
        """
        Tests .list-group class is added to the list group inside a panel
        """
        self.do_component_fixture_test_with_real_sphinx('HTMLTranslatorOverrides', 'bullet-list-panel-list')

    def test_bullet_list_panel_list_group(self):
        """
        Tests .list-group-item is added
        """
        self.do_component_fixture_test_with_real_sphinx('HTMLTranslatorOverrides', 'bullet-list-panel-list-group')

    def test_list_item_first_class(self):
        """
        Test list item first class
        """
        self.do_component_fixture_test_with_real_sphinx('HTMLTranslatorOverrides', 'list-item-first-class')

    def test_reference_no_follow(self):
        """
        Test we can add a exclamation mark to the start of a URL to add a rel="nofollow"
        """
        self.do_component_fixture_test_with_real_sphinx('HTMLTranslatorOverrides', 'reference-no-follow')

    def test_modal_attributes_added(self):
        """
        Test modal target and other attributes are added if name starts with "modal-"
        """
        self.do_component_fixture_test_with_real_sphinx('HTMLTranslatorOverrides', 'modal-target')

    def test_table_class(self):
        """
        Test even and add classes
        Test .table class is added
        Remove border=1 provided by docutils
        """
        self.do_component_fixture_test_with_real_sphinx('HTMLTranslatorOverrides', 'table-class')

    def test_table_class_append(self):
        """
        Test bs classes like bordered are prepended with "table-"
        """
        self.do_component_fixture_test_with_real_sphinx('HTMLTranslatorOverrides', 'table-class-append')

    def test_transition_class(self):
        """
        Test docutils classes are removed from <hr> elements
        """
        self.do_component_fixture_test_with_real_sphinx('HTMLTranslatorOverrides', 'transition-class')
