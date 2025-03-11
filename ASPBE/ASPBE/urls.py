from django.contrib import admin
from django.urls import path, include
from UserMainMenu.views import pageNotFound
from ASPBE import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('UserMainMenu.urls')),
    path('holding/', include('HoldingMainMenu.urls')),
    path('', include('registration.urls')),
    path('', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound


