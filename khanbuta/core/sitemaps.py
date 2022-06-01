from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Portfolio


#
class Static_Sitemap(Sitemap):
    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['products:category-list', 'products:service-list', 'products:portfolio-list', 'products:tag-list',
                'products:blog-list', 'products:contactus-list', 'products:partner-list', ]

    def location(self, item):
        return reverse(item)

# class Portfolio_Sitemap(Sitemap):
#     changefreq = "daily"
#     priority = 0.7
#
#     def items(self):
#         return Portfolio.objects.all()

# def location(self, item):
#     return reverse(item.get_absolute_url)
