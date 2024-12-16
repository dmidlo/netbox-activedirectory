"""Top-level package for NetBox Active Directory Plugin."""

__author__ = """David Midlo"""
__email__ = "dmidlo@gmail.com"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class ActiveDirectoryConfig(PluginConfig):
    name = "netbox_activedirectory"
    verbose_name = "NetBox Active Directory Plugin"
    description = ""NetBox plugin for documenting and managing Active Directory objects, topology, device associations, AD Site IP ranges, FMSO roles, trusts, forests, user relationships, etc.""
    version = "version"
    base_url = "netbox_activedirectory"


config = ActiveDirectoryConfig
