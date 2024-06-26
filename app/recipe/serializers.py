from rest_framework import serializers

from core.models import (Recipe, Tag, Ingredient)


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ['id']
        

class RecipeSerializer(serializers.ModelSerializer):
    #tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'time_minutes', 'price', 'link', 'ingredients')
        read_only_fields = ('id',)

    def _get_or_create_ingredients(self, ingredients, recipe):
        auth_user = self.context['request'].user
        for ingredient in ingredients:
            ingredient_obj, created = Ingredient.objects.get_or_create(
                user = auth_user,
                **ingredient
            )
            recipe.ingredients.add(ingredient_obj)

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_ingredients(ingredients, recipe)
        
        return recipe
    
    def update(self, instance, validated_data):
        ingredients = validated_data.pop('ingredients', None)
        if ingredients is not None:
            instance.ingredients.clear()
            self._get_or_create_ingredients(ingredients, instance)
            
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        return 


"""
class RecipeDetailSerializer(RecipeSerializer):

    class Meta:
        fields = RecipeSerializer.Meta.fields + ['description']
"""