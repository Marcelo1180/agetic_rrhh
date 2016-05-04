"""agetic_rrhh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from control_personal import views
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'horarios', views.HorarioViewSet)
router.register(r'horario_rangos', views.HorarioRangoViewSet)
router.register(r'designacion_horarios', views.DesignacionHorarioViewSet)
router.register(r'registro_horarios', views.RegistroHorarioViewSet)
router.register(r'feriados', views.FeriadoViewSet)
router.register(r'tipo_permisos', views.TipoPermisoViewSet)
router.register(r'designacion_permisos', views.DesignacionPermisoViewSet)

urlpatterns = [
    url(r'^api/v2/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^home/', views.home),
    url(r'^confirmar/permiso/$', views.confirmar_permiso),
]
