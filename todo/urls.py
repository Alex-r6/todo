from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('tag/list/',TagsListView.as_view(), name='tag_list'),
    path('tag/create/',TagCreateView.as_view(), name='tag_create'),
    path('tag/update/<int:pk>/', TagUpdateView.as_view(), name='tag_update'),
    path('tag/delete/<int:pk>/', TagDeleteView.as_view(), name='tag_delete'),
]