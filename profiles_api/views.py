from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods',
            'Is similar to traditional django view',
            '...',
            '...'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
