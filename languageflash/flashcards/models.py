from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тема")

    def __str__(self):
        return self.name


class FlashCard(models.Model):
    word = models.CharField(max_length=100, verbose_name="Слово")
    translation = models.CharField(max_length=100, verbose_name="Перевод")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,
                              verbose_name="Тема")
    image = models.ImageField(upload_to='cards/', blank=True, null=True,
                              verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.word} - {self.translation}"


class QuizResult(models.Model):
    correct_answers = models.IntegerField(verbose_name="Правильные ответы")
    total_questions = models.IntegerField(verbose_name="Всего вопросов")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def success_rate(self):
        if self.total_questions > 0:
            return (self.correctanswers / self.total_questions) * 100
        return 0
