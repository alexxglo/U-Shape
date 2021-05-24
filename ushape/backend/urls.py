from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views
from backend.views import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('calorie-list/', views.calorielist_list),
    path('calorie-list/<int:pk>/', views.calorielist_detail),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns = format_suffix_patterns(urlpatterns)