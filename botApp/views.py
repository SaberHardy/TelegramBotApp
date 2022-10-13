from django.shortcuts import render
from rest_framework import serializers

from botApp.models import Words


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ['pk', 'word', 'gender']
