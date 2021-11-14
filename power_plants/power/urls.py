from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from power.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('plant_states', PlantStates, basename='plant_states')
router.register('map', Map, basename='map')
router.register('lib_map', LibMap, basename='lib_map')

urlpatterns = [
    path('', include(router.urls)),
    path('admin_login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
