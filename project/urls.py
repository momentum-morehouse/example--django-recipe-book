"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from recipes import views as recipes_views
from api import views as api_views
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

router = routers.DefaultRouter()
router.register('recipes', api_views.RecipeViewSet, basename='recipe')

urlpatterns = [
    path('', recipes_views.homepage, name="homepage"),
    path('recipes/', recipes_views.recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_pk>/',
         recipes_views.recipe_detail,
         name='recipe_detail'),
    path('recipes/<int:recipe_pk>/edit/',
         recipes_views.edit_recipe,
         name='edit_recipe'),
    path('recipes/<int:recipe_pk>/delete/',
         recipes_views.delete_recipe,
         name='delete_recipe'),
    path('recipes/<int:recipe_pk>/copy/',
         recipes_views.copy_recipe,
         name='copy_recipe'),
    path('recipes/<int:recipe_pk>/favorite/',
         recipes_views.toggle_favorite_recipe,
         name='toggle_favorite_recipe'),
    path('recipes/new/', recipes_views.add_recipe, name='add_recipe'),
    path('recipes/<int:recipe_pk>/add_ingredient/',
         recipes_views.add_ingredient,
         name='add_ingredient'),
    path('recipes/<int:recipe_pk>/add_recipe_step/',
         recipes_views.add_recipe_step,
         name='add_recipe_step'),
    path('recipes/search/',
         recipes_views.search_recipes,
         name='search_recipes'),
    path('recipes/random/',
         recipes_views.show_random_recipe,
         name='random_recipe'),
    path('mealplan/<int:year>/<int:month>/<int:day>/',
         recipes_views.show_meal_plan,
         name='show_meal_plan'),
    path('tags/<str:tag_name>/', recipes_views.view_tag, name='view_tag'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/', include(router.urls)),
    path('api/user_recipes/<str:username>/',
         api_views.UserRecipesView.as_view(),
         name='api_user_recipes'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns