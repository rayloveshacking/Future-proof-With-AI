"""
URL configuration for app project.

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
from django.urls import path

from application.views import upload, results, talent, chat_with_gemini

urlpatterns = [
    path('admin/', admin.site.urls),
    path('results/', results, name='results'),
    path('talent/', talent, name='talent'),
    path('chat/', chat_with_gemini, name='chat_with_gemini'), # Add URL pattern for chat
    path('', upload, name='upload'), # Added name='upload' for potential redirects
]
