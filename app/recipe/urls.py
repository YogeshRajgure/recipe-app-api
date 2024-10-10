"""
URL mappings for recipe app
"""

from django.urls import (
    path, include
)

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tagss', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
