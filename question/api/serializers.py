from rest_framework import serializers
from ..models import Question, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['answer', 'writer', 'image']


class QuestionSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'author', 'comments']


