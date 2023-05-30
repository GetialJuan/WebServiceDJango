from django.urls import path, include
from rest_framework import routers
from .api import ProductoView

router = routers.DefaultRouter()
router.register(r'productos', ProductoView, 'productos')

urlpatterns = [
    path('api/', include(router.urls)),
]