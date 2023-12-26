from django.urls import path
from characters import views

urlpatterns = [
    path('', views.CharacterList.as_view()),
    path('<int:pk>/', views.CharacterDetails.as_view()),
    path('lore-entries/', views.LoreEntryList.as_view()),
    path('lore-entries/<int:pk>/', views.LoreEntryDetails.as_view()),

]
