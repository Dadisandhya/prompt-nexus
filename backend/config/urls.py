from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('prompts/', views.get_prompts),
    path('prompts/create/', views.create_prompt),
    path('prompts/<uuid:id>/', views.get_prompt),
]
