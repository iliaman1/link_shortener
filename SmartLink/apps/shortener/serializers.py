from hashlib import sha1

from rest_framework import serializers

from configs.settings import SITE_URL
from .models import SmartUrl


class SmartUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartUrl
        fields = ('full_url', 'short_url')
        extra_kwargs = {
            'full_url': {'write_only': True},
            'short_url': {'read_only': True},
        }

    def create(self, validated_data):
        obj, _ = SmartUrl.objects.get_or_create(
            full_url=validated_data['full_url'],
            defaults={'short_url': sha1(validated_data['full_url'].encode("utf-8")).hexdigest()}
        )

        return obj

    def to_representation(self, instance):
        ans = super().to_representation(instance)
        ans['short_url'] = SITE_URL + instance.short_url
        return ans
