#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wufd at 2016/10/25

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
