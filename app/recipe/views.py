from django.shortcuts import render

# Create your views here.
from rest_framework import (viewsets, mixins,)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (Recipe, Tag, Ingredient)
from recipe import serializers


class BaseRecipeAttrViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet, mixins.DestroyModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')


class IngredientViewSet(BaseRecipeAttrViewSet):
    """ Manage ingredients in the database """
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()


class RecipeViewSet(viewsets.ModelViewSet):
    #serializer_class = serializers.RecipeDetailSerializer
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_class = [IsAuthenticated]

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        ingredients = self.request.query_params.get('ingredients')
        queryset = self.queryset
        
        if ingredients:
            ingredient_ids = self._params_to_ints(ingredients)
            queryset = queryset.filter(ingredients__id__in = ingredient_ids)

        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RecipeSerializer 

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    """ Manage tags in the database """
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    
