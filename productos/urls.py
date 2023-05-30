from django.urls import path, include
from rest_framework import routers
from .api.api import ProductoView

from .api.api import ProductoApiView

router = routers.DefaultRouter()
router.register(r'productos', ProductoView)

urlpatterns = [
    path('', include(router.urls)),
    path('miapi', ProductoApiView.as_view()),
]