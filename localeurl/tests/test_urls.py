"""
URLconf for testing.
"""

from django.conf.urls import url


def dummy(request, test='test'):
    pass


urlpatterns = [
     url(r'^dummy/$', dummy, name='dummy0'),
     url(r'^dummy/(?P<test>.+)$', dummy, name='dummy1'),
]

