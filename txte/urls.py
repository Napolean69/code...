from django.urls import path
from .views import txteListCreateView, txteDetailView

urlpatterns = [
    path('txte/', txteListCreateView.as_view(), name='txte-list-create'),
    path('txte/<int:pk>/', txteDetailView.as_view(), name='txte-detail'),
]
