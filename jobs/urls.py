from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('create/', views.create_job, name='create_job'),
    path('delete/', views.create_job, name='create_job'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('delete/<int:job_id>/', views.delete_job, name='job_delete'),
]
