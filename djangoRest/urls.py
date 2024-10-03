from api import views
from django.contrib import admin
from django.urls import path
from api import views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentListCreate.as_view()), #change the method name for different methods that do not require primary key
    path('studentapi/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()), #change the method name for different methods that require primary key
]
