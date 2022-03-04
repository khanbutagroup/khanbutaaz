import email
from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    button_text = models.CharField(max_length=50)
    button_link = models.CharField(max_length=500)
    image = models.ImageField('Image',upload_to='icons/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliderler'


class Service(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField('Image',upload_to='icons/', null=False, blank=False)
    text = models.TextField("Text")
    sub_title = models.CharField(max_length=200)
    sub_desc = models.CharField(max_length=200)
    sub_image = models.ImageField('Image',upload_to='icons/', null=False, blank=False)
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
    image = models.ImageField('Image',upload_to='icons/', null=False, blank=False)
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
    text = models.TextField("Text")
    image = models.ImageField('Image',upload_to='icons/', null=False, blank=False)
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
    message = models.TextField("Message")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Uslar'