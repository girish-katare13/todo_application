from django.urls import path
from .views import TaskListCreate,TaskRetriveUpdateDelete,index

urlpatterns = [
    path('tasks/',TaskListCreate.as_view(),name="task_create"),
    path('tasks/<int:pk>/',TaskRetriveUpdateDelete.as_view(),name="task_retrive_update_delete"),
    path('',index,name='index'),
]
