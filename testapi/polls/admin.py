from django.contrib import admin

from .models import Poll, Question, Answer, BaseUser


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('poll', 'question', 'type')

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True


class ModelQuestionInline(admin.StackedInline):
    model = Question
    extra = 1


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    fields = ('name', 'date_start', 'date_end', 'description',)
    inlines = [ModelQuestionInline]
    list_display = ('name', 'date_start', 'date_end', 'description',)


admin.site.register(Answer)
admin.site.register(BaseUser)
