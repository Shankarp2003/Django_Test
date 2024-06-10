from django.urls import path
from .views import (
    ClientListCreateView,
    ClientRetrieveUpdateDestroyView,
    ProjectCreateView,
    AssignedProjectsView
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-retrieve-update-destroy'),
    path('clients/<int:pk>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/', AssignedProjectsView.as_view(), name='assigned-projects'),
]
