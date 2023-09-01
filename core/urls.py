from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions 
from dashboard.views import *

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework_simplejwt.views import TokenVerifyView
    
router = DefaultRouter()
router.register(r'offer', OfferViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Phone Pro ",
        default_version = "v1",
        description= "Phone Project",
        terms_of_service= 'http://www.google.com/policies/terms/',
        contact = openapi.Contact( email = 'asliddin.otabekov@gmail.com'),
        license= openapi.License(name = "well license")
    ),
    public= True,
    permission_classes= (permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/',schema_view.with_ui(
        'swagger',cache_timeout=0),name= 'schema-swager-ui'),
    path('redoc/',schema_view.with_ui(
        'redoc',cache_timeout=0),name= 'schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]






