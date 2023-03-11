import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *



class AutoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AutoModels
        fields = ('vendor', 'slug', 'vendor_code', 'user')

# class AutoSerializer(serializers.Serializer):
#     vendor = serializers.CharField(max_length=100)
#     vendor_code = serializers.CharField(max_length=100)
#     group = serializers.CharField(max_length=100)
#     subgroup = serializers.CharField(max_length=100)
#     auto_model = serializers.CharField(max_length=100)
#     photo = serializers.CharField(max_length=100)
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     slug = serializers.SlugField()
#
#     def create(self, validated_data):
#         return AutoModels.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.vendor = validated_data.get('vendor', instance.vendor)
#         instance.vendor_code = validated_data.get('vendor_code', instance.vendor_code)
#         instance.group = validated_data.get('group', instance.group)
#         instance.subgroup = validated_data.get('subgroup', instance.subgroup)
#         instance.auto_model = validated_data.get('auto_model', instance.auto_model)
#         instance.photo = validated_data.get('photo', instance.photo)
#         instance.time_create = validated_data.get('time_create', instance.time_create)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.save()
#         return instance



# class Auto:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#
# class AutoSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
# def encode():
#     model = Auto('Toyota', 'Ремни ГРМ')
#     model_sr = AutoSerializer(model)
#     print(model_sr.data)
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Toyota","content":"remni grm"}')
#     data = JSONParser().parse(stream)
#     serializer = AutoSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
#     print(11, serializer)
