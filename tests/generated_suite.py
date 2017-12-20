# -*- encoding: utf-8 -*-
import unittest2 as unittest
from unittest import TestCase

from .AlertTest import AlertTest
from .ButtonTest import ButtonTest
from .CalloutTest import CalloutTest
from .ClearfixTest import ClearfixTest
from .ContainerTest import ContainerTest
from .FontAwesomeTest import FontAwesomeTest
from .ListGroupTest import ListGroupTest
from .GridTest import GridTest
from .MediaTest import MediaTest
from .ModalTest import ModalTest
from .HrTest import HrTest
from .PanelTest import PanelTest
from .ParagraphTest import ParagraphTest
from .ProgressBarTest import ProgressBarTest
from .RolesTest import RolesTest
from .RolesInlineTest import RolesInlineTest
from .TabsTest import TabsTest
from .TooltipTest import TooltipTest
from .HTMLTranslatorOverridesTest import HTMLTranslatorOverridesTest


TestCase.maxDiff = None
unittest.util._MAX_LENGTH = 10000

# -------------------------------------------------------------------------------------------------
# Generated test suite, find all tests from these modules and run them
#
# To run this with PyCharm use the following test configuration
#
# Path: /path/to/project/sphinx-bootstrap/src/tests/generated_suite.py
# Working Directory: /path/to/project/sphinx-bootstrap/tests
#
# With tox:
# tox -e py27
# -------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(AlertTest))
    test_suite.addTest(unittest.makeSuite(ButtonTest))
    test_suite.addTest(unittest.makeSuite(CalloutTest))
    test_suite.addTest(unittest.makeSuite(ClearfixTest))
    test_suite.addTest(unittest.makeSuite(ContainerTest))
    test_suite.addTest(unittest.makeSuite(FontAwesomeTest))
    test_suite.addTest(unittest.makeSuite(GridTest))
    test_suite.addTest(unittest.makeSuite(HTMLTranslatorOverridesTest))
    test_suite.addTest(unittest.makeSuite(ListGroupTest))
    test_suite.addTest(unittest.makeSuite(MediaTest))
    test_suite.addTest(unittest.makeSuite(ModalTest))
    test_suite.addTest(unittest.makeSuite(HrTest))
    test_suite.addTest(unittest.makeSuite(PanelTest))
    test_suite.addTest(unittest.makeSuite(ParagraphTest))
    test_suite.addTest(unittest.makeSuite(ProgressBarTest))
    test_suite.addTest(unittest.makeSuite(RolesInlineTest))
    test_suite.addTest(unittest.makeSuite(RolesTest))
    test_suite.addTest(unittest.makeSuite(TabsTest))
    test_suite.addTest(unittest.makeSuite(TooltipTest))

    runner = unittest.TextTestRunner()
    runner.run(test_suite)
