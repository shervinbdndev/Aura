"""
URL configuration for aura project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings as DEFAULT_SETTINGS

from error.views import Error400View, Error403View, Error404View, Error500View

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='',
        view=include('clickit.urls'),
        name='clickit-app',
    ),
    path(
        route='account/',
        view=include('account.urls'),
        name='account-app',
    ),
    # path(
    #     route='err_400/',
    #     view=Error400View.as_view(),
    #     name='e400',
    # ),
    # path(
    #     route='err_403/',
    #     view=Error403View.as_view(),
    #     name='e403',
    # ),
    # path(
    #     route='err_404/',
    #     view=Error404View.as_view(),
    #     name='e404',
    # ),
    # path(
    #     route='err_500/',
    #     view=Error500View.as_view(),
    #     name='e500',
    # ),
]

if (not DEFAULT_SETTINGS.DEBUG):
    urlpatterns += static(DEFAULT_SETTINGS.STATIC_URL, document_root=DEFAULT_SETTINGS.STATIC_ROOT)

handler400 = Error400View.as_view()
handler403 = Error403View.as_view()
handler404 = Error404View.as_view()
handler500 = Error500View.as_view()