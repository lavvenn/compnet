from django.contrib import admin
from django.urls import path, include

import homepage.urls

urlpatterns = [
    path('', include("homepage.urls")),
    path('admin/', admin.site.urls),

]
