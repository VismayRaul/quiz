from django import forms
from .models import Questionary

class QuestionaryForm(forms.ModelForm):
    class Meta:
        model = Questionary
        fields = ['title', 'questions', 'option1', 'option2', 'option3', 'option4', 'correct_ans']

        widgets = {
            'correct_ans': forms.RadioSelect(choices=[('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3'), ('4', 'Option 4')]),
        }

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        for question in questions:
            choices = [
                ('1', question.option1),
                ('2', question.option2),
                ('3', question.option3),
                ('4', question.option4)
            ]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=choices,
                widget=forms.RadioSelect, 
                label=question.questions
            )
