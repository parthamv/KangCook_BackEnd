from rest_framework import viewsets
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.filters import SearchFilter  # Import SearchFilter


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()  # Ensure this line is present
    serializer_class = RecipeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description', 'ingredients']

    def get_queryset(self):
        queryset = Recipe.objects.all()
        query = self.request.query_params.get('search')
        if query:
            queryset = queryset.filter(
                name__icontains=query
            ) | queryset.filter(
                description__icontains=query
            ) | queryset.filter(
                ingredients__icontains=query
            )
        return queryset