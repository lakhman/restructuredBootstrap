# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class ProgressBarTest(BaseTest):
    def test_progress_bar_active(self):
        """
        Test active class is applied
        """
        self.do_component_fixture_test('progress-bar', 'pb-active')

    def test_progress_bar_basic(self):
        """
        Test a dead basic pb
        """
        self.do_component_fixture_test('progress-bar', 'pb-basic')

    def test_progress_bar_class(self):
        """
        Test we can add a class
        """
        self.do_component_fixture_test('progress-bar', 'pb-custom-class')

    def test_progress_bar_label(self):
        """
        Test we can add a text label
        """
        self.do_component_fixture_test('progress-bar', 'pb-label')

    def test_progress_bar_stacked(self):
        """
        Test we can stack them
        """
        self.do_component_fixture_test('progress-bar', 'pb-stack')

    def test_progress_bar_contextual(self):
        """
        Test we can stack them
        """
        self.do_component_fixture_test('progress-bar', 'pb-contextual')

