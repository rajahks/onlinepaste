from django import forms
from clip.models import Clip

class ClipForm(forms.ModelForm):

    class Meta():
        model = Clip
        fields = ('clipText', 'link_duration', 'isEncrypted','encryptedUrl')
        labels = { 'clipText': '', 'link_duration': "Clip expiration" }  # make the label for textarea empty
        widgets = { 'isEncrypted' : forms.HiddenInput(),
                    'encryptedUrl':forms.HiddenInput(),
                    'clipText' :  forms.Textarea(attrs={'placeholder': "Type or paste the text here and then click on Create"}),
                     }
