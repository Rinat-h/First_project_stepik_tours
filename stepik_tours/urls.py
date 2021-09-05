"""stepik_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
import tours.views as t_views

handler500 = t_views.custom_handler500

urlpatterns = [
    path('', t_views.main_view, name='main_view'),
    path('departure/<str:departure>/', t_views.departure_view, name='departure_link'),
    path('tour/<int:tour_id>/', t_views.tour_view, name='tour_link'),
]
