# -*- coding: utf-8 -*-
# (c) 2013 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
from django.utils.unittest import TestCase
from django.test.client import RequestFactory
from url_utils.templatetags.url_utils import current_url_with_params


class CurrentUrlWithParamsTests(TestCase):
    def test_page_argument_is_added_to_query_string(self):
        context = self._create_context_with_request('/test/url?arg1=1&arg2=2')

        url = current_url_with_params(context, page='xyz')

        self.assertEqual('/test/url?arg1=1&arg2=2&page=xyz', url)

    def test_argument_overwrites_existing(self):
        context = self._create_context_with_request('/test/url?arg1=1&arg2=2')

        url = current_url_with_params(context, arg2='new')

        self.assertEqual('/test/url?arg1=1&arg2=new', url)

    def test_show_argument_is_added_to_query_string(self):
        context = self._create_context_with_request('/test/url?arg1=1&arg2=2')

        url = current_url_with_params(context, show=20)

        self.assertEqual('/test/url?arg1=1&arg2=2&show=20', url)

    def test_with_no_page_number_original_url_is_returned(self):
        context = self._create_context_with_request('/test/url?arg1=1&arg2=2')

        url = current_url_with_params(context)

        self.assertEqual('/test/url?arg1=1&arg2=2', url)

    def _create_context_with_request(self, path):
        request_factory = RequestFactory()
        request = request_factory.get(path)

        return {'request': request}
