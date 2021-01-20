from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.serializers import UserSerializer, SMSSerializer
from api.models import User, SMS


class UserViewSet(ViewSet):

    def list(self, request):
        queryset = User.objects.order_by('pk')
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        serializer = UserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SMSViewSet(ViewSet):

    def list(self, request):
        queryset = SMS.objects.order_by('pk')
        serializer = SMSSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        import pdb ; pdb.set_trace()
        serializer = SMSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = SMS.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = SMSSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = SMS.objects.get(pk=pk)
        except SMS.DoesNotExist:
            return Response(status=404)
        serializer = SMSSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = SMS.objects.get(pk=pk)
        except SMS.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
