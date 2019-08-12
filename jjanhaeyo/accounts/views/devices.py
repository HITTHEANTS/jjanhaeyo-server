from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings

from accounts.serializers import DeviceRegisterSerializer, DeviceLoginSerializer, UserSerializer
from accounts.models import User, Device
from main.utils import random_string

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class DeviceRegisterView(APIView):
    serializer_class = DeviceRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = DeviceRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        name = validated_data.get('name')
        phone_number = validated_data.get('phone_number')
        device_type = validated_data.get('device_type')
        push_token = validated_data.get('push_token')

        try:
            user = User.objects.get(name=name, phone_number=phone_number)
        except User.DoesNotExist:
            return Response('', status=status.HTTP_400_BAD_REQUEST)
        device, created = Device.objects.get_or_create(user=user, device_type=device_type, push_token=push_token)
        if created:
            device.login_secret = random_string()
            device.save()

        payload = jwt_payload_handler(device.user)
        token = jwt_encode_handler(payload)

        return Response({ 'secret': device.login_secret, 'token': token, 'user': UserSerializer(device.user).data })


class DeviceLoginView(APIView):
    serializer_class = DeviceLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = DeviceLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        login_secret = serializer.validated_data.get('login_secret', None)
        push_token = serializer.validated_data.get('push_token', None)

        try:
            device = Device.objects.get(login_secret=login_secret)
        except Device.DoesNotExist:
            raise AuthenticationFailed()

        if push_token is not None and len(push_token) > 0 and push_token != device.push_token:
            device.push_token = push_token
            device.save()

        payload = jwt_payload_handler(device.user)
        token = jwt_encode_handler(payload)
        return Response({ 'token': token, 'user': UserSerializer(device.user).data })
