from api import views
from django.contrib import admin
from django.urls import path
from api import views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuinfo/<int:pk>', views.student_detail),
    # path('stuinfo/', views.student_list),
    # path('stucreate/', views.student_create),
    # path('stuapi/', views.student_api),
    path('stuapi/', views.hello_world),
]
