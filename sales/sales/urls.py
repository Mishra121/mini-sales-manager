from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from django.contrib import admin
from django.urls import path
from app import views
from sales import settings
from django.conf.urls.static import static
from app import views_orders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login', views.login_view),
    path('api/orders/', views_orders.orders),
    path('api/orders/<int:order_id>/', views_orders.order),
    path('', views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
