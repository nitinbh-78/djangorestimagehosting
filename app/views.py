from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import action
from app.models import Account, ThumbnailSize, Plan, Image, Thumbnail, TemporalLink
from app.serializers import AccountSerializer, ThumbnailSizeSerializer, PlanSerializer
from app.serializers import ImageSerializer, ThumbnailSerializer, TemporalLinkSerializer
from app.authorcheck import IsAuthor

class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAdminUser]

class PlanView(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAdminUser]

class ImageView(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        author=Account.objects.get(user=self.request.user)
        return Image.objects.filter(author=author)

    @action(detail=True)
    def perform_create(self, serializer):
        author=Account.objects.get(user=self.request.user)
        serializer.save(author=author)
    

class ThumbnailView(viewsets.ModelViewSet):
    serializer_class = ThumbnailSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        author=Account.objects.filter(user=self.request.user)[:1].get()
        return Thumbnail.objects.filter(author=author)

    @action(detail=True)
    def perform_create(self, serializer):
        author=Account.objects.filter(user=self.request.user)[:1].get()
        serializer.save(author=author)

class TemporalLinkView(viewsets.ModelViewSet):
    queryset = TemporalLink.objects.all()
    serializer_class = TemporalLinkSerializer
    permission_classes = [IsAuthor]

