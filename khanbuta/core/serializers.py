from rest_framework import serializers
from .models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'title', 'description', 'button_text', 'button_link', 'image', 'created_at', 'updated_at')


class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = ('id', 'title', 'created_at', 'updated_at')


class ServiceSerializer(serializers.ModelSerializer):
    sub_services = SubServiceSerializer(required=False, many=True)
    class Meta:
        model = Service
        fields = ('id', 'title', 'text', 'image', 'sub_title', 'sub_desc', 'sub_image', 'sub_services', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'created_at', 'updated_at')


class PortfolioSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    class Meta:
        model = Portfolio
        fields = ('id', 'title', 'image', 'category', 'created_at', 'updated_at')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title', 'created_at', 'updated_at')


class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(required=False,  many=True)
    class Meta:
        model = Blog
        fields = ('id', 'title', 'text', 'image', 'tags', 'created_at', 'updated_at')


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('id', 'first_name', 'last_name', 'email', 'number', 'message', 'created_at', 'updated_at')


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('id', 'image', 'created_at', 'updated_at')