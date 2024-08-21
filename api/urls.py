from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')  # Register the viewset with a basename

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
