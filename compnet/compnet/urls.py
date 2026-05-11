from django.contrib import admin
from django.urls import path, include

import homepage.urls

urlpatterns = [
    path('', include("homepage.urls")),
    path('topic/', include("topics.urls")),
    path('about/', include("about.urls")),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

]
