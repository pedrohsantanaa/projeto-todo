from django.urls import path
from tasks.views import taskList


urlpatterns = [
    path('' , taskList, name='task-list'),
]
