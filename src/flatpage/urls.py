from django.conf.urls import patterns

urlpatterns = patterns(
    'flatpage.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
