from django.urls import include, path

app_name = "web"

urlpatterns = [
    path("<version>/users/", include("apps.users.web.urls")),
]
