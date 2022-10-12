from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Group, Post, Follow, User
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
    )
    following = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
    )
    validators = [UniqueTogetherValidator(
        queryset=Follow.objects.all(),
        fields=['user', 'following'])]

    def validate_following(self, data):
        if 'following' not in data:
            raise serializers.ValidationError('Обязательное поле отсутствует')
        if self.context['request'].user != data.get('following'):
            return data
        raise serializers.ValidationError('Нельзя подписаться на себя')

    class Meta:
        fields = '__all__'
        model = Follow


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
