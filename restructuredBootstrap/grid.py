#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
import re
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from builtins import str as strtext


class PageRow(Directive):
    """
    Fixed rows are a given pixel width (940px) split between 12 columns.
    """
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged
    }

    def run(self):
        self.assert_has_content()
        node = nodes.container(self.content)
        node['classes'] = ['row']
        if self.arguments:
            node['classes'] += [self.arguments[0]]
        node['classes'] += self.options.get('class', [])

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class PageColumn(Directive):
    """
    A page column with width, offset, push, pull.
    You can pass shorthand columns like 12,-,6,- and we'll map it to the correct BS size class
    You can also use this for offset, push and pull.
    """
    required_arguments, optional_arguments = 0, 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'width': directives.unchanged,
        'offset': directives.unchanged,
        'push': directives.unchanged,
        'pull': directives.unchanged,
        'class': directives.class_option
    }

    def parse_shorthand_to_classes(self, shorthand, class_format="col-%s-%s"):
        """
        Convert width: 12,12,6,6 into [col-xs-12, col-sm-12, col-md-6, col-lg-6]
        Convert width: 12,-,6,-  into [col-xs-12, col-md-6]
        Convert offset: -,0,6,- into [col-sm-offset-0, col-md-offset-6]
        .. also converts push and pull via class_format

        :param shorthand: String to split
        :param class_format: String to format on (offset, pull, push)
        :return classes: List of string classes to be applied to node
        """
        try:
            shorthand_list = shorthand.split(',')

            if shorthand[-1] == ',':
                raise ValueError(
                    'No dangling commas are allowed in column '
                    'width,offset,push or pull.'
                )

            if len(shorthand_list) > 4:
                msg = 'To many size classes "%s" (for shorthand), ' \
                      'use 4 or less (xs,sm,md,lg).' % shorthand
                raise ValueError(msg)

            zipped = zip(shorthand_list, ['xs', 'sm', 'md', 'lg'])
            stripped_zipped = [x for x in zipped if strtext(x[0]).isnumeric()]

            # Remove '0' values for width, offset, push and pull can have a 0
            if class_format == 'col-%s-%s':
                stripped_zipped = [x for x in stripped_zipped if x[0] > '0']

            classes = map(lambda pair: class_format % (pair[1], pair[0]),
                          stripped_zipped)

            return classes
        except ValueError as error:
            msg = 'Incorrect shorthand format "%s". ' \
                  'Try "12,-,6,-" for "col-sm-12, col-md-6"' % shorthand
            raise ValueError(error if error else msg)

    def match_shorthand_class_via_argument(self, argument):
        """
        Users can pass `12,-,6,-` via an *argument*, match and return it if so
        also, create and return other user provided node classes
        """
        arg_classes = argument.split(' ')
        shorthand = None
        node_classes = []

        for i, c in enumerate(arg_classes):
            rx = r"^(?:[0-9]+|[-]{,1})(?:,?)((?:[0-9]+|[-]{,1})(?:,))?" \
                 r"((?:[0-9]+|[-]{,1})(?:,))?(?:[0-9]+|[-]{,1})$"
            match = re.match(rx, c)
            if match:
                shorthand = match.group()
                arg_classes[i] = ''
            else:
                node_classes += directives.class_option(c)

        return shorthand, node_classes

    def get_width_classes_from_shorthand(self, shorthand):
        """
        If we have a valid shorthand class, convert it, else default to xs-12
        """
        if shorthand:
            try:
                width_classes = self.parse_shorthand_to_classes(shorthand)
            except ValueError as error:
                raise self.error(error)
        else:
            width = self.options.get('width', '12')
            width_classes = ["col-xs-%s" % width]

        return width_classes

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = nodes.container(text)
        node_user_classes = []

        # :width: takes priority over a width provided via argument
        if 'width' in self.options:
            node['classes'] += self.get_width_classes_from_shorthand(
                self.options.get('width'))
        else:
            node['classes'] += self.get_width_classes_from_shorthand(None)

        if self.arguments:
            shorthand, node_user_classes = self.match_shorthand_class_via_argument(
                self.arguments[0])
            if shorthand and 'width' not in self.options:
                node['classes'] += self.get_width_classes_from_shorthand(
                    shorthand)

        # Offset, push and pull - No default value, classes are only added if option is provided
        if 'offset' in self.options:
            node['classes'] += self.parse_shorthand_to_classes(
                self.options.get('offset'), "col-%s-offset-%s")

        if 'push' in self.options:
            node['classes'] += self.parse_shorthand_to_classes(
                self.options.get('push'), "col-%s-push-%s")

        if 'pull' in self.options:
            node['classes'] += self.parse_shorthand_to_classes(
                self.options.get('pull'), "col-%s-pull-%s")

        # User classes go after BS ones
        node['classes'].extend(node_user_classes)
        node['classes'] += self.options.get('class', [])

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


def setup(app):
    app.add_directive('row', PageRow)
    app.add_directive('column', PageColumn)
