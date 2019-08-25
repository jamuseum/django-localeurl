from localeurl.views import change_locale


from django.conf.urls import url

urlpatterns = (
    url(r'^change/', change_locale, name='localeurl_change_locale'),
)
