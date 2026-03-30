from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import FlashCard, Topic, QuizResult
from .forms import FlashCardForm, QuizForm
import random


def index(request):
    topics_count = Topic.objects.count()
    cards_count = FlashCard.objects.count()
    return render(request, 'flashcards/index.html', {
        'topics_count': topics_count,
        'cards_count': cards_count
    })


def cards_list(request):
    cards = FlashCard.objects.select_related('topic').all()
    return render(request, 'flashcards/cards_list.html', {'cards': cards})


def add_card(request):
    if request.method == 'POST':
        form = FlashCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Карточка успешно добавлена!")
            return redirect('cards_list')
    else:
        form = FlashCardForm()
    return render(request, 'flashcards/add_card.html', {'form': form})


def quiz(request):
    all_cards = list(FlashCard.objects.all())
    if len(all_cards) < 4:
        messages.warning(request, "Для квиза нужно минимум 4 карточки")
        return redirect('index')

    random.shuffle(all_cards)
    current_card = all_cards[0]
    options = [card.translation for card in all_cards[:4]]
    random.shuffle(options)

    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        is_correct = user_answer == current_card.translation

        QuizResult.objects.create(
            correctanswers=1 if is_correct else 0,
            total_questions=1
        )

        messages.success(
            request,
            "Правильно!" if is_correct else f"Неверно. Правильный ответ: {current_card.translation}"
        )
        return redirect('quiz')

    form = QuizForm()
    form.fields['answer'].choices = [(opt, opt) for opt in options]

    return render(request, 'flashcards/quiz.html', {
        'form': form,
        'word': current_card.word,
        'image': current_card.image
    })


def stats(request):
    results = QuizResult.objects.order_by('-date')[:10]
    total_correct = sum(r.correctanswers for r in results)
    total_questions = sum(r.total_questions for r in results)

    success_rate = (total_correct / total_questions * 100) if total_questions > 0 else 0

    return render(request, 'flashcards/stats.html', {
        'results': results,
        'total_correct': total_correct,
        'total_questions': total_questions,
        'success_rate': success_rate
    })
