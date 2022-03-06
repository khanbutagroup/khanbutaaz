from statistics import mode
from unicodedata import category
from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import *


class SliderSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Slider)
    class Meta:
        model = Slider
        fields = ('id', 'translations', 'image', 'created_at', 'updated_at')


class SubServiceSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=SubService)
    class Meta:
        model = SubService
        fields = ('id', 'translations', 'created_at', 'updated_at')


class ServiceSerializer(TranslatableModelSerializer):
    sub_services = SubServiceSerializer(required=False, many=True)
    translations = TranslatedFieldsField(shared_model=Service)
    class Meta:
        model = Service
        fields = ('id', 'translations', 'sub_image', 'sub_services', 'created_at', 'updated_at')


class CategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)
    class Meta:
        model = Category
        fields = ('id', 'translations', 'created_at', 'updated_at')


class PortfolioSerializer(TranslatableModelSerializer):
    category = CategorySerializer(required=False)
    translations = TranslatedFieldsField(shared_model=Portfolio)
    class Meta:
        model = Portfolio
        fields = ('id', 'translations', 'image', 'category', 'created_at', 'updated_at')


class TagSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Tag)
    class Meta:
        model = Tag
        fields = ('id', 'translations', 'created_at', 'updated_at')


class BlogSerializer(TranslatableModelSerializer):
    tags = TagSerializer(required=False,  many=True)
    translations = TranslatedFieldsField(shared_model=Blog)
    class Meta:
        model = Blog
        fields = ('id', 'translations', 'tags', 'created_at', 'updated_at')


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('id', 'first_name', 'last_name', 'email', 'number', 'message', 'created_at', 'updated_at')