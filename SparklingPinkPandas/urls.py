from django.contrib import admin
from django.urls import path,include
from blog import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('gallery/',include('gallery.urls')),
    path('',views.homeView,name='home'),
    path('accounts/',include('accounts.urls')),
    path('events/',include('event.urls'))
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
