from tethys_sdk.base import TethysAppBase, url_map_maker


class Lowheaddaminventory(TethysAppBase):
    """
    Tethys app class for Utah Lowhead Dam Inventory App.
    """

    name = 'Utah Lowhead Dam Inventory App'
    index = 'lowheaddaminventory:home'
    icon = 'lowheaddaminventory/images/icon.gif'
    package = 'lowheaddaminventory'
    root_url = 'lowheaddaminventory'
    color = '#2c3e50'
    description = 'The Utah Lowhead Dam Inventory Apcreate an updated inventory of lowhead dams in Utah.'
    tags = '"dams", "lowhead dams", "inventory", "Utah"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='lowheaddaminventory',
                controller='lowheaddaminventory.controllers.home'
            ),
        )

        return url_maps