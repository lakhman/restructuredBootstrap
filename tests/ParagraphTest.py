# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class ParagraphTest(BaseTest):
    def test_paragraph(self):
        """
        Test a simple paragraph directive (renders as a <p>)
        .. paragraph:: A sentence for the paragraph. → <p>A ...</p>
        """
        self.do_component_fixture_test('paragraph', 'paragraph')

    def test_paragraph_multiline(self):
        """
        Test multiple paragraph renders as siblings
        """
        self.do_component_fixture_test('paragraph', 'paragraph-multiline')

    def test_paragraph_lead(self):
        """
        A lead paragraph (a p tag with a lead class).
        """
        self.do_component_fixture_test('paragraph', 'paragraph-lead')

    def test_paragraph_lead_contextual(self):
        """
        A contextual lead paragraph via for e.g: lead-muted, lead-primary
        """
        self.do_component_fixture_test('paragraph', 'paragraph-lead-contextual')
