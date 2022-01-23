from django.urls import path
from .views import (
    ArticleDeleteView,
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),

    # path('', product_list_view, name='product-list'),
    # path('create/', product_create_view, name='product-create'),
    # path('<int:obj_id>/', product_detail_view, name='product-detail'),
    # path('<int:obj_id>/update/', product_update_view, name='product-update'),
    # path('<int:obj_id>/delete/', product_delete_view, name='product-delete'),
]
