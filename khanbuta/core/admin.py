from django.contrib import admin
from .models import Blog, Category, ContactUs, Partner, Portfolio, Service, Slider, SubService, Tag, FooterFields, \
    Numbers, Socials

admin.site.register(
    [Slider, Service, SubService, Blog, Tag, Portfolio, Category, ContactUs, Partner, FooterFields, Numbers, Socials])
