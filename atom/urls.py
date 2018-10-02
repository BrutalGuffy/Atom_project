"""atom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import debug_toolbar
from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from hobby import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:pk>/', views.board_events, name='events'),
    path('boards/<int:pk>/events/<int:event_pk>/', views.event_detail, name='event_detail'),
    path('admin/', admin.site.urls),
    path('signup/', accounts_views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('add_like/', views.add_like, name='add_like'),
    path('add_like_comment/', views.add_like_comment, name='add_like_comment'),
    path('boards/<int:pk>/events/<int:event_pk>/more_comments/', views.more_comments, name='more_comments'),
    path('__debug__/', include(debug_toolbar.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
