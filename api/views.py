from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework_jwt.settings import api_settings
from api.serializers import RegisterSerializer, authenticationSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": authenticationSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })