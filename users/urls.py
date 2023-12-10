from django.urls import path

from users import views

urlpatterns = [
     path('users/register/', views.register_view),
     path('users/login/', views.login_view),
     path('users/logout/', views.logout_view),
     path('users/profile/', views.profile_view),

]
