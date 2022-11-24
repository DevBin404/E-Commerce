from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    # path('category/<int:pk>/', views.SelectedCategoryListView.as_view(), name='selected-category'), 
    # path('category/<slug:slug>/', views.SelectedCategoryListView.as_view(), name='selected-category'),
    re_path(r'category/(?P<slug>[-\w]+)/', views.SelectedCategoryListView.as_view(), name='selected-category'),
    re_path(r'products/(?P<slug>[-\w]+)/', views.ProductDetailListView.as_view(), name='product-detail'),
]