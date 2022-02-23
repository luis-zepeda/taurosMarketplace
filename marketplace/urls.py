from email.mime import base
from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from marketplace.products.views import ProductCreateViewSet, ProductUpdateViewSet, ProductViewSet
from .users.views import UserViewSet, UserCreateViewSet

router = DefaultRouter()

### Users ###
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

### Products ###
router.register(r'products', ProductViewSet)
router.register(r'products', ProductCreateViewSet)
router.register(r'products', ProductUpdateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
