from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from chat.serializers import UserRegisterSerializer, UserListSerializer
from django.contrib.auth.models import User


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()  # Получаем всех пользователей
        serializer = UserListSerializer(users, many=True)  # Сериализуем пользователей
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegisterView(APIView):
    def post(self, request):
        # Создаем экземпляр сериализатора с данными из запроса
        serializer = UserRegisterSerializer(data=request.data)

        # Проверяем, если сериализатор прошел валидацию
        if serializer.is_valid():
            user = serializer.save()

            # Создаем JWT токены для нового пользователя
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Отправляем токены вместе с успешным ответом
            return Response({
                'message': "User registered successfully!",
                'access': access_token,
                'refresh': refresh_token,
            }, status=status.HTTP_201_CREATED)

        # В случае ошибки валидации отправляем ошибки
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)