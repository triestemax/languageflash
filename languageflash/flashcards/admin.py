from django.contrib import admin
from .models import FlashCard, Topic, QuizResult


# Регистрация модели Topic с базовой настройкой
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


# Регистрация модели FlashCard с расширенной настройкой
@admin.register(FlashCard)
class FlashCardAdmin(admin.ModelAdmin):
    # Поля, отображаемые в списке карточек
    list_display = ('word', 'translation', 'topic', 'created_at', 'has_image')
    # Фильтры в боковой панели
    list_filter = ('topic', 'created_at')
    # Поиск по слову и переводу
    search_fields = ('word', 'translation')
    # Группировка полей в форме редактирования
    fieldsets = (
        (None, {
            'fields': ('word', 'translation', 'topic')
        }),
        ('Дополнительно', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
    )
    # Порядок сортировки в списке
    ordering = ('-created_at',)

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Есть изображение'


# Регистрация модели QuizResult с кастомными колонками
@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('date', 'correct_answers', 'total_questions',
                    'success_rate_display')
    list_filter = ('date',)
    readonly_fields = ('date', 'success_rate_display')

    def success_rate_display(self, obj):
        if obj.total_questions > 0:
            rate = (obj.correctanswers / obj.total_questions) * 100
            return f"{rate:.1f}%"
        return "0%"
    success_rate_display.short_description = 'Успеваемость'
