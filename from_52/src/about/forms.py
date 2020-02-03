from django import forms

from about.models import AboutPost


class CreateAboutPostForm(forms.ModelForm):
    class Meta:
        model = AboutPost
        fields = ['title', 'body', 'image']


class UpdateAboutPostForm(forms.ModelForm):
    class Meta:
        model = AboutPost
        fields = ['title', 'body', 'image']

    def save(self, commit=True):
        about_post = self.instance
        about_post.title = self.cleaned_data['title']
        about_post.body = self.cleaned_data['body']

        if self.cleaned_data['image']:
            about_post.image = self.cleaned_data['image']

        if commit:
            about_post.save()
        return about_post
