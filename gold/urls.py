from django.urls import path
from . import views



urlpatterns = [
    path('', views.main_view),
    path('make_card/', views.makeCard, name='make_card'),
    path('draw-card/', views.draw_card, name='draw-card'),
]