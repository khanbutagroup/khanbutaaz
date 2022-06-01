from ckeditor.fields import RichTextField
from django.db import models
# from django.utils.translation import gettext_lazy as _
# from parler.models import models.Model, TranslatedFields
from django.urls import reverse


class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    button_text = models.CharField(max_length=50)
    button_link = models.CharField(max_length=500)
    image = models.ImageField('Image', upload_to='icons/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliderler'


class Service(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextField(null=True, blank=True)
    button_text = models.CharField(max_length=50)
    button_link = models.CharField(max_length=500)
    sub_title = models.CharField(max_length=200)
    sub_desc = models.CharField(max_length=200)
    image = models.ImageField('Image', upload_to='icons/', null=False, blank=False)
    sub_image = models.ImageField('Image', upload_to='icons/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Servis'
        verbose_name_plural = 'Servisler'


class SubService(models.Model):
    title = models.CharField(max_length=200)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='sub_services', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sub Servis'
        verbose_name_plural = 'Sub Servisler'


class Category(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField('Image', upload_to='icons/', null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='portfolios', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfoliolar'


class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextField()
    image = models.ImageField('Image', upload_to='icons/', null=False, blank=False)
    tags = models.ManyToManyField('Tag', db_index=True, related_name='blogs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'


class Tag(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Taglar'


class ContactUs(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(('email adress'), null=False, blank=False)
    number = models.CharField(max_length=50)
    message = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Uslar'


class Partner(models.Model):
    image = models.ImageField('Image', upload_to='icons/', null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Partnyor'
        verbose_name_plural = 'Partnyorlar'


class FooterFields(models.Model):
    location = models.TextField()
    email = models.CharField(max_length=255)
    about_text = models.TextField()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'


class Numbers(models.Model):
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.phone}'


class Socials(models.Model):
    icon = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=555)

    def __str__(self):
        return f'{self.name}'
