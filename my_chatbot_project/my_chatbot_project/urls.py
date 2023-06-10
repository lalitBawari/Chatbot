from django.contrib import admin
from django.urls import path
from chatbot_app.views import chatbot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chatbot, name='chatbot'),
]
