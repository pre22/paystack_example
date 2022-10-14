
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("paystack", include(('paystack.urls','paystack'),name='paystack')),
]
