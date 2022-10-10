from django.urls import path 
from products import views 
 
urlpatterns = [ 
    path('api/products', views.products_list),
    path('api/products/<int:id>', views.product_detail)
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]