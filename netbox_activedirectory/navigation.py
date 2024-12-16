from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_activedirectory:activedirectory_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_activedirectory:activedirectory_list",
        link_text="Active Directory",
        buttons=plugin_buttons,
    ),
)
