# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class ButtonTest(BaseTest):
    def test_contextual(self):
        """
        Test a default <button> is rendered with classes .btn.btn-primary
        """
        self.do_component_fixture_test('button', 'button-contextual')

    def test_button_doc_ref(self):
        """
        Test we can use the :doc: option to reference an internal document
        """
        self.do_component_fixture_test_with_real_sphinx('button', 'button-doc-ref')

    def test_collapsible(self):
        """
        Test a <button> is rendered with collapsible attributes
        """
        self.do_component_fixture_test('button', 'button-collapse-target')

    def test_collapsible_href_js_void(self):
        """
        Test a <button> is rendered with collapsible attributes, the href should be javascript:void()
        """
        self.do_component_fixture_test('button', 'button-collapse-target-href')

    def test_custom_class(self):
        """
        Test a default <button> is rendered with a custom class .btn.btn-default.btn-xs.custom_user_class
        .custom_user_class should always be last
        """
        self.do_component_fixture_test('button', 'button-custom-class')

    def test_default(self):
        """
        Test a default <button> is rendered with classes .btn.btn-default
        """
        self.do_component_fixture_test('button', 'button-default')

    def test_plain(self):
        """
        Test a plain <button> is rendered with no classes
        """
        self.do_component_fixture_test('button', 'button-plain')

    def test_disabled(self):
        """
        Test a default <button> is rendered as disabled .btn.btn-primary.disabled
        """
        self.do_component_fixture_test('button', 'button-disabled')

    def test_group(self):
        """
        Tests a button group is rendered (with correct role and optional aria-label)
        """
        self.do_component_fixture_test_with_real_sphinx('button', 'button-group')

    def test_vertical_group(self):
        """
        Tests a button group is rendered with a vertical class
        """
        self.do_component_fixture_test_with_real_sphinx('button', 'button-group-vertical')

    def test_group_class(self):
        """
        Tests a button group is rendered with a custom class (for justification for example)
        """
        self.do_component_fixture_test_with_real_sphinx('button', 'button-group-class')

    def test_group_arg_class(self):
        """
        Tests a button group is rendered with a custom argument class (for justification for example)
        It should be prepended if required.
        """
        self.do_component_fixture_test('button', 'button-group-arg-class')

    def test_group_arg_class_invalid(self):
        """
        Tests a button group checks for invalid classes
        """
        self.do_component_fixture_test('button', 'button-group-invalid-arg-class')

    def test_onclick(self):
        """
        Test a button :onclick:
        """
        self.do_component_fixture_test('button', 'button-onclick')

    def test_onmouseover(self):
        """
        Test a button :onmouseover:
        """
        self.do_component_fixture_test('button', 'button-onmouseover')

    def test_onmouseout(self):
        """
        Test a button :onmouseout:
        """
        self.do_component_fixture_test('button', 'button-onmouseout')

    def test_href(self):
        """
        Test an <a> tag is rendered as a.btn-primary.btn-xs
        """
        self.do_component_fixture_test('button', 'button-href')

    def test_href_void(self):
        """
        Test an <a> tag is rendered with href void - expanded
        """
        self.do_component_fixture_test('button', 'button-href-void')

    def test_href_disabled(self):
        """
        Test an <a> tag is rendered as a.btn-primary.btn-xs
        """
        self.do_component_fixture_test('button', 'button-href-disabled')

    def test_href_target(self):
        """
        Test an <a> tag is rendered as a.btn-primary.btn-xs with a _blank target window
        """
        self.do_component_fixture_test('button', 'button-href-target')

    def test_name(self):
        """
        Test we can add a name (ID) to this button
        """
        self.do_component_fixture_test('button', 'button-name')

    def test_modal_toggle(self):
        """
        Test modal toggle button and attributes
        """
        self.do_component_fixture_test('button', 'button-modal-toggle')

    def test_size(self):
        """
        Test a default <button> is rendered with classes .btn.btn-default.btn-xs
        """
        self.do_component_fixture_test('button', 'button-size')

    def test_size_directives(self):
        """
        Test our size directives .. button-xs-primary::
        """
        self.do_component_fixture_test('button', 'button-size-directives')

    def test_toggle(self):
        """
        Test an <a> tag is rendered as a.btn-primary.btn-xs.toggle with toggle attributes
        The list group with a dropdown-menu class is added immediately after is used
        """
        self.do_component_fixture_test_with_real_sphinx('button', 'button-toggle')

    def test_toolbar(self):
        """
        Tests a button toolbar is rendered with btn-groups and buttons inside
        """
        self.do_component_fixture_test('button', 'button-toolbar')
