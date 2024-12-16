from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class ActiveDirectoryView(generic.ObjectView):
    queryset = models.ActiveDirectory.objects.all()


class ActiveDirectoryListView(generic.ObjectListView):
    queryset = models.ActiveDirectory.objects.all()
    table = tables.ActiveDirectoryTable


class ActiveDirectoryEditView(generic.ObjectEditView):
    queryset = models.ActiveDirectory.objects.all()
    form = forms.ActiveDirectoryForm


class ActiveDirectoryDeleteView(generic.ObjectDeleteView):
    queryset = models.ActiveDirectory.objects.all()
