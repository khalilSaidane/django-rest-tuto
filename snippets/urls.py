from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r"^snippets/$", views.snippet_list_api),
    url(r"^snippets/(?P<pk>\d+)$", views.snippet_detail_api),
]
urlpatterns = format_suffix_patterns(urlpatterns)
