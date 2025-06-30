from django.urls import path
from .views import user_list, update_user, delete_user, logout_view

urlpatterns = [
    path('', user_list, name="user_list"),
    path('update/<int:pk>/', update_user, name="update_user"),
    path('delete/<int:pk>/', delete_user, name="delete_user"),
    path('logout/', logout_view, name="logout"),
]
