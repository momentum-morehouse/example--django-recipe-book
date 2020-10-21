from django import forms
from django.forms.widgets import Input
from .models import Recipe, Ingredient, RecipeStep

class RangeInput(Input):
    input_type = 'range'
    template_name = 'django/forms/widgets/input.html'

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
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'w-100 pa1',
                'placeholder': "Grandma's Snoopy Salad",
            }),
            "difficulty": forms.Select(attrs={'class': 'w-100 pa1'}),
            "prep_time_in_minutes": RangeInput(attrs={'min': 5, 'max': 120, 'step': 5}),
            "cook_time_in_minutes": forms.NumberInput(attrs={'class': 'w-100 pa1'}),
        }

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
