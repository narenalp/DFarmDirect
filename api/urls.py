# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"categories", views.CategoryViewSet, "category")
router.register(r"products", views.ProductViewSet, "product")

urlpatterns = [
    path("v1/", include(router.urls)),
    ]
