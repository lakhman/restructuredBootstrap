#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 - Anil Lakhman - MIT License
# -----------------------------------------------------------------------------
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives.body import Container
from sphinx.environment import NoUri

btn_classes = {
    'toggle': 'dropdown-toggle',
}
size_classes = {
    'xs': 'btn-xs',
    'btn-xs': 'btn-xs',
    'sm': 'btn-sm',
    'btn-sm': 'btn-sm',
    'lg': 'btn-lg',
    'btn-lg': 'btn-lg',
    'block': 'btn-block',
    'active': 'btn-active'
}


class button(nodes.Inline, nodes.Element):
    pass


def visit_button(self, node):
    atts = []

    if 'dropdown-toggle' in node['classes']:
        atts.append('data-toggle="dropdown" aria-haspopup="true"')

    if node['collapse']:
        target = node['collapse'][0]
        atts.append('data-toggle="collapse"')
        atts.append('data-target="#%s" aria-controls="%s"' % (target, target))

    if node['names']:
        atts.append('id="%s"' % " ".join(node['names']))

    if node['onclick']:
        atts.append('onclick="%s"' % node['onclick'])

    if node['onmouseover']:
        atts.append('onmouseover="%s"' % node['onmouseover'])

    if node['onmouseout']:
        atts.append('onmouseout="%s"' % node['onmouseout'])

    if node['modal-target']:
        atts.append('data-toggle="modal"')
        atts.append('data-target="#%s"' % node['modal-target'])

    if node['href']:
        atts.append('role="button"')

        if 'disabled' in node['classes']:
            atts.append('disabled="disabled"')

        if node['target']:
            atts.append('target="%s"' % node['target'])

        if node['href'] == 'void':
            node['href'] = 'javascript:void(0)'

        anchor_atts = (node['href'], " ".join(node['classes']), " ".join(atts))
        anchor = '<a href="%s" class="%s" %s>' % anchor_atts
        self.body.append(anchor)
    else:
        atts.append('type="button"')
        html_classes = ''
        if len(node['classes']):
            html_classes = 'class="%s" ' % " ".join(node['classes'])
        html_properties = " ".join(atts)
        btn = '<button %s%s>' % (html_classes, html_properties)
        self.body.append(btn)


def depart_button(self, node):
    if node['href']:
        self.body.append('</a>\n')
    else:
        self.body.append('</button>\n')


class BaseButton(Directive):
    required_arguments, optional_arguments = 0, 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
        'href': directives.uri,
        'doc': directives.unchanged_required,
        'target': directives.unchanged_required,
        'modal-target': directives.unchanged,
        'collapse': directives.class_option,
        'onclick': directives.unchanged,
        'onmouseover': directives.unchanged,
        'onmouseout': directives.unchanged,
    }

    node_classes = None

    def replace_shortcut_classes(self, node):
        """
        We expand shortcut classes xs => btn-xs, view bs_classes and user_classes
        """
        bs_classes = []
        user_classes = []

        if self.node_classes is not None:
            bs_classes.extend(['btn'])
            bs_classes += self.node_classes

        for i, node_class in enumerate(node.attributes['classes']):
            if node_class in btn_classes:
                bs_classes.append(btn_classes.get(node_class))
                node.attributes['classes'][i] = ''
            elif node_class in size_classes:
                bs_classes.append(size_classes.get(node_class))
                node.attributes['classes'][i] = ''
            else:
                user_classes.append(node_class)

        # Remove user 'btn' class, and add to bs_classes to maintain order
        if 'btn' in user_classes:
            user_classes.remove('btn')

        return bs_classes, user_classes

    def run(self):
        self.assert_has_content()

        node = button()
        node['href'] = self.options.get('href', None)
        node['doc'] = self.options.get('doc', None)
        node['target'] = self.options.get('target', None)
        node['classes'] = self.options.get('class', [])
        node['collapse'] = self.options.get('collapse', [])
        node['onclick'] = self.options.get('onclick', None)
        node['onmouseover'] = self.options.get('onmouseover', None)
        node['onmouseout'] = self.options.get('onmouseout', None)
        node['modal-target'] = self.options.get('modal-target', None)

        bs_classes, user_classes = self.replace_shortcut_classes(node)
        node['classes'] = bs_classes + user_classes

        if 'doc' in self.options:
            # Create a reference
            try:
                env = self.state.document.settings.env
                docname = env.docname
                href = env.app.builder.get_relative_uri(docname, node['doc'])
                node['href'] = href
            except NoUri:  # pragma: no cover
                # ignore if no URI can be determined, e.g. for LaTeX output
                pass

        self.state.nested_parse(self.content, self.content_offset, node)
        self.add_name(node)

        return [node]


class ButtonGroup(Container):
    has_content = True
    option_spec = {
        'name': directives.unchanged,
        'class': directives.class_option,
        'vertical': directives.flag,
    }

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = nodes.container(text, **self.options)
        node['classes'] = []

        if 'vertical' in self.options:
            node['classes'] += ['btn-group-vertical']
        else:
            node['classes'] += ['btn-group']

        node['classes'] += self.options.get('class', [])
        node['html_attributes'] = {
            'role': 'group',
        }

        try:
            if self.arguments:
                node['classes'] += directives.class_option(self.arguments[0])
        except ValueError:
            val_error = 'Invalid class argument for "%s" directive: "%s".'
            raise self.error(val_error % (self.name, " ".join(self.arguments)))

        bs_classes = ['justified', 'xs', 'sm', 'md', 'lg']

        for i, cls in enumerate(node['classes']):
            if cls in bs_classes:
                node['classes'][i] = 'btn-group-%s' % node['classes'][i]

        self.state.nested_parse(self.content, self.content_offset, node)
        self.add_name(node)
        return [node]


