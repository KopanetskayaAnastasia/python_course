from django.urls import path
from . import views

urlpatterns = [
    path('', views.workers_home, name='workers_home'),
    path('add', views.add, name='add'),
    path('<int:pk>', views.WorkerDetailView.as_view(), name='worker-detail'),
    path('<int:pk>/update', views.WorkerUpdateView.as_view(), name='worker-update')
]
