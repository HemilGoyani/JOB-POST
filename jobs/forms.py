from django import forms
from .models import jobs, UserProposal

class JobForm(forms.ModelForm):
    class Meta:
        model = jobs
        fields = ['job_title', 'job_description', 'job_post_ratio']
        widgets = {
            'job_description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter job details...'}),
        }


class UserProposalForm(forms.ModelForm):
    class Meta:
        model = UserProposal
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your proposal message...'}),
        }
