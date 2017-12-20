# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class HrTest(BaseTest):
    def test_hr(self):
        """
        Test a .. hr:: renders a <hr />
        """
        self.do_component_fixture_test('hr', 'hr')
