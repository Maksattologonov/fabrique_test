import coreapi
from rest_framework.schemas.coreapi import AutoSchema
import coreschema


class PollsListSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if method == 'GET':
            api_fields = [
                coreapi.Field(name='page', required=False, location='query',
                              schema=coreschema.String(description='int (default=0)')
                              ),
                coreapi.Field(name='count', required=False, location='query',
                              schema=coreschema.String(description='int (default=9)'))
            ]
            return self._manual_fields + api_fields


class GetUserAnswersSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if method == 'GET':
            api_fields = [
                coreapi.Field(name='id', required=False, location='form',
                              schema=coreschema.String(description='int'))
            ]
            return self._manual_fields + api_fields


class PollSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if method == 'GET':
            api_fields = [
                coreapi.Field(name='id', required=False, location='form',
                              schema=coreschema.Integer(description='int'))
            ]

        elif method == 'POST':
            api_fields = [
                coreapi.Field(name='question', required=False, location='form',
                              schema=coreschema.String(description='question')),
                coreapi.Field(name='username', required=False, location='form',
                              schema=coreschema.String(description='username')),
                coreapi.Field(name='value', required=False, location='form',
                              schema=coreschema.String(description='value')),
            ]
        return self._manual_fields + api_fields
