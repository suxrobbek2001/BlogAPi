from django.contrib import admin
from django.urls import path

from blogrestapp.views import MaqolaListCreateAPIView
    #RUDMaqola,
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MaqolaListCreateAPIView.as_view()),

    # path('blog/<int:pk>', RUDMaqola.as_view()),

    path('get-token/', obtain_auth_token),
]
