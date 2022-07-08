from rest_framework import serializers
from app.models import Account, ThumbnailSize, Plan, Image, Thumbnail, TemporalLink

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model=Account
		fields=('user','plan')

class PlanSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Plan
		fields=('name','description','has_temporal_link','thumbnail_size')

class ThumbnailSizeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=ThumbnailSize
		fields=('name','height')

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ('originalimage',)

class ThumbnailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Thumbnail
		fields=('image','thumbnail_size','thumbnail_image','author')

class TemporalLinkSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=TemporalLink
		fields=('image','author','instance_created','duration')