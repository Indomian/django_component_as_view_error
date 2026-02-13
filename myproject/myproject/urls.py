"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django_components import ComponentView

from components.test_component.component import MagicComponent
from components.test_on_render_htmx.component import Magic2Component
from .views import index

component = MagicComponent(
    registered_name="test_component"
)


urlpatterns = [
    path('', index),
    path(
        'magic/',
        # ComponentView.as_view(
        #     component=component
        # ),
        MagicComponent.as_view(),
        name="magic_component_name"
    ),
    path(
        'magic2/',
        Magic2Component.as_view(),
        name="magic2_component_name"
    ),
    path("", include("django_components.urls")),
]
