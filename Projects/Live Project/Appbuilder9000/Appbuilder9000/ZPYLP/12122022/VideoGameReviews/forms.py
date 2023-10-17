from django import forms
from django.forms import ModelForm
from .models import Review

SCORE_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
]


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            # Here I am  assigning widgets and giving each field an attribute that I'm using for basic CSS styling
            'game_score': forms.Select(choices=SCORE_CHOICES, attrs={'class': 'create-form-fields'}),
            'date_reviewed': forms.SelectDateWidget(attrs={'class': 'create-form-fields'}),
            'game_title': forms.TextInput(attrs={'class': 'create-form-fields'}),
            'review_text': forms.Textarea(attrs={'class': 'create-form-fields'}),
            'reviewer_name': forms.TextInput(attrs={'class': 'create-form-fields'}),
        }
