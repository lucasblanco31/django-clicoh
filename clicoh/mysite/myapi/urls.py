from django.urls import include, path
from rest_framework import routers
from . import views
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'orderdetail', views.OrderDetailViewSet)
router.register(r'order', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

