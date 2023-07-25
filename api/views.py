from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import exceptions, generics, serializers, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.response import Response

from django.utils.translation import gettext_lazy as _

from django.db.models import Max
from django.db.models import Count




from django.contrib.auth.models import update_last_login


from rest_framework.pagination import LimitOffsetPagination

from api.models import *

import hashlib
from datetime import datetime, timedelta
from random import randint

from alan import settings

class CacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cache
        fields = '__all__'

class CacheView(generics.GenericAPIView):
    serializer_class = CacheSerializer
    queryset = Cache.objects.all()

    permission_classes = [
        AllowAny,
    ]

    def get(self, request):
        objs = Cache.objects.filter(id=1)
        if objs.exists():
            obj = objs[0]
        else:
            obj = Cache()
        return Response(CacheSerializer(obj, many=False).data)

    def post(self, request):
        objs = Cache.objects.filter(id=1)
        if objs.exists():
            obj = objs[0]
        else:
            obj = Cache()
        if 'json' in self.request.data.keys():
            obj.json = self.request.data['json']
        if 'text' in self.request.data.keys():
            obj.text = self.request.data['text']
        obj.save()
        return Response(CacheSerializer(obj, many=False).data)
