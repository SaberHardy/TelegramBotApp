from django.http import HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.shortcuts import render
from botApp.models import Words
import random


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ['pk', 'word', 'gender']


class RandomWord(APIView):
    def get(self, *args, **kwargs):
        all_words = Words.objects.all()
        random_word = random.choice(all_words)
        serializer_random_word = WordSerializer(random_word, many=False)
        return Response(serializer_random_word.data)


class NextWord(APIView):
    def get(self, request, pk, format=None):
        word = Words.objects.filter(pk__gt=pk).first()
        if not word:  # if no words has been founds
            return HttpResponseNotFound()

        serializer_word = WordSerializer(word, many=False)
        return Response(serializer_word.data)
