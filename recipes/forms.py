from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient, RecipeStep


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "difficulty",
            "prep_time_in_minutes",
            "cook_time_in_minutes",
            "public",
        ]

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            "amount",
            "item",
        ]


class RecipeStepForm(forms.ModelForm):
    class Meta:
        model = RecipeStep
        fields = ["text"]


class MealPlanForm(forms.Form):
    recipe = forms.ChoiceField(choices=[])


def make_meal_plan_form_for_user(user, data=None):
    form = MealPlanForm(data=data)
    form.fields["recipe"].choices = [
        (recipe.pk, recipe.title) for recipe in user.recipes.order_by("title")
    ]
    return form
