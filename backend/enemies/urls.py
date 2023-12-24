from django.urls import path
from enemies import views

urlpatterns = [
    path('dragons/', views.DragonList.as_view(), name='dragon-list'),
    path('dragons/<int:pk>/', views.DragonDetail.as_view(), name='dragon-detail'),
    path('weapons/', views.WeaponList.as_view(), name='weapon-list'),
    path('weapons/<int:pk>/', views.WeaponDetail.as_view(), name='weapon-detail'),
    path('goblins/', views.GoblinList.as_view(), name='goblin-list'),   
    path('goblins/<int:pk>/', views.GoblinDetail.as_view(), name='goblin-detail'),
]