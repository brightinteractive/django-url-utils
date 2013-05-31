# -*- coding: utf-8 -*-
# (c) 2013 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
from urlparse import urlparse, urlunparse
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def current_url_with_params(context, **kwargs):
    """
    Replaces or creates parameters in a query string.

    See tests for example usage.
    """
    request = context['request']
    full_path = request.get_full_path()
    url_parts = list(urlparse(full_path))

    query = request.GET.copy()

    for (name, value) in kwargs.items():
        query[name] = value

    query_part_index = 4
    url_parts[query_part_index] = query.urlencode()

    return urlunparse(url_parts)
