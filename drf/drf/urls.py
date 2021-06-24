from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/api-token-auth/', obtain_auth_token),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