class ButtonToolbar(Container):
    has_content = True
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged,
    }

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = nodes.container(text, **self.options)
        node['classes'] = ['btn-toolbar']
        node['classes'] += self.options.get('class', [])
        node['html_attributes'] = {
            'role': 'toolbar',
        }

        if self.arguments:
            node['classes'] += directives.class_option(self.arguments[0])

        self.state.nested_parse(self.content, self.content_offset, node)
        self.add_name(node)

        return [node]


class ButtonPlain(BaseButton):
    node_classes = None


class ButtonDefault(BaseButton):
    node_classes = ['btn-default']


class ButtonPrimary(BaseButton):
    node_classes = ['btn-primary']


class ButtonSuccess(BaseButton):
    node_classes = ['btn-success']


class ButtonInfo(BaseButton):
    node_classes = ['btn-info']


class ButtonWarning(BaseButton):
    node_classes = ['btn-warning']


class ButtonDanger(BaseButton):
    node_classes = ['btn-danger']


class ButtonLink(BaseButton):
    node_classes = ['btn-link']


#
# Extra Small
#


class ButtonXsDefault(BaseButton):
    node_classes = ['btn-default', 'btn-xs']


class ButtonXsPrimary(BaseButton):
    node_classes = ['btn-primary', 'btn-xs']


class ButtonXsSuccess(BaseButton):
    node_classes = ['btn-success', 'btn-xs']


class ButtonXsInfo(BaseButton):
    node_classes = ['btn-info', 'btn-xs']


class ButtonXsWarning(BaseButton):
    node_classes = ['btn-warning', 'btn-xs']


class ButtonXsDanger(BaseButton):
    node_classes = ['btn-danger', 'btn-xs']


class ButtonXsLink(BaseButton):
    node_classes = ['btn-link', 'btn-xs']


#
# Small
#


class ButtonSmDefault(BaseButton):
    node_classes = ['btn-default', 'btn-sm']


class ButtonSmPrimary(BaseButton):
    node_classes = ['btn-primary', 'btn-sm']


class ButtonSmSuccess(BaseButton):
    node_classes = ['btn-success', 'btn-sm']


class ButtonSmInfo(BaseButton):
    node_classes = ['btn-info', 'btn-sm']


class ButtonSmWarning(BaseButton):
    node_classes = ['btn-warning', 'btn-sm']


class ButtonSmDanger(BaseButton):
    node_classes = ['btn-danger', 'btn-sm']


class ButtonSmLink(BaseButton):
    node_classes = ['btn-link', 'btn-sm']


#
# Large
#


class ButtonLgDefault(BaseButton):
    node_classes = ['btn-default', 'btn-lg']


class ButtonLgPrimary(BaseButton):
    node_classes = ['btn-primary', 'btn-lg']


class ButtonLgSuccess(BaseButton):
    node_classes = ['btn-success', 'btn-lg']


class ButtonLgInfo(BaseButton):
    node_classes = ['btn-info', 'btn-lg']


class ButtonLgWarning(BaseButton):
    node_classes = ['btn-warning', 'btn-lg']


class ButtonLgDanger(BaseButton):
    node_classes = ['btn-danger', 'btn-lg']


class ButtonLgLink(BaseButton):
    node_classes = ['btn-link', 'btn-lg']


def setup(app):
    app.add_node(button, html=(visit_button, depart_button))

    app.add_directive('button-group', ButtonGroup)
    app.add_directive('button-toolbar', ButtonToolbar)

    app.add_directive('button', ButtonDefault)
    app.add_directive('button-plain', ButtonPlain)
    app.add_directive('button-primary', ButtonPrimary)
    app.add_directive('button-success', ButtonSuccess)
    app.add_directive('button-info', ButtonInfo)
    app.add_directive('button-warning', ButtonWarning)
    app.add_directive('button-danger', ButtonDanger)
    app.add_directive('button-link', ButtonLink)

    # https://getbootstrap.com/docs/3.3/css/#buttons-sizes
    # xs, sm, lg (md = default)
    app.add_directive('button-xs', ButtonXsDefault)
    app.add_directive('button-xs-primary', ButtonXsPrimary)
    app.add_directive('button-xs-success', ButtonXsSuccess)
    app.add_directive('button-xs-info', ButtonXsInfo)
    app.add_directive('button-xs-warning', ButtonXsWarning)
    app.add_directive('button-xs-danger', ButtonXsDanger)
    app.add_directive('button-xs-link', ButtonXsLink)

    app.add_directive('button-sm', ButtonSmDefault)
    app.add_directive('button-sm-primary', ButtonSmPrimary)
    app.add_directive('button-sm-success', ButtonSmSuccess)
    app.add_directive('button-sm-info', ButtonSmInfo)
    app.add_directive('button-sm-warning', ButtonSmWarning)
    app.add_directive('button-sm-danger', ButtonSmDanger)
    app.add_directive('button-sm-link', ButtonSmLink)

    app.add_directive('button-lg', ButtonLgDefault)
    app.add_directive('button-lg-primary', ButtonLgPrimary)
    app.add_directive('button-lg-success', ButtonLgSuccess)
    app.add_directive('button-lg-info', ButtonLgInfo)
    app.add_directive('button-lg-warning', ButtonLgWarning)
    app.add_directive('button-lg-danger', ButtonLgDanger)
    app.add_directive('button-lg-link', ButtonLgLink)
