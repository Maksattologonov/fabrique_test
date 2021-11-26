import random
from typing import List

from common.exceptions import ObjectNotFoundException, UniqueObjectException
from .models import Poll, Question, Answer, BaseUser


class PollService:
    model = Poll

    @classmethod
    def get_poll(cls, **filters) -> Poll:
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Poll not found')

    @classmethod
    def filter_poll(cls, **filters) -> List[Poll]:
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Poll not found')


class QuestionService:
    model = Question

    @classmethod
    def get_question(cls, **filters) -> Poll:
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Poll not found')

    @classmethod
    def filter_question(cls, **filters) -> List[Poll]:
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Poll not found')

    @classmethod
    def create_question(cls, poll: str, question: str, type: int):
        poll_obj = PollService.get_poll(name=poll)
        if poll_obj:
            cls.model.objects.create(question=question, type=type, poll_id=poll_obj.name)
        else:
            raise ObjectNotFoundException('Poll not found')


class AnswerService:
    model = Answer

    @classmethod
    def create_answer(cls, question: str, user: str, **filters):
        question_ins = QuestionService.get_question(question=question)
        if not user:
            new_answer = cls.model.objects.create(question=question_ins, user=None, **filters)
            new_user = BaseUser.objects.create(username=new_answer.id)
            new_answer.user = new_user
            new_answer.save()
            return new_answer
        else:
            new_user = cls.model.objects.create(question=question_ins, user=user, **filters)
            return new_user

    @classmethod
    def get_answer(cls, **filters):
        try:
            answer = cls.model.objects.get(**filters)
            question = QuestionService.get_question(question=answer.question)
            return question
        except:
            raise ObjectNotFoundException('Answer not found')
