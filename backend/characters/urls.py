from django.urls import path
from characters import views

urlpatterns = [
    path('', views.CharacterList.as_view()),
    path('<int:pk>/', views.CharacterDetails.as_view()),
    path('lore-entries/', views.LoreEntryList.as_view()),
    path('lore-entries/<int:pk>/', views.LoreEntryDetails.as_view()),
    path('items/', views.ItemList.as_view()),
    path('items/<int:pk>/', views.ItemDetails.as_view()),
    path('statistics/', views.StatisticsList.as_view()),
    path('statistics/<int:pk>/', views.StatisticsDetails.as_view()),
    path('habilities/', views.HabilitiesList.as_view()),
    path('habilities/<int:pk>/', views.HabilitiesDetails.as_view()),    
]
