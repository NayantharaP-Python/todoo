from . import views
from django.urls import path

urlpatterns = [
    path('', views.add, name='add'),
    path('delete<int:taskid>/', views.delete, name='delete'),
    path('update<int:id>/', views.update, name='update'),
    path('home/', views.Tasklistview.as_view(), name='home'),
    path('details/<int:pk>/', views.TaskDetailview.as_view(), name='details'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cbvdelete'),

]
