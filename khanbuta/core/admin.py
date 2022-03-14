from django.contrib import admin
from .models import Blog, Category, ContactUs, Partner, Portfolio, Service, Slider, SubService, Tag

admin.site.register([Slider, Service, SubService, Blog, Tag, Portfolio, Category, ContactUs, Partner,])