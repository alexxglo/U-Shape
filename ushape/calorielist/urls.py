from django.urls import path
from calorielist import views

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from calorielist import views

urlpatterns = [
    path('calorielist/', views.calorielist_list),
    path('calorielist/<int:pk>/', views.calorielist_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)