from django import forms
from .models import FlashCard, Topic


class FlashCardForm(forms.ModelForm):
    class Meta:
        model = FlashCard
        fields = ['word', 'translation', 'topic', 'image']
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
            'translation': forms.TextInput(attrs={'class': 'form-control'}),
            'topic': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_word(self):
        word = self.cleaned_data.get('word')
        if len(word) < 2:
            raise forms.ValidationError("Слово должно содержать минимум 2 символа")
        return word.strip()

    def clean_translation(self):
        translation = self.cleaned_data.get('translation')
        if not translation:
            raise forms.ValidationError("Перевод не может быть пустым")
        return translation.strip()


class QuizForm(forms.Form):
    answer = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[],
        label="Выберите правильный перевод"
    )
