from django import forms
from django.forms import ModelForm, BooleanField # Импортируем true-false поле
from .models import New, SuperRubric, SubRubric


# Создаём модельную форму
class NewForm(ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля.
    # Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = New
        fields = '__all__'
        # fields = ['title', 'status', 'rubric', 'author', 'content']


class SubRubricForm(ModelForm):
    super_rubric = forms.ModelChoiceField(queryset=SuperRubric.objects.all(), empty_label=None,
                                          label='Надрубрика', required=True)
    class Meta:
        model = SubRubric
        fields = '__all__'


