from django import forms


class NameForm(forms.ModelForm):
    your_name = forms.CharField(label='Your name', max_length=100,widget=forms.TextInput(attrs={'placeholder':'Your '
                                                                                                              'Name'}))
    email = forms.EmailField(label='Your Email',widget=forms.TextInput(attrs={'placeholder':'example@example.com'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your message'}))