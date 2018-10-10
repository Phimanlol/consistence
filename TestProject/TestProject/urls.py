"""TestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from TestProject.settings import MEDIA_ROOT

from publish.views import PublishViewSet
from pet.views import PetsViewSet
from users.views import UserViewSet

router = DefaultRouter()

router.register(r'publish', PublishViewSet, base_name='publish')
router.register(r'pet', PetsViewSet, base_name='pet')
router.register(r'users', UserViewSet, base_name='users')


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/', obtain_jwt_token),
    url(r'^', include(router.urls)),
    url(r'docs/', include_docs_urls(title="宠物")),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

]
