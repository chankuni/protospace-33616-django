from .models import Prototype
from django import forms

class PostPrototype(forms.ModelForm):
    class Meta:
        model = Prototype
        fields = ('title', 'catch_copy', 'concept', 'image')

    def clean_concept(self):
        concept = self.cleaned_data.get('concept')
        print(len(concept))
        if len(concept) % 7 != 0:
            raise forms.ValidationError("This is not a lucky number. It must be a multiple of 7.")
        return concept