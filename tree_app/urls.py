from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from tree import views

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    path('', views.tree_list, name='item_list'),
    path(r'^(?P<name>[-\w/]+)/$', views.tree_detail, name='item_detail'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    # urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
