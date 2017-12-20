# -*- coding: utf-8 -*-
from .BaseTest import BaseTest


class MediaTest(BaseTest):
    def test_media(self):
        """
        Test a simple media
        """
        self.do_component_fixture_test('media', 'media')

    def test_media_arg_class(self):
        """
        Test class via argument
        """
        self.do_component_fixture_test('media', 'media-arg-class')

    def test_media_body(self):
        """
        Test a media object with a media-body
        """
        self.do_component_fixture_test('media', 'media-body')

    def test_media_heading(self):
        """
        Test a media-heading class is applied
        """
        self.do_component_fixture_test('media', 'media-heading')

    def test_media_heading_link(self):
        """
        Test a media-heading class is applied with a link
        """
        self.do_component_fixture_test('media', 'media-heading-link')

    def test_media_heading_inline(self):
        """
        Test our heading is parsed (so we can use icons)
        """
        self.do_component_fixture_test('media', 'media-heading-inliner')

    def test_media_heading_page_header(self):
        """
        Test our media :page-header: flag
        """
        self.do_component_fixture_test('media', 'media-heading-page-header')

    def test_media_left_arg(self):
        """
        Test a media left object with a class argument
        """
        self.do_component_fixture_test('media', 'media-left-class-arg')

    def test_media_left_arg_error(self):
        """
        Test a media left object with an invalid class argument
        """
        self.do_component_fixture_test('media', 'media-left-class-arg-error')

    def test_media_left_image(self):
        """
        Test a media object with a media-body and media-left image
        """
        self.do_component_fixture_test('media', 'media-left-image')

    def test_media_right_image(self):
        """
        Test a media object with a media-body and media-right image
        """
        self.do_component_fixture_test('media', 'media-right-image')

    def test_media_right_image_no_target(self):
        """
        Test media-object class is applied direct image children
        """
        self.do_component_fixture_test('media', 'media-right-image-no-target')

    def test_media_list(self):
        """
        Test media list is returned as a ul
        """
        self.do_component_fixture_test('media', 'media-list')

    def test_media_list_arg_class(self):
        """
        Test user classes can be applied to media list via arguments
        """
        self.do_component_fixture_test('media', 'media-list-arg-class')
