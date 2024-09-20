from api import views
from django.contrib import admin
from django.urls import path
from api import views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/', views.student_api),
]
