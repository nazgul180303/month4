from django.urls import path

from post import views

urlpatterns = [
    path('product/', views.products_view),
    path('product/<int:id>', views.product_detail),
    path('category/', views.category_view),
    path('category/create', views.category_create),
    path('', views.main_view),
    path('product/create/', views.product_create),
    #path('current_date/', views.current_date),
    #path('goodby/',views.goodby) ,
    #path('islam/',views.islam),
]