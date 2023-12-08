from django.urls import path
from . import views


urlpatterns = [
    path('', views.TemplateProducts.as_view(), name='products'),
    path('<int:product_id>/', views.TemplateInfoAboutProduct.as_view(), name='product_info'),
]
