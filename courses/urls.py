from django.urls import path
from .views import (
    CourseCreateView,
    CourseDeleteView,
    CourseListView,
    CourseUpdateView,
    CourseView,
    # MyListView,
    # my_fbv,
)

app_name = 'courses'
urlpatterns = [
    # path('', MyListView.as_view(), name='courses-list'),
    path('', CourseListView.as_view(), name='courses-list'),
    # path('', CourseView.as_view(template_name='contact.html'), name='courses-list'),
    # path('', my_fbv, name='courses-list'),
    
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
]

'''app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    path('<int:obj_id>/', product_detail_view, name='product-detail'),
    path('<int:obj_id>/update/', product_update_view, name='product-update'),
    path('<int:obj_id>/delete/', product_delete_view, name='product-delete'),
]'''
