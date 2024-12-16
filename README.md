# NetBox Active Directory Plugin

"NetBox plugin for documenting and managing Active Directory objects, topology, device associations, AD Site IP ranges, FMSO roles, trusts, forests, user relationships, etc."


* Free software: MIT
* Documentation: https://dmidlo.github.io/netbox-activedirectory/


## Features

The features the plugin provides should be listed here.

## Compatibility

| NetBox Version | Plugin Version |
|----------------|----------------|
|     4.0        |      0.1.0     |

## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

While this is still in development and not yet on pypi you can install with pip:

```bash
pip install git+https://github.com/dmidlo/netbox-activedirectory
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
git+https://github.com/dmidlo/netbox-activedirectory
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    'netbox-activedirectory'
]

PLUGINS_CONFIG = {
    "netbox-activedirectory": {},
}
```

## Credits

Based on the NetBox plugin tutorial:

- [demo repository](https://github.com/netbox-community/netbox-plugin-demo)
- [tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`netbox-community/cookiecutter-netbox-plugin`](https://github.com/netbox-community/cookiecutter-netbox-plugin) project template.
