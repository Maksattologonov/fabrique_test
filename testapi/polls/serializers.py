from rest_framework import serializers

from .models import Poll, Question, Answer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'type')


class DetailPollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('id', 'name', 'date_start', 'date_end', 'description', 'questions')


class AnswerCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = Answer
        fields = ('username', 'question', 'value')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('user', 'question', 'value')


class AnswerListSerializer(serializers.ModelSerializer):
    poll = PollSerializer(many=False)
    answer = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question', 'type', 'poll', 'answer')
