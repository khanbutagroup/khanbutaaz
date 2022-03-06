from django.contrib import admin
from .models import Blog, Category, ContactUs, Portfolio, Service, Slider, SubService, Tag
from parler.admin import TranslatableAdmin

class SliderAdmin(TranslatableAdmin):
    list_display = ('title', 'description', 'button_text', 'button_link')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'button_text', 'button_link'),
        }),
    )


class SubServiceAdmin(TranslatableAdmin):
    list_display = ('title', 'service',)
    fieldsets = (
        (None, {
            'fields': ('title', 'service',),
        }),
    )


class ServiceAdmin(TranslatableAdmin):
    list_display = ('title', 'text', 'button_text', 'button_link', 'sub_title', 'sub_desc',)
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'button_text', 'button_link', 'sub_title', 'sub_desc',),
        }),
    )


class BlogAdmin(TranslatableAdmin):
    list_display = ('title', 'text')
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'image', 'tags'),
        }),
    )


class TagAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title',),
        }),
    )


class TagAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title',),
        }),
    )


class PortfolioAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'category'),
        }),
    )


class CategoryAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title',),
        }),
    )


admin.site.register(Slider, SliderAdmin)
admin.site.register(SubService, SubServiceAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register([ContactUs,])

