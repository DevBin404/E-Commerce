from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/', views.SelectedCategoryListView.as_view(), name='selected-category'),
]