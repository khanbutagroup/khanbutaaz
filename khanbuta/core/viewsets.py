from rest_framework import viewsets
from rest_framework.response import Response
from .models import Slider, Service, Category, Portfolio, Tag, Blog, ContactUs
from .serializers import SliderSerializer, ServiceSerializer, CategorySerializer, PortfolioSerializer, TagSerializer, BlogSerializer, ContactUsSerializer
from django.shortcuts import get_object_or_404


class SliderViewSet(viewsets.ViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

    def list(self, request):
        self.queryset = Slider.objects.all()
        serializers_class = SliderSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        slider = get_object_or_404(self.queryset, slug=pk)
        serializers_class = SliderSerializer(slider)
        return Response(serializers_class.data)


class ServiceViewSet(viewsets.ViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def list(self, request):
        self.queryset = Service.objects.all()
        serializers_class = ServiceSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        service = get_object_or_404(self.queryset, slug=pk)
        serializers_class = ServiceSerializer(service)
        return Response(serializers_class.data)


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        self.queryset = Category.objects.all()
        serializers_class = CategorySerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(self.queryset, slug=pk)
        serializers_class = CategorySerializer(category)
        return Response(serializers_class.data)


class PortfolioViewSet(viewsets.ViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def list(self, request):
        self.queryset = Portfolio.objects.all()
        serializers_class = PortfolioSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        portfolio = get_object_or_404(self.queryset, slug=pk)
        serializers_class = PortfolioSerializer(portfolio)
        return Response(serializers_class.data)


class TagViewSet(viewsets.ViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self, request):
        self.queryset = Tag.objects.all()
        serializers_class = TagSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        tag = get_object_or_404(self.queryset, slug=pk)
        serializers_class = TagSerializer(tag)
        return Response(serializers_class.data)


class BlogViewSet(viewsets.ViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request):
        self.queryset = Blog.objects.all()
        serializers_class = BlogSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        blog = get_object_or_404(self.queryset, slug=pk)
        serializers_class = BlogSerializer(blog)
        return Response(serializers_class.data)


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer