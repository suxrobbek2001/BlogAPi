from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Maqola, Rasm
from .serializers import MaqolaSerializer, RasmSerializer


class MaqolaListCreateAPIView(ListCreateAPIView):
    #queryset = Maqola.objects.all()
    serializer_class = MaqolaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        maqola = Maqola.objects.filter(user=self.request.user)
        return maqola


###### 2-usul ############################################################################################
class RUDMaqola(RetrieveUpdateDestroyAPIView):
    serializer_class = MaqolaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        maqola = Maqola.objects.filter(user=self.request.user)
        return maqola

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer


