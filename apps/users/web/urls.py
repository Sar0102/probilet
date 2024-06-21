from django.urls import path

from apps.users.web.login.views import TokenObtainPairView, TokenRefreshView
from apps.users.web.registration.views import CreateListUserView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/", CreateListUserView.as_view(), name="user"),
]
