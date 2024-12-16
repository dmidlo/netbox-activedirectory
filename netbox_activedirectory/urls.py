from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("active-directorys/", views.ActiveDirectoryListView.as_view(), name="activedirectory_list"),
    path("active-directorys/add/", views.ActiveDirectoryEditView.as_view(), name="activedirectory_add"),
    path("active-directorys/<int:pk>/", views.ActiveDirectoryView.as_view(), name="activedirectory"),
    path("active-directorys/<int:pk>/edit/", views.ActiveDirectoryEditView.as_view(), name="activedirectory_edit"),
    path("active-directorys/<int:pk>/delete/", views.ActiveDirectoryDeleteView.as_view(), name="activedirectory_delete"),
    path(
        "active-directorys/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="activedirectory_changelog",
        kwargs={"model": models.ActiveDirectory},
    ),
)
