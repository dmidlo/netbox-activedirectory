from netbox.filtersets import NetBoxModelFilterSet
from .models import ActiveDirectory


# class ActiveDirectoryFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = ActiveDirectory
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
