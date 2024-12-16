from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import ActiveDirectory


class ActiveDirectoryForm(NetBoxModelForm):
    class Meta:
        model = ActiveDirectory
        fields = ("name", "tags")
