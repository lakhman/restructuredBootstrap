# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class ModalTest(BaseTest):
    def test_modal(self):
        """
        Test modal complete
        """
        self.do_component_fixture_test('modal', 'modal')

    def test_modal_class_arg(self):
        """
        Test modal class arg
        """
        self.do_component_fixture_test('modal', 'modal-class-arg')

    def test_modal_lg(self):
        """
        Test modal lg
        """
        self.do_component_fixture_test('modal', 'modal-lg')

    def test_modal_container(self):
        """
        Test modal container
        """
        self.do_component_fixture_test('modal', 'modal-container')

    def test_modal_container_name(self):
        """
        Test modal container name error
        """
        self.do_component_fixture_test('modal', 'modal-container-name')

    def test_modal_header(self):
        """
        Test modal header
        """
        self.do_component_fixture_test('modal', 'modal-header')

    def test_modal_body(self):
        """
        Test modal body
        """
        self.do_component_fixture_test('modal', 'modal-body')

    def test_modal_body_title(self):
        """
        Test modal body titles
        """
        self.do_component_fixture_test('modal', 'modal-body-titles')

    def test_modal_footer(self):
        """
        Test modal footer
        """
        self.do_component_fixture_test('modal', 'modal-footer')

    def test_modal_footer_close_class(self):
        """
        Test modal footer close class
        """
        self.do_component_fixture_test('modal', 'modal-footer-close-class')

    def test_modal_link_reference(self):
        """
        Test we can open modal via inline text
        """
        self.do_component_fixture_test_with_real_sphinx('modal', 'modal-link-reference')

    def test_modal_close_text(self):
        """
        Test we can pass custom close text
        """
        self.do_component_fixture_test('modal', 'modal-close-text')
