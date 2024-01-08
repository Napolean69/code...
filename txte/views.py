
from rest_framework import generics
from .models import txte, txteDetail
from .serializers import txteSerializer, txteDetailSerializer

class txteListCreateView(generics.ListCreateAPIView):
    queryset = txte.objects.all()
    serializer_class = txteSerializer

class txteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = txteDetail.objects.all()
    serializer_class = txteDetailSerializer
