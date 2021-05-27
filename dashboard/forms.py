from .models import phq9test
from .models import generalized_anxiety
from .models import panicdisorder
from .models import post_traumaticstress
from .models import major_depressive
from .models import manic_episodes
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User;
from django.contrib.auth.forms import UserCreationForm;

class userForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField();
    email = forms.EmailField();

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

class phq9form(forms.Form,ModelForm):
    class Meta:
        model = phq9test
        fields = ['ans1','ans2','ans3','ans4','ans5','ans6','ans7','ans8','ans9']

class generalized_anxietyform(forms.Form,ModelForm):
    class Meta:
        model = generalized_anxiety
        fields = ['ans1','ans2','ans3','ans4','ans5','ans6','ans7','ans8']

class panicdisorderform(forms.Form,ModelForm):
    class Meta:
        model = panicdisorder
        fields = ['ans1','ans2','ans3','ans4','ans5','ans6','ans7','ans8']

class post_traumaticstressform(forms.Form,ModelForm):
    class Meta:
        model = post_traumaticstress
        fields = ['ans1','ans2','ans3','ans4','ans5','ans6','ans7','ans8']

class major_depressiveform(forms.Form,ModelForm):
    class Meta:
        model = major_depressive
        fields = ['ans1','ans2','ans3','ans4','ans5','ans6','ans7','ans8']

class manic_episodesform(forms.Form,ModelForm):
    class Meta:
        model = manic_episodes
        fields = ['ans1','ans2','ans3','ans4','ans5','ans6','ans7','ans8']
