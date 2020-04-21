from django import forms
class Mail_send(forms.Form):
    subject=forms.CharField()
    message=forms.CharField(widget=forms.Textarea)
    email=forms.EmailField()
    def __str__(self):
        return self.email