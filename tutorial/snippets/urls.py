from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
# добавили новые представления в API, настроив их URL-маршруты.
urlpatterns = [
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view()),
    path("users/", views.UserList.as_view()),  # new
    path("users/<int:pk>/", views.UserDetail.as_view()),  # new
]

urlpatterns = format_suffix_patterns(urlpatterns)

