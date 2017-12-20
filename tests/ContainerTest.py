# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class ContainerTest(BaseTest):
    def test_empty(self):
        """
        Test an empty div for a container (removing the .container class)
        """
        self.do_component_fixture_test('container', 'container')

    def test_argument_class(self):
        """
        Test arguments are added as classes
        """
        self.do_component_fixture_test('container', 'container-arg-class')

    def test_container_clearfix(self):
        """
        Clearfixes are container nodes with no content
        We strip the line break if no content to keep the HTML source clean
        """
        self.do_component_fixture_test('container', 'container-clearfix')

    def test_container_contextual(self):
        """
        Container contextual variants
        """
        self.do_component_fixture_test('container', 'container-contextual')
