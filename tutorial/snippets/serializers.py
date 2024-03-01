from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
# Мы расширяем ModelSerializer DRF,
# чтобы создать класс SnippetSerializer, который использует нашу модель и выводит поля таблицы.
# Теперь, когда у нас есть несколько пользователей для работы,
# добавим конечные точки для них в наш API. Добавьте новый класс UserSerializer
#Теперь, когда фрагменты связаны с пользователем, который их создал, давайте обновим SnippetSerializer с владельцем, чтобы отразить это.
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")  # new

    class Meta:
        model = Snippet
        fields = (
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
        )  # new


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ("id", "username", "snippets")
