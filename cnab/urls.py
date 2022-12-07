from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r"^parser/(?P<filename>[^/]+)/$",
            views.UploadView.as_view()),
    path("report/<str:name_company>/", views.ListView.as_view()),
]
