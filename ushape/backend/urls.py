from django.urls import path
from backend import views

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('calorie-list/', views.calorielist_list),
    path('calorie-list/<int:pk>/', views.calorielist_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)