
"""
URL configuration for homebanking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views as home_template
from cuentas import views as cuentas_template
from clientes import views as clientes_templates
from movimientos import views as movimientos_template
from prestamos import views as prestamos_template
from tarjetas import views as tarjetas_template

urlpatterns = [
    path('', home_template.home_template, name='home'),
    path('cuentas/', cuentas_template.cuentas_templates, name='cuentas'),
    path('clientes/', clientes_templates.register_page, name='clientes'),
    path('lista_clientes/', clientes_templates.clientes_template, name="lista_clientes"),
    path('lista_clientes/<int:customer_id>', clientes_templates.detalle_cliente, name="detalle_cliente"),
    path('movimientos/', movimientos_template.movimientos_template, name='movimientos'),
    path('prestamo/', prestamos_template.prestamos_template, name='prestamos'),
    path('tarjetas/', tarjetas_template.tarjetas_template, name='tarjeta'),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/', include('registration.urls')),
]
