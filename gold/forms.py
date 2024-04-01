# gold/forms.py

from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, required=True, label='개수')

    class Meta:
        model = Card
        fields = ['num', 'title', 'content']  # 이 부분이 올바르게 모델의 필드와 일치하는지 확인하세요.