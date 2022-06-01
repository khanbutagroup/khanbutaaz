from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import *

app_name = "products"

router = DefaultRouter()

router.register('sliders', SliderViewSet, basename='slider')
router.register('services', ServiceViewSet, basename='service')
router.register('categories', CategoryViewSet, basename='category')
router.register('portfolios', PortfolioViewSet, basename='portfolio')
router.register('tags', TagViewSet, basename='tag')
router.register('blogs', BlogViewSet, basename='blog')
router.register('contactus', ContactUsViewSet, basename='contactus')
router.register('partners', PartnerViewSet, basename='partner')
router.register('footers', FooterViewSet, basename='footer')
router.register('numbers', NumberViewSet, basename='number')
router.register('socials', SocialViewSet, basename='social')
router.register('partners', PartnerViewSet, basename='partner')

urlpatterns = [
    path('', include(router.urls)),
]