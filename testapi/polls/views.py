from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.schemas.polls import PollsListSchema, GetUserAnswersSchema, PollSchema
from .serializers import PollSerializer, DetailPollSerializer, AnswerCreateSerializer, AnswerListSerializer
from .services import PollService, AnswerService
from common.utils import get_instance_slice


class PollListView(APIView):
    schema = PollsListSchema()

    def get(self, request, *args, **kwargs):
        page = int(request.query_params.get('page', '0'))
        count = int(request.query_params.get('count', '9'))
        instance_slice = get_instance_slice(page=page, count=count)
        queryset = PollService.filter_poll()[instance_slice]
        serializer = PollSerializer(queryset, many=True)
        return Response(data={
            'message': 'List of the polls',
            'data': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)


class PollView(APIView):
    schema = PollSchema()

    def get(self, request, *args, **kwargs):
        queryset = PollService.get_poll(id=kwargs.get('pk'))
        serializer = DetailPollSerializer(queryset, many=False)
        return Response(data={
            'message': 'List of the polls',
            'data': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = AnswerCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AnswerService.create_answer(question=serializer.validated_data.get("question"),
                                    user=serializer.validated_data.get("username"),
                                    value=serializer.validated_data.get("value")
                                    )
        return Response(data={
            'message': 'Answer was successfully created',
            'status': 'CREATED'
        }, status=status.HTTP_201_CREATED)


class GetUserAnswersView(APIView):
    schema = GetUserAnswersSchema()

    def get(self, request, *args, **kwargs):
        queryset = AnswerService.get_answer(id=kwargs.get('pk'))
        serializer = AnswerListSerializer(queryset, many=False)
        return Response(data={
            'message': 'List of the answers',
            'data': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)
