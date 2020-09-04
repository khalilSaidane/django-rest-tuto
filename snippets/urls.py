from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r"^snippets/$", views.SnippetList.as_view()),
    url(r"^snippets/(?P<pk>\d+)$", views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r"^users/$", views.UserList.as_view()),
    url(r"^users/(?P<pk>\d+)$", views.UserDetail.as_view()),
    url(r"^snippets/(?P<pk>\d+)/highlight$", views.SnippetHighlight.as_view(), name="snippet-highlight"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
