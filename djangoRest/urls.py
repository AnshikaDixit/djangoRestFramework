from api import views
from django.contrib import admin
from django.urls import path
from api import views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.LCStudentAPI.as_view()),
    path('studentapi/<int:pk>', views.StudentDestroy.as_view()),
    # path('studentapi/<int:pk>', views.StudentUpdate.as_view()),
]
