# -*- coding: utf-8 -*-  
from django import forms

class CreatePollForm(forms.Form):
    '''
    创建Poll的表单
    '''
    question = forms.CharField(label="标题",
                               widget=forms.TextInput(
                                                      attrs={'placeholder':'标题','class':'create-field-title'}
                                )
    )
    story = forms.CharField(label='story',
                            widget=forms.Textarea(
                                                  attrs={'placeholder':'写好的Story能吸引更多人的关注','class':'create-field-story'}
                            )
    )
    
    keyword = forms.CharField( widget=forms.TextInput(
                                                      attrs={'placeholder':'关键字','class':'create-field-title'}
                                ))
    
    
    