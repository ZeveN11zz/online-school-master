"""
URL configuration for djangoShop project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from shop import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="index"),
    path("course/<slug:slug>/", views.ProductDetailView.as_view(), name="product"),
    path("course/<slug:slug>/add/", views.EditCartView.as_view(), name="add_to_cart"),
    path("orders/", views.OrdersView.as_view(), name="orders"),
    path("orders/<int:pk>/", views.OrderDetailView.as_view(), name="order"),
    path("reclamation/", views.ReclamationView.as_view(), name="reclamation"),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("cart/<slug:slug>/update/", views.EditCartView.as_view(), name="cart_update"),
    path("payment/", views.PaymentView.as_view(), name="payment"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("orders/<int:order>/dispute/", views.DisputeCreateView.as_view(), name="dispute_create"),
    path("dispute/<int:pk>/update/", views.DisputeUpdateView.as_view(), name="dispute_update"),
    path("dispute/<int:pk>/", views.DisputeDetailView.as_view(), name="dispute_detail"),
    path("schedule/", views.ScheduleList.as_view(), name="schedule_list"),
    path("schedule/<int:pk>/", views.ScheduleBookingView.as_view(), name="schedule_booking"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
] + [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
