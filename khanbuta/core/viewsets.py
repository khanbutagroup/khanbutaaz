from rest_framework import viewsets
from rest_framework.response import Response
from .models import Slider, Service, Category, Portfolio, Tag, Blog, ContactUs, Partner, FooterFields, Numbers, Socials
from .serializers import SliderSerializer, ServiceSerializer, CategorySerializer, PortfolioSerializer, TagSerializer, \
    BlogSerializer, ContactUsSerializer, PartnerSerializer, FooterSerializer, NumbersSerializer, SocialSerializer
from django.shortcuts import get_object_or_404


class SliderViewSet(viewsets.ViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

    def list(self, request):
        self.queryset = Slider.objects.all()
        serializers_class = SliderSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        slider = get_object_or_404(self.queryset, pk=pk)
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
        service = get_object_or_404(self.queryset, pk=pk)
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
        category = get_object_or_404(self.queryset, pk=pk)
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
        portfolio = get_object_or_404(self.queryset, pk=pk)
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
        tag = get_object_or_404(self.queryset, pk=pk)
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
        blog = get_object_or_404(self.queryset, pk=pk)
        serializers_class = BlogSerializer(blog)
        return Response(serializers_class.data)


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class PartnerViewSet(viewsets.ViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

    def list(self, request):
        self.queryset = Partner.objects.all()
        serializers_class = PartnerSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        partner = get_object_or_404(self.queryset, pk=pk)
        serializers_class = PartnerSerializer(partner)
        return Response(serializers_class.data)


class FooterViewSet(viewsets.ViewSet):
    queryset = FooterFields.objects.all()
    serializer_class = FooterSerializer

    def list(self, request):
        self.queryset = FooterFields.objects.all()
        serializers_class = FooterSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        partner = get_object_or_404(self.queryset, pk=pk)
        serializers_class = FooterSerializer(partner)
        return Response(serializers_class.data)


class NumberViewSet(viewsets.ViewSet):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer

    def list(self, request):
        self.queryset = Numbers.objects.all()
        serializers_class = NumbersSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        partner = get_object_or_404(self.queryset, pk=pk)
        serializers_class = NumbersSerializer(partner)
        return Response(serializers_class.data)


class SocialViewSet(viewsets.ViewSet):
    queryset = Socials.objects.all()
    serializer_class = SocialSerializer

    def list(self, request):
        self.queryset = Socials.objects.all()
        serializers_class = SocialSerializer(self.queryset, many=True)
        return Response(serializers_class.data)

    def retrieve(self, request, pk=None):
        partner = get_object_or_404(self.queryset, pk=pk)
        serializers_class = SocialSerializer(partner)
        return Response(serializers_class.data)
