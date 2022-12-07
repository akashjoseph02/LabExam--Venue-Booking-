from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'venueapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('venue/', views.VenueView, name='venue'),
    path('addvenueItem/', views.addvenueView),
    path('deleteVenueItem/<int:i>/', views.deleteVenueView),
]
