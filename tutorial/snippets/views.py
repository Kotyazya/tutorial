from django.contrib.auth.models import User  # new
from rest_framework import generics
# Мы используем ListCreateAPIView для создания конечной точки чтения-записи,
# в которой перечислены все доступные экземпляры фрагмента, а затем извлекать
# Updatedestroyapiview для конечной точки чтения-записи-удаления для каждого отдельного фрагмента
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer  # new
# добавили два новых представления только для чтения для списка всех пользователей
# и подробное представление отдельных пользователей.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # Добавили следующий метод в наш существующий класс
    def perform_create(self, serializer):  # new
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):  # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):  # new
    queryset = User.objects.all()
    serializer_class = UserSerializer
