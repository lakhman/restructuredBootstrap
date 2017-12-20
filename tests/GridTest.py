# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class GridTest(BaseTest):
    def test_column(self):
        """
        Columns default to **xs** and **12** when no arguments or options provided.
        """
        self.do_component_fixture_test('grid', 'column')

    def test_column_arg_classes(self):
        """
        Custom classes can be provided via arguments.
        """
        self.do_component_fixture_test('grid', 'column-arg-classes')

    def test_column_arg_classes_width(self):
        """
        Shorthand Width argument can be provided via argument
        """
        self.do_component_fixture_test('grid', 'column-arg-classes-width')

    def test_column_offset(self):
        """
        Column offset should be applied when using default size and width.
        """
        self.do_component_fixture_test('grid', 'column-offset')

    def test_column_offset_width(self):
        """
        Column offset should be applied when using default size of xs.
        """
        self.do_component_fixture_test('grid', 'column-offset-width')

    def test_column_offset_zero(self):
        """
        Column offset class can have a zero, default to xs-12
        """
        self.do_component_fixture_test('grid', 'column-offset-0')

    def test_column_offset_multi_width(self):
        """
        Test shorthand offset notation 2,-,4,-
        """
        self.do_component_fixture_test('grid', 'column-offset-multi-width')

    def test_column_pull(self):
        """
        Column pull should be applied when using default size and width.
        """
        self.do_component_fixture_test('grid', 'column-pull')

    def test_column_pull_width(self):
        """
        Column pull should be applied when using default size of xs and user provided width.
        """
        self.do_component_fixture_test('grid', 'column-pull-width')

    def test_column_pull_multi_width(self):
        """
        Column pull multi width 12,-,6,0 notation
        """
        self.do_component_fixture_test('grid', 'column-pull-multi-width')

    def test_column_push(self):
        """
        Column push should be applied when using default size and width.
        """
        self.do_component_fixture_test('grid', 'column-push')

    def test_column_push_width(self):
        """
        Column push should be applied when using default size of xs and user provided width.
        """
        self.do_component_fixture_test('grid', 'column-push-width')

    def test_column_push_multi_width(self):
        """
        Column push multi width 12,-,6,0 notation
        """
        self.do_component_fixture_test('grid', 'column-push-multi-width')

    def test_column_width(self):
        """
        Columns should default to **xs** if no size provided.
        """
        self.do_component_fixture_test('grid', 'column-width')

    def test_column_width_arg_class(self):
        """
        Classes via arguments should be applied when using width option
        """
        self.do_component_fixture_test('grid', 'column-width-arg-class')

    def test_column_width_push(self):
        """
        Test push and width can be used with custom class
        """
        self.do_component_fixture_test('grid', 'column-width-push')

    def test_column_multi_width(self):
        """
        Columns can use shorthand notation 12,12,6,4 (xs,sm,md,lg).
        """
        self.do_component_fixture_test('grid', 'column-multi-width')

    def test_column_multi_width_dangling(self):
        """
        When using shorthand, you cannot have a dangling comma
        """
        self.do_component_fixture_test('grid', 'column-multi-width-dangling')

    def test_column_multi_width_missing(self):
        """
        Columns can use shorthand notation with 2 digits 12,6, (xs,sm,).
        """
        self.do_component_fixture_test('grid', 'column-multi-width-missing')

    def test_column_multi_width_skip(self):
        """
        Columns widths can skip size classes with a zero 12,0, 6,0 (xs,sm,md,lg).
        """
        self.do_component_fixture_test('grid', 'column-multi-width-skip')

    def test_column_multi_width_extra(self):
        """

        """
        self.do_component_fixture_test('grid', 'column-multi-width-extra')

    def test_row(self):
        """
        Default empty div.row
        """
        self.do_component_fixture_test('grid', 'row')

    def test_row_arg_class(self):
        """
        Row with a custom class passed as an argument
        """
        self.do_component_fixture_test('grid', 'row-arg-class')

    def test_row_class(self):
        """
        Row with a custom class passed as an option
        """
        self.do_component_fixture_test('grid', 'row-class')




