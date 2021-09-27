from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index_page, name='index-page'),
    path('login/', views.login_page, name='login-page'),
    path('logout/', views.logout_page, name='logout-page'),

    path('dashboard/categories/', views.category_list, name='category-list'),
    path('dashboard/categories/create/', views.category_create, name='category-create'),
    path('dashboard/categories/<int:pk>/update/', views.category_update, name='category-update'),
    path('dashboard/categories/<int:pk>/delete/', views.category_delete, name='category-delete'),

    path('dashboard/materials/', views.material_list, name='material-list'),
    path('dashboard/materials/create/', views.material_create, name='material-create'),
    path('dashboard/materials/<int:pk>/update/', views.material_update, name='material-update'),
    path('dashboard/materials/<int:pk>/delete/', views.material_delete, name='material-delete'),

    path('dashboard/customers/', views.customer_list, name='customer-list'),
    path('dashboard/customers/create/', views.customer_create, name='customer-create'),
    path('dashboard/customers/<int:pk>/update/', views.customer_update, name='customer-update'),
    path('dashboard/materials/<int:pk>/delete/', views.customer_delete, name='customer-delete'),
]
